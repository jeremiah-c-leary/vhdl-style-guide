
from vsg import token
from vsg import violation

from vsg.rule_group import case

lPortTokens = []
lPortTokens.append(token.interface_unknown_declaration.identifier)
lPortTokens.append(token.interface_constant_declaration.identifier)
lPortTokens.append(token.interface_variable_declaration.identifier)
lPortTokens.append(token.interface_signal_declaration.identifier)

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


class rule_601(case.Rule):
    '''
    This rule checks for consistent capitalization of port names in an architecture body.

    **Violation**

    .. code-block:: vhdl

       entity FIFO is
         port (
           I_DATA : in std_logic_vector(31 downto 0)
         );
       end entity fifo;

       architecture rtl of fifo is

       begin

          register <= i_data;

       end architecture rtl;

    **Fix**

    .. code-block:: vhdl

       entity FIFO is
         port (
           I_DATA : in std_logic_vector(31 downto 0)
         );
       end entity fifo;

       architecture rtl of fifo is

       begin

          register <= I_DATA;

       end architecture rtl;
    '''

    def __init__(self):
        case.Rule.__init__(self, name="architecture", identifier="601")
        self.subphase = 2

    def analyze(self, oFile):
        lPorts = extract_port_names_from_entities(oFile)

        if no_ports_detected(lPorts):
            return None

        lArchitectures = oFile.get_tokens_bounded_by(oStartToken, oEndToken)
        for oArchitecture in lArchitectures:
            oArchitecture.name = extract_entity_name(oArchitecture)
            lArchitecturePorts = lPorts[oArchitecture.name]
            lToi = extract_token_pairs(oArchitecture, lPairs)
            lToi.extend(extract_component_instantiation_actual_parts(oArchitecture))
            for oToi in lToi:
                validate_port_name_in_token_list(self, lArchitecturePorts, oToi)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dActions = oViolation.get_action()
        lTokens[0].set_value(dActions['value'])
        oViolation.set_tokens(lTokens)


def extract_component_instantiation_actual_parts(oArchitecture):
    lReturn = []

    lInstantiations = extract_component_instantiations(oArchitecture)
    for oInstantiation in lInstantiations:
        lGenericMapAspects = extract_generic_map_aspect(oInstantiation)
        lReturn.extend(extract_actual_part_tokens_from_aspects(lGenericMapAspects))
        lPortMapAspects = extract_port_map_aspect(oInstantiation)
        lReturn.extend(extract_actual_part_tokens_from_aspects(lPortMapAspects))
    return lReturn


def extract_component_instantiations(oArchitecture):
    return extract_token_pairs(oArchitecture, [[token.component_instantiation_statement.label_colon, token.component_instantiation_statement.semicolon]])


def extract_generic_map_aspect(oInstantiation):
    return extract_token_pairs(oInstantiation, [[token.generic_map_aspect.open_parenthesis, token.generic_map_aspect.close_parenthesis]])


def extract_port_map_aspect(oInstantiation):
    return extract_token_pairs(oInstantiation, [[token.port_map_aspect.open_parenthesis, token.port_map_aspect.close_parenthesis]])


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


def no_ports_detected(lPorts):
    if len(lPorts) == 0:
        return True
    return False


def validate_port_name_in_token_list(self, lMyPorts, oToi):
    lMyPortsLower = []
    dPortMap = {}
    for sPort in lMyPorts:
        lMyPortsLower.append(sPort.lower())
        dPortMap[sPort.lower()] = sPort

    lTokens = oToi.get_tokens()
    for iToken, oToken in enumerate(lTokens):
        sToken = oToken.get_value()
        if port_case_mismatch(sToken, lMyPorts, lMyPortsLower):
            oViolation = create_violation(sToken, iToken, dPortMap, oToi)
            self.add_violation(oViolation)


def create_violation(sToken, iToken, dPortMap, oToi):
    sSolution = 'Port case mismatch:  Change ' + sToken + ' to ' + dPortMap[sToken.lower()]
    oNewToi = oToi.extract_tokens(iToken, iToken)
    oViolation = violation.New(oNewToi.get_line_number(), oNewToi, sSolution)
    dAction = {}
    dAction['value'] = dPortMap[sToken.lower()]
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


def port_case_mismatch(sToken, lPorts, lPortsLower):
    if sToken.lower() in lPortsLower and sToken not in lPorts:
        return True
    return False


def extract_matching_value(sFind, lValues):
    sLower = sFind.lower()
    for sValue in lValues:
        if sLower == sValue.lower():
            return sValue


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


def extract_port_names_from_entities(oFile):
    lEntities = oFile.get_tokens_bounded_by(token.entity_declaration.identifier, token.entity_declaration.end_keyword)
    lPorts = {}
    for oEntity in lEntities:
        oEntity.name = extract_entity_name(oEntity)
        lPorts[oEntity.name] = extract_port_names(oEntity)
    return lPorts


def extract_entity_name(oToi):
    lTokens = oToi.get_tokens()
    for oToken in lTokens:
        if isinstance(oToken, token.entity_declaration.identifier):
            return oToken.get_value().lower()
        if isinstance(oToken, token.architecture_body.entity_name):
            return oToken.get_value().lower()


def extract_port_names(oToi):
    lReturn = []

    bSearch = False
    for oToken in oToi.get_tokens():
        bSearch = end_search(oToken, bSearch)
        lReturn.extend(extract_port_token(bSearch, oToken, lPortTokens))
        bSearch = start_search(oToken, bSearch)
    return lReturn


def end_search(oToken, bSearch):
    if isinstance(oToken, token.port_clause.close_parenthesis):
        return False
    return bSearch


def extract_port_token(bSearch, oToken, lPortTokens):
    lReturn = []
    if bSearch:
        if is_token_in_token_type_list(oToken, lPortTokens):
            lReturn.append(oToken.get_value())
    return lReturn


def start_search(oToken, bSearch):
    if isinstance(oToken, token.port_clause.open_parenthesis):
        return True
    return bSearch


def is_token_in_token_type_list(oToken, lTokenTypes):
    for oTokenType in lTokenTypes:
        if isinstance(oToken, oTokenType):
            return True
    return False
