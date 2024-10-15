# -*- coding: utf-8 -*-

from vsg import token, violation
from vsg.rule_group import case

lInterfaceTokens = []
lInterfaceTokens.append(token.interface_unknown_declaration.identifier)
lInterfaceTokens.append(token.interface_constant_declaration.identifier)
lInterfaceTokens.append(token.interface_variable_declaration.identifier)
lInterfaceTokens.append(token.interface_signal_declaration.identifier)

lPairs = []
lPairs.append([token.concurrent_simple_signal_assignment.target, token.concurrent_simple_signal_assignment.semicolon])
lPairs.append([token.concurrent_conditional_signal_assignment.target, token.concurrent_conditional_signal_assignment.semicolon])
lPairs.append([token.constant_declaration.colon, token.constant_declaration.semicolon])
lPairs.append([token.signal_declaration.colon, token.signal_declaration.semicolon])
lPairs.append([token.variable_declaration.colon, token.variable_declaration.semicolon])
lPairs.append([token.process_statement.open_parenthesis, token.process_statement.close_parenthesis])
lPairs.append([token.process_statement.begin_keyword, token.process_statement.end_keyword])

oStartToken = token.architecture_body.entity_name
oEndToken = token.architecture_body.end_keyword


class consistent_interface_token_case(case.Rule):
    """
    Checks the case for generic and port identifiers.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens: list of token type objects
       token type to apply the case check against
    """

    def __init__(self):
        super().__init__()
        self.subphase = 2
        self.configuration_documentation_link = None
        self.map_aspect_token = None
        self.clause_token = None
        self.interface_string = None

    def analyze(self, oFile):
        lInterfaces = extract_interface_names_from_entities(oFile, self.clause_token)

        if no_interfaces_detected(lInterfaces):
            return None

        lArchitectures = oFile.get_tokens_bounded_by(oStartToken, oEndToken)
        for oArchitecture in lArchitectures:
            oArchitecture.name = extract_entity_name(oArchitecture)
            lArchitectureInterfaces = lInterfaces[oArchitecture.name]
            lToi = extract_token_pairs(oArchitecture, lPairs)
            lToi.extend(extract_component_instantiation_actual_parts(oArchitecture, self.map_aspect_token))
            for oToi in lToi:
                validate_interface_name_in_token_list(self, lArchitectureInterfaces, oToi, self.interface_string)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dActions = oViolation.get_action()
        lTokens[0].set_value(dActions["value"])
        oViolation.set_tokens(lTokens)


def extract_component_instantiation_actual_parts(oArchitecture, oMapAspectToken):
    lReturn = []

    lInstantiations = extract_component_instantiations(oArchitecture)
    for oInstantiation in lInstantiations:
        lGenericMapAspects = extract_generic_map_aspect(oInstantiation)
        lReturn.extend(extract_actual_part_tokens_from_aspects(lGenericMapAspects))
        lInterfaceMapAspects = extract_interface_map_aspect(oInstantiation, oMapAspectToken)
        lReturn.extend(extract_actual_part_tokens_from_aspects(lInterfaceMapAspects))
    return lReturn


def extract_component_instantiations(oArchitecture):
    return extract_token_pairs(oArchitecture, [[token.component_instantiation_statement.label_colon, token.component_instantiation_statement.semicolon]])


def extract_generic_map_aspect(oInstantiation):
    return extract_token_pairs(oInstantiation, [[token.generic_map_aspect.open_parenthesis, token.generic_map_aspect.close_parenthesis]])


def extract_interface_map_aspect(oInstantiation, oMapAspectToken):
    return extract_token_pairs(oInstantiation, [[oMapAspectToken.open_parenthesis, oMapAspectToken.close_parenthesis]])


def extract_actual_part_tokens_from_aspects(lMapAspect):
    lReturn = []
    for oMapAspect in lMapAspect:
        lReturn.extend(extract_actual_part_tokens_from_aspect(oMapAspect))
    return lReturn


def extract_actual_part_tokens_from_aspect(oMapAspect):
    lReturn = []
    for iToken, oToken in enumerate(oMapAspect.get_tokens()):
        lReturn.extend(extract_actual_part_token(oMapAspect, iToken, oToken))
    return lReturn


def extract_actual_part_token(oMapAspect, iToken, oToken):
    lReturn = []
    if is_actual_part_token(oToken):
        lReturn.append(oMapAspect.extract_tokens(iToken, iToken))
    return lReturn


def is_actual_part_token(oToken):
    if isinstance(oToken, token.association_element.actual_part):
        return True
    return False


def no_interfaces_detected(lInterfaces):
    if len(lInterfaces) == 0:
        return True
    return False


