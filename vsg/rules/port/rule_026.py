# -*- coding: utf-8 -*-

import copy

from vsg import parser, violation
from vsg.rule_group import structure
from vsg.token import (
    identifier_list,
    interface_list,
    interface_unknown_declaration,
    port_clause as token,
)


class rule_026(structure.Rule):
    """
    This rule checks for multiple identifiers on port declarations.

    Any comments are not replicated.

    **Violation**

    .. code-block:: vhdl

       port (
         wr_en, rd_en : in    std_logic;  -- Comment
         data     : inout std_logic;
         overflow, empty : out   std_logic -- Other comment
       );

    **Fix**

    .. code-block:: vhdl

       port (
         wr_en    : in    std_logic;
         rd_en    : in    std_logic;  -- Comment
         data    : inout std_logic
         overflow : out   std_logic;
         empty : out   std_logic -- Other comment
       );
    """

    def __init__(self):
        super().__init__()
        self.subphase = 2
        self.configuration_documentation_link = None

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_interface_elements_between_tokens(token.open_parenthesis, token.close_parenthesis)

    def _analyze(self, lToi):
        for oToi in lToi:
            if not oToi.token_type_exists(identifier_list.comma):
                continue
            lTokens = oToi.get_tokens()

            ### Find identifiers ###
            lIdentifiers = []
            lIdentifierIndexes = []
            for iToken, oToken in enumerate(lTokens):
                if isinstance(oToken, interface_unknown_declaration.identifier):
                    lIdentifiers.append(oToken.get_value())
                    lIdentifierIndexes.append(iToken)

            sSolution = "Split identifiers " + ", ".join(lIdentifiers) + " to individual lines."
            dAction = {}
            if oToi == lToi[-1]:
                dAction["last_element"] = False
            else:
                dAction["last_element"] = True
            dAction["identifier_indexes"] = lIdentifierIndexes
            dAction["split_index"] = lIdentifierIndexes[-1] + 1
            oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
            oViolation.set_action(dAction)
            self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        """
        Applies fixes for any rule violations.
        """
        lTokens = oViolation.get_tokens()
        lNewTokens = []
        dAction = oViolation.get_action()
        for iIndex in dAction["identifier_indexes"]:
            lCopyTokens = duplicate_tokens(lTokens)
            lNewTokens.append(lCopyTokens[iIndex])

            lNewTokens.extend(lCopyTokens[dAction["split_index"] :])

            if iIndex != dAction["identifier_indexes"][-1]:
                lNewTokens.append(interface_list.semicolon())
                lNewTokens.append(parser.carriage_return())
        oViolation.set_tokens(lNewTokens)


def duplicate_tokens(lTokens):
    lReturn = []
    for oToken in lTokens:
        lReturn.append(copy.deepcopy(oToken))
    return lReturn
