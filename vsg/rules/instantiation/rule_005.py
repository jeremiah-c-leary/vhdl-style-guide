# -*- coding: utf-8 -*-

from vsg import parser, violation
from vsg.rule_group import structure
from vsg.rules import utils as rules_utils
from vsg.token import generic_map_aspect, instantiated_unit, port_map_aspect as token

lTokens = [token.port_keyword]


class rule_005(structure.Rule):
    """
    This rule checks the **port map** keywords are on their own line.

    |configuring_port_map_new_line_link|

    **Violation**

    .. code-block:: vhdl

       U_FIFO : FIFO port map (

    **Fix**

    .. code-block:: vhdl

       U_FIFO : FIFO
         port map (
    """

    def __init__(self):
        super().__init__()
        self.lTokens = lTokens
        self.configuration_documentation_link = "configuring_port_map_new_line_link"
        self.after_instantiated_unit = "add_new_line"
        self.configuration.append("after_instantiated_unit")
        self.after_generic_map_aspect = "add_new_line"
        self.configuration.append("after_generic_map_aspect")

    def _get_tokens_of_interest(self, oFile):
        lReturn = []
        lToi = oFile.get_tokens_from_non_whitespace_token_until_tokens(self.lTokens)
        for oToi in lToi:
            if not oToi.token_type_exists(parser.comment):
                lReturn.append(oToi)
        return lReturn

    def _analyze(self, lToi):
        for oToi in lToi:
            if is_after_instantiated_unit(oToi):
                self.check_after_instantiated_unit(oToi)
            elif is_after_generic_map_aspect(oToi):
                self.check_after_generic_map_aspect(oToi)

    def _fix_violation(self, oViolation):
        if oViolation.get_action() == "add":
            self.fix_add_violation(oViolation)
        elif oViolation.get_action() == "remove":
            self.fix_remove_violation(oViolation)

    def fix_add_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if isinstance(lTokens[-1], parser.whitespace):
            rules_utils.insert_carriage_return(lTokens, -1)
        else:
            rules_utils.insert_carriage_return(lTokens, "end")
            rules_utils.insert_whitespace(lTokens, "end")
        oViolation.set_tokens(lTokens)

    def fix_remove_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        lNewTokens = [lTokens[0]]
        rules_utils.insert_whitespace(lNewTokens, "end")
        oViolation.set_tokens(lNewTokens)

    def check_after_instantiated_unit(self, oToi):
        self.check_for_violation(self.after_instantiated_unit, oToi)

    def check_after_generic_map_aspect(self, oToi):
        self.check_for_violation(self.after_generic_map_aspect, oToi)

    def check_for_violation(self, condition, oToi):
        if condition == "add_new_line" and not oToi.token_type_exists(parser.carriage_return):
            self.create_violation("Move port keyword to new line", "add", oToi)
        elif condition == "remove_new_line" and oToi.token_type_exists(parser.carriage_return):
            self.create_violation("Move port keyword to previous line", "remove", oToi)

    def create_violation(self, sSolution, sAction, oToi):
        oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
        oViolation.set_action(sAction)
        self.add_violation(oViolation)


def is_after_instantiated_unit(oToi):
    if (
        oToi.token_type_exists(instantiated_unit.configuration_name)
        or oToi.token_type_exists(instantiated_unit.close_parenthesis)
        or oToi.token_type_exists(instantiated_unit.component_name)
        or oToi.token_type_exists(instantiated_unit.entity_name)
    ):
        return True
    return False


def is_after_generic_map_aspect(oToi):
    if oToi.token_type_exists(generic_map_aspect.close_parenthesis):
        return True
    return False