def validate_interface_name_in_token_list(self, lMyInterfaces, oToi, sInterface):
    lMyInterfacesLower = []
    dInterfaceMap = {}
    for sInterfaceName in lMyInterfaces:
        lMyInterfacesLower.append(sInterfaceName.lower())
        dInterfaceMap[sInterfaceName.lower()] = sInterfaceName

    lTokens = oToi.get_tokens()
    for iToken, oToken in enumerate(lTokens):
        sToken = oToken.get_value()
        if interface_case_mismatch(sToken, lMyInterfaces, lMyInterfacesLower):
            oViolation = create_violation(sInterface, sToken, iToken, dInterfaceMap, oToi)
            self.add_violation(oViolation)


def create_violation(sInterface, sToken, iToken, dInterfaceMap, oToi):
    sSolution = sInterface + " case mismatch:  Change " + sToken + " to " + dInterfaceMap[sToken.lower()]
    oNewToi = oToi.extract_tokens(iToken, iToken)
    oViolation = violation.New(oNewToi.get_line_number(), oNewToi, sSolution)
    dAction = {}
    dAction["value"] = dInterfaceMap[sToken.lower()]
    oViolation.set_action(dAction)
    return oViolation


def skip_code(oToken, bSkip):
    bReturn = bSkip

    if not bSkip:
        return start_of_skip_region_found(oToken, bReturn)

    return end_of_skip_region_found(oToken, bReturn)


def end_of_skip_region_found(oToken, bReturn):
    if isinstance(oToken, token.subprogram_body.semicolon):
        return False
    return True


def start_of_skip_region_found(oToken, bReturn):
    bReturn = function_keyword_found(oToken, bReturn)
    bReturn = procedure_keyword_found(oToken, bReturn)
    return bReturn


def function_keyword_found(oToken, bReturn):
    if isinstance(oToken, token.function_specification.function_keyword):
        return True
    return bReturn


def procedure_keyword_found(oToken, bReturn):
    if isinstance(oToken, token.procedure_specification.procedure_keyword):
        return True
    return bReturn


def interface_case_mismatch(sToken, lInterfaces, lInterfacesLower):
    if sToken.lower() in lInterfacesLower and sToken not in lInterfaces:
        return True
    return False


def extract_token_pairs(oArchitecture, lPairs):
    lReturn = []
    for lPair in lPairs:
        lReturn.extend(extract_token_pair(oArchitecture, lPair))
    return lReturn


def extract_token_pair(oArchitecture, lPair):
    lReturn = []
    bSkip = False
    iStart = None
    for iToken, oToken in enumerate(oArchitecture.get_tokens()):
        bSkip = skip_code(oToken, bSkip)
        if bSkip:
            continue
        iStart = set_start_index(iToken, oToken, lPair, iStart)
        lReturn.extend(extract_tokens_if_end_is_found(oArchitecture, iToken, oToken, lPair, iStart))
    return lReturn


def extract_tokens_if_end_is_found(oArchitecture, iToken, oToken, lPair, iStart):
    lReturn = []
    if isinstance(oToken, lPair[1]):
        lReturn.append(oArchitecture.extract_tokens(iStart, iToken))
    return lReturn


def set_start_index(iToken, oToken, lPair, iStart):
    if isinstance(oToken, lPair[0]):
        return iToken
    return iStart


def extract_interface_names_from_entities(oFile, oClauseToken):
    lEntities = oFile.get_tokens_bounded_by(token.entity_declaration.identifier, token.entity_declaration.end_keyword)
    lInterfaces = {}
    for oEntity in lEntities:
        oEntity.name = extract_entity_name(oEntity)
        lInterfaceNames = extract_interface_names(oEntity, oClauseToken)
        if lInterfaceNames != []:
            lInterfaces[oEntity.name] = lInterfaceNames
    return lInterfaces


def extract_entity_name(oToi):
    lTokens = oToi.get_tokens()
    for oToken in lTokens:
        if isinstance(oToken, token.entity_declaration.identifier):
            return oToken.get_lower_value()
        if isinstance(oToken, token.architecture_body.entity_name):
            return oToken.get_lower_value()


def extract_interface_names(oToi, oClauseToken):
    lReturn = []

    bSearch = False
    for oToken in oToi.get_tokens():
        bSearch = end_search(oToken, bSearch, oClauseToken)
        lReturn.extend(extract_interface_token(bSearch, oToken, lInterfaceTokens))
        bSearch = start_search(oToken, bSearch, oClauseToken)
    return lReturn


def end_search(oToken, bSearch, oClauseToken):
    if isinstance(oToken, oClauseToken.close_parenthesis):
        return False
    return bSearch


def extract_interface_token(bSearch, oToken, lInterfaceTokens):
    lReturn = []
    if bSearch:
        if is_token_in_token_type_list(oToken, lInterfaceTokens):
            lReturn.append(oToken.get_value())
    return lReturn


def start_search(oToken, bSearch, oClauseToken):
    if isinstance(oToken, oClauseToken.open_parenthesis):
        return True
    return bSearch


def is_token_in_token_type_list(oToken, lTokenTypes):
    for oTokenType in lTokenTypes:
        if isinstance(oToken, oTokenType):
            return True
    return False
