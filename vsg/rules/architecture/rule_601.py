
from vsg import parser
from vsg import token
from vsg import rule
from vsg.vhdlFile import utils
from vsg import violation

lTokens = []
lTokens.append(token.interface_unknown_declaration.identifier)
lTokens.append(token.interface_constant_declaration.identifier)
lTokens.append(token.interface_variable_declaration.identifier)
lTokens.append(token.interface_signal_declaration.identifier)

lIgnore = []
lIgnore.append(parser.whitespace)
lIgnore.append(parser.carriage_return)
lIgnore.append(parser.blank_line)
lIgnore.append(token.identifier.identifier)

oStartToken = token.port_clause.open_parenthesis
oEndToken = token.port_clause.close_parenthesis

oRegionStart = token.architecture_body.is_keyword
oRegionEnd = token.architecture_body.end_keyword

lPairs = []
#[token.type_declaration.is_keyword, token.type_declaration.semicolon]
#[token.subtype_declaration.is_keyword, token.subtype_declaration.semicolon]
lPairs.append([token.simple_waveform_assignment.target, token.simple_waveform_assignment.semicolon])
lPairs.append([token.concurrent_simple_signal_assignment.target, token.concurrent_simple_signal_assignment.semicolon])
lPairs.append([token.concurrent_conditional_signal_assignment.target, token.concurrent_conditional_signal_assignment.semicolon])
lPairs.append([token.constant_declaration.colon, token.constant_declaration.semicolon])
lPairs.append([token.signal_declaration.colon, token.signal_declaration.semicolon])
lPairs.append([token.variable_declaration.colon, token.variable_declaration.semicolon])
lPairs.append([token.if_statement.if_keyword, token.if_statement.then_keyword])
#[token.file_declaration.colon, token.file_declaration.semicolon]
#[token.alias_declaration.colon, token.alias_declaration.semicolon]
#[token.attribute_declaration.colon, token.attribute_declaration.semicolon]
#[token.attribute_specification.is_keyword, token.attribute_declaration.semicolon]
lPairs.append([token.process_statement.open_parenthesis, token.process_statement.close_parenthesis])
#[token.process_statement.begin_keyword, token.process_statement.end_keyword]


class rule_601(rule.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens: list of token type objects
       token type to apply the case check against
    '''

    def __init__(self):
        rule.Rule.__init__(self, name="architecture", identifier="601")
        self.solution = None
        self.phase = 6
        self.subphase = 2

    def analyze(self, oFile):
        lPorts = extract_port_names_from_entities(oFile)
        if len(lPorts) > 0:
            lArchitectures = oFile.get_tokens_bounded_by(token.architecture_body.entity_name, token.architecture_body.end_keyword)
            for oArchitecture in lArchitectures:
                oArchitecture.name = extract_entity_name(oArchitecture)
                lMyPorts = lPorts[oArchitecture.name]
                lToi = extract_token_pairs(oArchitecture, lPairs)
                for oToi in lToi:
                    validate_port_name_in_token_list(self, lMyPorts, oToi)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dActions = oViolation.get_action()
        lTokens[0].set_value(dActions['value'])
        oViolation.set_tokens(lTokens)


def validate_port_name_in_token_list(self, lMyPorts, oToi):
    lMyPortsLower = []
    dPortMap = {}
    for sPort in lMyPorts:
        lMyPortsLower.append(sPort.lower())
        dPortMap[sPort.lower()] = sPort

    iLine, lTokens = utils.get_toi_parameters(oToi)
    for iToken, oToken in enumerate(lTokens):
        sToken = oToken.get_value()
        if port_case_mismatch(sToken, lMyPorts, lMyPortsLower):
           sSolution = 'Port case mismatch:  Change ' + sToken + ' to ' + dPortMap[sToken.lower()]
           oNewToi = oToi.extract_tokens(iToken, iToken)
           oViolation = violation.New(oNewToi.get_line_number(), oNewToi, sSolution)
#           print(f'{iLine} | MisMatch!! Expected {dPortMap[sToken.lower()]}  Found {sToken}')
           dAction = {}
           dAction['value'] = dPortMap[sToken.lower()]
           oViolation.set_action(dAction)
           self.add_violation(oViolation)

#        if sToken.lower() in lMyPortsLower:
#            print(f'{iLine}|{oToken.get_value()}|{lMyPortsLower}')
#            if sToken not in lMyPorts:
#               print(f'MisMatch!! Expected {dPortMap[sToken.lower()]}  Found {sToken}')

def skip_code(oToken, bSkip):
    bReturn = bSkip
    if not bSkip:
        if isinstance(oToken, token.function_specification.function_keyword):
            bReturn = True
        if isinstance(oToken, token.procedure_specification.procedure_keyword):
            bReturn = True
    else:
        if isinstance(oToken, token.subprogram_body.semicolon):
            bReturn = False
    return bReturn


def port_case_mismatch(sToken, lPorts, lPortsLower):
    if sToken.lower() in lPortsLower:
        if sToken not in lPorts:
            return True
    return False


def extract_matching_value(sFind, lValues):
    sLower = sFind.lower()
    for iValue, sValue in enumerate(lValues):
        if sLower == sValue.lower():
            return sValue


def extract_token_pairs(oArchitecture, lPairs):
    lReturn = []
    for lPair in lPairs:
        bSkip = False
        for iToken, oToken in enumerate(oArchitecture.get_tokens()):
            bSkip = skip_code(oToken, bSkip)
            if bSkip:
                continue
            if isinstance(oToken, lPair[0]):
                iStart = iToken
            if isinstance(oToken, lPair[1]):
                lReturn.append(oArchitecture.extract_tokens(iStart, iToken))
    return lReturn


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

    lTokens = []
    lTokens.append(token.interface_unknown_declaration.identifier)
    lTokens.append(token.interface_constant_declaration.identifier)
    lTokens.append(token.interface_variable_declaration.identifier)
    lTokens.append(token.interface_signal_declaration.identifier)

    bSearch = False
    for oToken in oToi.get_tokens():
        if isinstance(oToken, token.port_clause.close_parenthesis):
            break
        if bSearch: 
            if is_token_in_token_type_list(oToken, lTokens):
                lReturn.append(oToken.get_value())
        if isinstance(oToken, token.port_clause.open_parenthesis):
            bSearch = True
    return lReturn


def is_token_in_token_type_list(oToken, lTokenTypes):
    for oTokenType in lTokenTypes:
        if isinstance(oToken, oTokenType):
            return True
    return False
