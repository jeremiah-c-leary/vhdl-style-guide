# -*- coding: utf-8 -*-


from vsg import parser, violation
from vsg.rule_group import alignment
from vsg.rules import utils as rules_utils
from vsg.vhdlFile import utils


class align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token(alignment.Rule):
    """
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    token : token object
       reference token to align comments with
    """

    def __init__(self, token, bIncrement=False):
        super().__init__()
        self.phase = 4
        self.subphase = 2
        self.token = token
        self.bIncrement = bIncrement

    def _get_tokens_of_interest(self, oFile):
        lToi = oFile.get_consecutive_lines_starting_with_token_and_stopping_when_token_starting_line_is_found(parser.comment, self.token)
        lReturn = []
        for oToi in lToi:
            oToi.set_meta_data("indentLevel", oFile.get_indent_of_line_at_index(oToi.get_end_index()))
            lReturn.append(oToi)

        return lReturn

    def _analyze(self, lToi):
        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)

            iTargetIndent = lTokens[-1].get_indent()
            sExpectedWhitespace = expected_whitespace(self, oToi)

            for iToken, oToken in enumerate(lTokens):
                iLine = utils.increment_line_number(iLine, oToken)
                if comment_at_beginning_of_line(iToken, lTokens):
                    sActualWhitespace = actual_whitespace(iToken - 1, lTokens)
                    if sExpectedWhitespace != sActualWhitespace:
                        oMyToi = extract_toi(iToken, oToi)
                        oViolation = create_violation(oMyToi, sActualWhitespace, sExpectedWhitespace, lTokens[-1])
                        self.add_violation(oViolation)
                    self._adjust_token_indent(lTokens[iToken], iTargetIndent)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        if dAction["action"] == "insert":
            rules_utils.insert_new_whitespace(lTokens, len(lTokens) - 1, dAction["whitespace"])
        else:
            lTokens[0].set_value(dAction["whitespace"])
        oViolation.set_tokens(lTokens)

    def _adjust_token_indent(self, oToken, iIndent):
        oToken.set_indent(iIndent)


def expected_whitespace(self, oToi):
    iIndentLevel = oToi.get_meta_data("indentLevel")
    if self.indent_style == "smart_tabs":
        return "\t" * iIndentLevel
    return " " * iIndentLevel * self.indent_size


def actual_whitespace(iToken, lTokens):
    if iToken == -1:
        return ""
    elif rules_utils.token_is_whitespace(lTokens[iToken]):
        return lTokens[iToken].get_value()
    return ""


def comment_at_beginning_of_line(iToken, lTokens):
    oToken = lTokens[iToken]
    if rules_utils.token_is_comment(oToken):
        if iToken == 0 or iToken == 1:
            return True
        elif rules_utils.token_is_whitespace(lTokens[iToken - 1]) and rules_utils.token_is_carriage_return(lTokens[iToken - 2]):
            return True
        elif rules_utils.token_is_carriage_return(lTokens[iToken - 1]):
            return True
    return False


def create_violation(oToi, sActualWhitespace, sExpectedWhitespace, oToken):
    iLine = oToi.get_line_number()
    sSolution = "Align comment with " + oToken.get_value()
    dAction = {}
    if sActualWhitespace == "":
        dAction["action"] = "insert"
    else:
        dAction["action"] = "adjust"
    dAction["whitespace"] = sExpectedWhitespace
    oViolation = violation.New(iLine, oToi, sSolution)
    oViolation.set_action(dAction)
    return oViolation


def extract_toi(iToken, oToi):
    lTokens = oToi.get_tokens()
    if iToken == 0:
        return oToi.extract_tokens(iToken, iToken)
    elif rules_utils.token_is_whitespace(lTokens[iToken - 1]):
        return oToi.extract_tokens(iToken - 1, iToken - 1)
    return oToi.extract_tokens(iToken, iToken)
