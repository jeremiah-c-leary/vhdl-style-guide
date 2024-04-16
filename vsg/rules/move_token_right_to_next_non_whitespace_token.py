# -*- coding: utf-8 -*-


from vsg import parser, violation
from vsg.rule_group import structure
from vsg.rules import utils as rules_utils
from vsg.vhdlFile import utils


class move_token_right_to_next_non_whitespace_token(structure.Rule):
    """
    Moves one token to the right until it encounters a non whitespace token.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    tokens_to_move : token type
       The token which will be moved next to the anchor token.
    """

    def __init__(self, tokens_to_move):
        super().__init__()
        self.tokens_to_move = tokens_to_move
        self.bInsertWhitespace = True
        self.bRemoveTrailingWhitespace = True
        self.configuration_documentation_link = None

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for oToken in self.tokens_to_move:
            aToi = oFile.get_tokens_from_beginning_of_line_containing_token_to_the_next_non_whitespace_token_to_the_right(oToken)
            lToi = utils.combine_two_token_class_lists(lToi, aToi)
        lReturn = filter_toi(self, lToi)
        return lReturn

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iTokenIndex = oToi.get_meta_data("iTokenIndex")

            sSolution = "Move " + lTokens[iTokenIndex].get_value() + " to same line as " + lTokens[-1].get_value()
            oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
            oViolation.set_remap()
            oViolation.set_action(oToi.get_meta_data("iTokenIndex"))
            oViolation.fix_blank_lines = True
            self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        iTokenIndex = oViolation.get_action()
        rules_utils.insert_token(lTokens, -1, lTokens.pop(iTokenIndex))

        if self.bInsertWhitespace:
            rules_utils.insert_whitespace(lTokens, -1)

        lNewTokens = utils.remove_consecutive_whitespace_tokens(lTokens)
        lNewTokens = utils.remove_all_trailing_whitespace(lNewTokens)

        lNewTokens = utils.fix_blank_lines(lNewTokens)
        oViolation.set_tokens(lNewTokens)


def tokens_are_next_to_each_other(oToi):
    lTokens = oToi.get_tokens()
    iTokenIndex = oToi.get_meta_data("iTokenIndex")

    if len(lTokens) - 2 == iTokenIndex:
        return True
    return False


def filter_toi(self, lToi):
    lReturn = []
    for oToi in lToi:
        if tokens_are_next_to_each_other(oToi):
            continue
        if skip_based_on_whitespace(self.bInsertWhitespace, oToi):
            continue
        lReturn.append(oToi)
    return rules_utils.remove_tois_with_pragmas(lReturn)


def skip_based_on_whitespace(bInsertWhitespace, oToi):
    if bInsertWhitespace and does_a_whitespace_token_separate_tokens(oToi):
        return True
    return False


def does_a_whitespace_token_separate_tokens(oToi):
    lTokens = oToi.get_tokens()
    iTokenIndex = oToi.get_meta_data("iTokenIndex")

    if len(lTokens) - iTokenIndex == 3 and isinstance(lTokens[-2], parser.whitespace):
        return True
    return False
