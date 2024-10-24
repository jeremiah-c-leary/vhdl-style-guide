# -*- coding: utf-8 -*-

from vsg import token, violation
from vsg.rule_group import case

lTokens = []
lTokens.append(token.interface_unknown_declaration.identifier)
lTokens.append(token.interface_constant_declaration.identifier)
lTokens.append(token.interface_variable_declaration.identifier)
lTokens.append(token.interface_signal_declaration.identifier)
lTokens.append(token.interface_file_declaration.identifier)


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

        if self.subprogram_token == token.procedure_specification:
            lSubprogram = oFile.get_procedure_subprogram_body()
        elif self.subprogram_token == token.function_specification:
            lSubprogram = oFile.get_function_subprogram_body()

        for oSubprogram in lSubprogram:
            lSubprogramInterfaces = lInterfaces[oSubprogram.iLine]
            oToi = extract_all_tokens(oSubprogram)
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


def extract_all_tokens(oSubprogram):
    iStart = 0
    iEnd = len(oSubprogram.get_tokens())
    return oSubprogram.extract_tokens(iStart, iEnd)


def extract_interface_names_from_subprograms(oFile, oSubprogramKeywordToken, oSubprogramToken):
    lSubprograms = oFile.get_tokens_bounded_by(oSubprogramKeywordToken, token.subprogram_body.is_keyword)
    lInterfaces = {}
    for oSubprogram in lSubprograms:
        lInterfaceNames = extract_interface_names(oSubprogram, oSubprogramToken)
        if lInterfaceNames != []:
            lInterfaces[oSubprogram.iLine] = lInterfaceNames
    return lInterfaces


def extract_interface_names(oToi, oSubprogramToken):
    lReturn = []

    bSearch = False
    for oToken in oToi.get_tokens():
        bSearch = end_search(oToken, bSearch, oSubprogramToken)
        lReturn.extend(extract_interface_token(bSearch, oToken, lTokens))
        bSearch = start_search(oToken, bSearch, oSubprogramToken)
    return lReturn


def end_search(oToken, bSearch, oSubprogramToken):
    if isinstance(oToken, oSubprogramToken.close_parenthesis):
        return False
    return bSearch


def extract_interface_token(bSearch, oToken, lTokens):
    lReturn = []
    if bSearch:
        if is_token_in_token_type_list(oToken, lTokens):
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
