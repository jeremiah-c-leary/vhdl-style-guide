# -*- coding: utf-8 -*-

from vsg import parser, violation
from vsg.rule_group import whitespace as ws_group
from vsg.vhdlFile import utils


class rule_002(ws_group.Rule):
    """
    This rule will check for the existence of tabs in the middle of a line.

    **Violation**

    .. code-block:: text

       \\t\\tsignal wr_en\\t:\\tstd_logic;  --\\tWrite Enable

    **Fix**

    .. code-block:: text

       \\t\\tsignal wr_en : std_logic;  -- Write Enable
    """

    def __init__(self):
        super().__init__()
        self.phase = 1
        self.solution = "Remove tab"
        self.configuration_documentation_link = None

    def _get_tokens_of_interest(self, oFile):
        lTemp = oFile.get_tokens_matching_not_at_beginning_or_ending_of_line([parser.whitespace])
        lToia = []
        for oToi in lTemp:
            lTokens = oToi.get_tokens()
            if lTokens[0].has_tab:
                lToia.append(oToi)

        lTemp = oFile.get_tokens_matching([parser.comment])
        lToib = []
        for oToi in lTemp:
            lTokens = oToi.get_tokens()
            if lTokens[0].has_tab:
                lToib.append(oToi)

        lReturn = utils.combine_two_token_class_lists(lToia, lToib)
        return lReturn

    def _analyze(self, lToi):
        for oToi in lToi:
            create_violation(oToi, self)

    def _fix_violation(self, oViolation):
        dAction = oViolation.get_action()
        if dAction["action"] == "remove_tab_from_comment":
            remove_tab_from_comment(oViolation)
        else:
            remove_tab(oViolation)


def create_violation(oToi, self):
    lTokens = oToi.get_tokens()
    oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
    dAction = define_action(lTokens)
    oViolation.set_action(dAction)
    self.add_violation(oViolation)


def whitespace_exists(oToi):
    lTokens = oToi.get_tokens()
    if isinstance(lTokens[1], parser.whitespace):
        return True
    return False


def define_action(lTokens):
    dAction = {}
    if isinstance(lTokens[0], parser.comment):
        dAction["action"] = "remove_tab_from_comment"
    else:
        dAction["action"] = "remove_tab"
    return dAction


def need_to_remove_whitespace(dAction):
    if dAction["action"] == "remove":
        return True
    return False


def remove_tab(oViolation):
    lTokens = oViolation.get_tokens()
    myToken = lTokens.pop()
    sValue = myToken.get_value()
    sValue = sValue.replace("\t", "  ")
    lTokens.append(parser.whitespace(sValue))
    lTokens[0].has_tab = False


def remove_tab_from_comment(oViolation):
    lTokens = oViolation.get_tokens()
    myToken = lTokens.pop()
    sValue = myToken.get_value()
    sValue = sValue.replace("\t", "  ")
    lTokens.append(parser.comment(sValue))
    lTokens[0].has_tab = False
