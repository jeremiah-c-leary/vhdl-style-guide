# -*- coding: utf-8 -*-

from vsg import token, violation
from vsg.rule_group import case

lInterfaceTokens = []
lInterfaceTokens.append(token.interface_unknown_declaration.identifier)
lInterfaceTokens.append(token.interface_constant_declaration.identifier)
lInterfaceTokens.append(token.interface_variable_declaration.identifier)
lInterfaceTokens.append(token.interface_signal_declaration.identifier)

lPairs = []
lPairs.append([token.simple_waveform_assignment.target, token.simple_waveform_assignment.semicolon])
lPairs.append([token.simple_variable_assignment.simple_name, token.simple_variable_assignment.semicolon])
lPairs.append([token.conditional_waveform_assignment.target, token.conditional_waveform_assignment.semicolon])
lPairs.append([token.conditional_variable_assignment.target, token.conditional_variable_assignment.semicolon])
lPairs.append([token.concurrent_simple_signal_assignment.target, token.concurrent_simple_signal_assignment.semicolon])
lPairs.append([token.concurrent_conditional_signal_assignment.target, token.concurrent_conditional_signal_assignment.semicolon])
lPairs.append([token.constant_declaration.colon, token.constant_declaration.semicolon])
lPairs.append([token.signal_declaration.colon, token.signal_declaration.semicolon])
lPairs.append([token.variable_declaration.colon, token.variable_declaration.semicolon])
lPairs.append([token.process_statement.open_parenthesis, token.process_statement.close_parenthesis])
lPairs.append([token.process_statement.begin_keyword, token.process_statement.end_keyword])


class consistent_subprogram_parameter_token_case(case.Rule):
    """
    Checks the case for formal parameter interface identifiers.

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
        self.subprogram_token = None
        self.start_token = None
        self.end_token = token.subprogram_body.end_keyword

    def analyze(self, oFile):
        lInterfaces = extract_interface_names_from_subprograms(oFile, self.start_token, self.subprogram_token)

        if no_interfaces_detected(lInterfaces):
            return None

        lSubprogramBodies = oFile.get_tokens_bounded_by_tokens_unless_token_is_between_them(
            self.start_token, self.end_token, token.subprogram_declaration.semicolon
        )
        for oSubprogramBody in lSubprogramBodies:
            oSubprogramBody.name = extract_subprogram_name(oSubprogramBody, self.subprogram_token)
            lSubprogramInterfaces = lInterfaces[oSubprogramBody.name]
            lToi = extract_token_pairs(oSubprogramBody, lPairs)
            # lToi.extend(extract_component_instantiation_actual_parts(oSubprogramBody, self.map_aspect_token))
            for oToi in lToi:
                validate_interface_name_in_token_list(self, lSubprogramInterfaces, oToi)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dActions = oViolation.get_action()
        lTokens[0].set_value(dActions["value"])
        oViolation.set_tokens(lTokens)


def no_interfaces_detected(lInterfaces):
    if len(lInterfaces) == 0:
        return True
    return False


def validate_interface_name_in_token_list(self, lMyInterfaces, oToi):
    lMyInterfacesLower = []
    dInterfaceMap = {}
    for sInterfaceName in lMyInterfaces:
        lMyInterfacesLower.append(sInterfaceName.lower())
        dInterfaceMap[sInterfaceName.lower()] = sInterfaceName

    lTokens = oToi.get_tokens()
    for iToken, oToken in enumerate(lTokens):
        sToken = oToken.get_value()
        if interface_case_mismatch(sToken, lMyInterfaces, lMyInterfacesLower):
            oViolation = create_violation(sToken, iToken, dInterfaceMap, oToi)
            self.add_violation(oViolation)


def create_violation(sToken, iToken, dInterfaceMap, oToi):
    sSolution = "Parameter case mismatch:  Change " + sToken + " to " + dInterfaceMap[sToken.lower()]
    oNewToi = oToi.extract_tokens(iToken, iToken)
    oViolation = violation.New(oNewToi.get_line_number(), oNewToi, sSolution)
    dAction = {}
    dAction["value"] = dInterfaceMap[sToken.lower()]
    oViolation.set_action(dAction)
    return oViolation


def interface_case_mismatch(sToken, lInterfaces, lInterfacesLower):
    if sToken.lower() in lInterfacesLower and sToken not in lInterfaces:
        return True
    return False


def extract_token_pairs(oSubprogramBody, lPairs):
    lReturn = []
    for lPair in lPairs:
        lReturn.extend(extract_token_pair(oSubprogramBody, lPair))
    return lReturn


def extract_token_pair(oSubprogram, lPair):
    lReturn = []
    iStart = None
    for iToken, oToken in enumerate(oSubprogram.get_tokens()):
        iStart = set_start_index(iToken, oToken, lPair, iStart)
        lReturn.extend(extract_tokens_if_end_is_found(oSubprogram, iToken, oToken, lPair, iStart))
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


def extract_interface_names_from_subprograms(oFile, oSubprogramKeywordToken, oSubprogramToken):
    lSubprograms = oFile.get_tokens_bounded_by(oSubprogramKeywordToken, oSubprogramToken.close_parenthesis)
    lInterfaces = {}
    for oSubprogram in lSubprograms:
        oSubprogram.name = extract_subprogram_name(oSubprogram, oSubprogramToken)
        lInterfaceNames = extract_interface_names(oSubprogram, oSubprogramToken)
        if lInterfaceNames != []:
            lInterfaces[oSubprogram.name] = lInterfaceNames
    return lInterfaces


def extract_subprogram_name(oToi, oSubprogramToken):
    lTokens = oToi.get_tokens()
    for oToken in lTokens:
        if isinstance(oToken, oSubprogramToken.designator):
            return oToken.get_lower_value()


def extract_interface_names(oToi, oSubprogramToken):
    lReturn = []

    bSearch = False
    for oToken in oToi.get_tokens():
        bSearch = end_search(oToken, bSearch, oSubprogramToken)
        lReturn.extend(extract_interface_token(bSearch, oToken, lInterfaceTokens))
        bSearch = start_search(oToken, bSearch, oSubprogramToken)
    return lReturn


def end_search(oToken, bSearch, oSubprogramToken):
    if isinstance(oToken, oSubprogramToken.close_parenthesis):
        return False
    return bSearch


def extract_interface_token(bSearch, oToken, lInterfaceTokens):
    lReturn = []
    if bSearch:
        if is_token_in_token_type_list(oToken, lInterfaceTokens):
            lReturn.append(oToken.get_value())
    return lReturn


def start_search(oToken, bSearch, oSubprogramToken):
    if isinstance(oToken, oSubprogramToken.open_parenthesis):
        return True
    return bSearch


def is_token_in_token_type_list(oToken, lTokenTypes):
    for oTokenType in lTokenTypes:
        if isinstance(oToken, oTokenType):
            return True
    return False
