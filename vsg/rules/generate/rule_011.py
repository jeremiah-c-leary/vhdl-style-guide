# -*- coding: utf-8 -*-

from vsg import parser, token, violation
from vsg.rule_group import structure
from vsg.rules import utils as rules_utils
from vsg.vhdlFile import utils

oInsertTokens = token.for_generate_statement.end_generate_label
oAnchorTokens = token.for_generate_statement.semicolon
oLeftTokens = token.for_generate_statement.end_keyword
oRightTokens = token.for_generate_statement.semicolon
oValueTokens = token.for_generate_statement.generate_label

lRemoveTokens = []
lRemoveTokens.append(token.for_generate_statement.end_generate_label)
lRemoveTokens.append(token.if_generate_statement.end_generate_label)
lRemoveTokens.append(token.case_generate_statement.end_generate_label)


class rule_011(structure.Rule):
    """
    This rule checks the **end generate**  label on for, case and if generate statements.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       ram_array : for i in 0 to 127 generate

       end generate;

    **Fix**

    .. code-block:: vhdl

       ram_array : for i in 0 to 127 generate

       end generate ram_array;
    """

    def __init__(self):
        super().__init__()
        self.solution = "generate label"
        self.insert_token = oInsertTokens
        self.anchor_token = oAnchorTokens
        self.left_token = oLeftTokens
        self.right_token = oRightTokens
        self.value_token = oValueTokens
        self.groups.append("structure::optional")
        self.configuration_documentation_link = None
        self.action = "add"
        self.configuration.append("action")
        self.configuration_documentation_link = "configuring_optional_items_link"

    def _get_tokens_of_interest(self, oFile):
        if remove_keyword(self):
            return oFile.get_token_and_n_tokens_before_it(lRemoveTokens, 1)
        else:
            return oFile.get_tokens_bounded_by(token.architecture_body.begin_keyword, token.architecture_body.end_keyword)

    def _analyze(self, lToi):
        if remove_keyword(self):
            analyze_for_existence_of_optional_keyword(lToi, self)
        else:
            analyze_for_missing_optional_keyword(lToi, self)

    def _fix_violation(self, oViolation):
        if remove_keyword(self):
            rules_utils.remove_optional_item(oViolation)
        else:
            add_optional_item(oViolation)


def add_optional_item(oViolation):
    lTokens = oViolation.get_tokens()
    dAction = oViolation.get_action()
    lTokens.append(parser.whitespace(" "))
    lTokens.append(dAction["label"])
    oViolation.set_tokens(lTokens)


def analyze_for_existence_of_optional_keyword(lToi, self):
    for oToi in lToi:
        oViolation = create_violation(oToi, oToi.get_line_number(), self)
        self.add_violation(oViolation)


def analyze_for_missing_optional_keyword(lToi, self):
    for oToi in lToi:
        iLine, lTokens = utils.get_toi_parameters(oToi)
        lLabels = []
        for iToken, oToken in enumerate(lTokens):
            iLine = utils.increment_line_number(iLine, oToken)

            if manage_labels(oToken, lLabels):
                continue

            if isinstance(oToken, token.for_generate_statement.end_generate_keyword):
                if not utils.are_next_consecutive_token_types_ignoring_whitespace([token.for_generate_statement.end_generate_label], iToken + 1, lTokens):
                    oNewToi = oToi.extract_tokens(iToken, iToken)
                    dAction = {}
                    dAction["label"] = token.for_generate_statement.end_generate_label(lLabels[-1].get_value())
                    sSolution = "Add label " + lLabels[-1].get_value()
                    oViolation = violation.New(oNewToi.get_line_number(), oNewToi, sSolution)
                    oViolation.set_action(dAction)
                    self.add_violation(oViolation)
                continue

            if isinstance(oToken, token.if_generate_statement.end_generate_keyword):
                if not utils.are_next_consecutive_token_types_ignoring_whitespace([token.if_generate_statement.end_generate_label], iToken + 1, lTokens):
                    oNewToi = oToi.extract_tokens(iToken, iToken)
                    dAction = {}
                    dAction["label"] = token.if_generate_statement.end_generate_label(lLabels[-1].get_value())
                    sSolution = "Add label " + lLabels[-1].get_value()
                    oViolation = violation.New(oNewToi.get_line_number(), oNewToi, sSolution)
                    oViolation.set_action(dAction)
                    self.add_violation(oViolation)
                continue

            if isinstance(oToken, token.case_generate_statement.end_generate_keyword):
                if not utils.are_next_consecutive_token_types_ignoring_whitespace([token.case_generate_statement.end_generate_label], iToken + 1, lTokens):
                    oNewToi = oToi.extract_tokens(iToken, iToken)
                    dAction = {}
                    dAction["label"] = token.case_generate_statement.end_generate_label(lLabels[-1].get_value())
                    sSolution = "Add label " + lLabels[-1].get_value()
                    oViolation = violation.New(oNewToi.get_line_number(), oNewToi, sSolution)
                    oViolation.set_action(dAction)
                    self.add_violation(oViolation)
                continue


def manage_labels(oToken, lLabels):
    if isinstance(oToken, token.for_generate_statement.generate_label):
        lLabels.append(oToken)
        return True

    if isinstance(oToken, token.if_generate_statement.generate_label):
        lLabels.append(oToken)
        return True

    if isinstance(oToken, token.case_generate_statement.generate_label):
        lLabels.append(oToken)
        return True

    if isinstance(oToken, token.for_generate_statement.semicolon):
        lLabels.pop()
        return True

    if isinstance(oToken, token.if_generate_statement.semicolon):
        lLabels.pop()
        return True

    if isinstance(oToken, token.case_generate_statement.semicolon):
        lLabels.pop()
        return True

    return False


def remove_keyword(self):
    if self.action == "remove":
        return True
    return False


def create_violation(oToi, iLineNumber, self):
    sSolution = self.action.capitalize() + " " + self.solution
    oViolation = violation.New(iLineNumber, oToi, sSolution)
    return oViolation
