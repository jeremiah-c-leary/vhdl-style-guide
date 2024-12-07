# -*- coding: utf-8 -*-

from vsg import parser, token, violation
from vsg.rule_group import case
from vsg.vhdlFile import utils

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
            if oSubprogram.iLine in lInterfaces.keys():
                lSubprogramInterfaces = lInterfaces[oSubprogram.iLine]
                oToi = extract_tokens(oSubprogram)
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


def validate_interface_name_in_token_list(self, lInterfaces, oToi):
    lInterfacesLower = [sInterfaceName.lower() for sInterfaceName in lInterfaces]
    dInterfaceMap = {sInterfaceName.lower(): sInterfaceName for sInterfaceName in lInterfaces}
    iSubprogramNestingDepth = 0
    dHiddenInterfaces = {}

    lTokens = oToi.get_tokens()
    for iToken, oToken in enumerate(lTokens):
        oTokenClass = oToken.__class__
        sToken = oToken.get_value()
        if oTokenClass in [token.procedure_specification.procedure_keyword, token.function_specification.function_keyword]:
            iSubprogramNestingDepth += 1
        elif oTokenClass is token.subprogram_body.end_keyword:
            dHiddenInterfaces = pop_hidden_interfaces_at_nesting_depth(dHiddenInterfaces, iSubprogramNestingDepth)
            iSubprogramNestingDepth -= 1
        elif does_token_string_match_non_hidden_interface_name(sToken.lower(), lInterfacesLower, dHiddenInterfaces):
            if is_token_of_class_potentially_hiding_interface_name(oTokenClass):
                dHiddenInterfaces[sToken.lower()] = iSubprogramNestingDepth
            elif is_token_of_class_potential_instance_of_interface_name(oTokenClass):
                if interface_case_mismatch(sToken, lInterfaces, lInterfacesLower):
                    oViolation = create_violation(sToken, iToken, dInterfaceMap, oToi)
                    self.add_violation(oViolation)


def pop_hidden_interfaces_at_nesting_depth(dHiddenInterfaces, iCurrentNestingDepth):
    return {sInterfaceName: iNestingLevel for sInterfaceName, iNestingLevel in dHiddenInterfaces.items() if iNestingLevel != iCurrentNestingDepth}


def does_token_string_match_non_hidden_interface_name(sToken, lInterfacesLower, dHiddenInterfaces):
    return sToken.lower() in lInterfacesLower and sToken.lower() not in dHiddenInterfaces.keys()


def is_token_of_class_potentially_hiding_interface_name(oTokenClass):
    return oTokenClass in [
        token.interface_unknown_declaration.identifier,
        token.interface_constant_declaration.identifier,
        token.interface_variable_declaration.identifier,
        token.interface_signal_declaration.identifier,
        token.interface_file_declaration.identifier,
        token.interface_file_declaration.identifier,
        token.constant_declaration.identifier,
        token.variable_declaration.identifier,
        token.signal_declaration.identifier,
        token.file_declaration.identifier,
    ]


def is_token_of_class_potential_instance_of_interface_name(oTokenClass):
    return oTokenClass in [
        parser.todo,
        token.todo.name,
        token.concurrent_conditional_signal_assignment.target,
        token.selected_variable_assignment.target,
        token.concurrent_selected_signal_assignment.target,
        token.concurrent_simple_signal_assignment.target,
        token.conditional_waveform_assignment.target,
        token.association_element.actual_part,
        token.selected_waveform_assignment.target,
        token.selected_force_assignment.target,
        token.simple_waveform_assignment.target,
        token.simple_force_assignment.target,
        token.simple_release_assignment.target,
    ]


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


def extract_tokens(oSubprogram):
    lTokens = oSubprogram.get_tokens()
    iStart = 0
    while not utils.does_token_type_match(lTokens[iStart], token.subprogram_body.is_keyword):
        iStart += 1
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
