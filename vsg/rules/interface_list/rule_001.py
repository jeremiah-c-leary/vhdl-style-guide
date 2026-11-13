# -*- coding: utf-8 -*-

from vsg import parser, token, violation
from vsg.rule_group import structure

lParenthesisPairs = []
lParenthesisPairs.append([token.generic_clause.open_parenthesis, token.generic_clause.close_parenthesis])
lParenthesisPairs.append([token.port_clause.open_parenthesis, token.port_clause.close_parenthesis])
lParenthesisPairs.append([token.subprogram_header.open_parenthesis, token.subprogram_header.close_parenthesis])
lParenthesisPairs.append([token.procedure_specification.open_parenthesis, token.procedure_specification.close_parenthesis])
lParenthesisPairs.append([token.function_specification.open_parenthesis, token.function_specification.close_parenthesis])
lParenthesisPairs.append([token.interface_procedure_specification.open_parenthesis, token.interface_procedure_specification.close_parenthesis])
lParenthesisPairs.append([token.interface_function_specification.open_parenthesis, token.interface_function_specification.close_parenthesis])

lSkipTokens = (parser.whitespace, parser.carriage_return, parser.blank_line, parser.comment)


class rule_001(structure.Rule):
    """
    This rule checks for the optional trailing semicolon at the end of interface lists.
    VHDL-2019 allows a semicolon after the last element of generic, port and subprogram parameter lists.

    The default action is "remove", which keeps code compatible with earlier VHDL standards.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       port (
         a : in    std_logic;
         b : out   std_logic;
       );

    **Fix**

    .. code-block:: vhdl

       port (
         a : in    std_logic;
         b : out   std_logic
       );
    """

    def __init__(self):
        super().__init__()
        self.solution = "trailing semicolon"
        self.groups.append("structure::optional")
        self.action = "remove"
        self.configuration.append("action")
        self.configuration_documentation_link = "configuring_optional_items_link"

    def _get_tokens_of_interest(self, oFile):
        lReturn = []
        for oLeft, oRight in lParenthesisPairs:
            lReturn.extend(oFile.get_tokens_bounded_by(oLeft, oRight))
        lReturn.sort(key=lambda oToi: oToi.get_start_index())
        return lReturn

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLast = find_last_significant_token(lTokens)
            if iLast is None:
                continue
            bHasSemicolon = isinstance(lTokens[iLast], token.interface_list.semicolon)
            if self.action == "remove" and bHasSemicolon:
                iStart = iLast
                if isinstance(lTokens[iLast - 1], parser.whitespace):
                    iStart = iLast - 1
                oNewToi = oToi.extract_tokens(iStart, iLast)
                self.add_violation(violation.New(oToi.extract_tokens(iLast, iLast).get_line_number(), oNewToi, "Remove " + self.solution))
            elif self.action == "add" and not bHasSemicolon:
                oNewToi = oToi.extract_tokens(iLast, iLast)
                self.add_violation(violation.New(oNewToi.get_line_number(), oNewToi, "Add " + self.solution))

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if self.action == "remove":
            oViolation.set_tokens([])
        else:
            oViolation.set_tokens(lTokens + [token.interface_list.semicolon()])


def find_last_significant_token(lTokens):
    """Returns the index of the last token before the closing parenthesis which is not whitespace or a comment."""
    for iIndex in range(len(lTokens) - 2, 0, -1):
        if not isinstance(lTokens[iIndex], lSkipTokens):
            return iIndex
    return None
