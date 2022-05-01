

from vsg import parser
from vsg import violation

from vsg.rule_group import structure
from vsg.rules import utils as rules_utils
from vsg.vhdlFile import utils


class move_token(structure.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    oToken : token type
       object type to split a line at
    '''

    def __init__(self, name, identifier, oToken):
        structure.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.oToken = oToken
        self.action = 'new_line'
        self.configuration.append('action')
        self.preserve_comment = False
        self.insert_whitespace = False

    def _get_tokens_of_interest(self, oFile):
        if self.action == 'new_line' and not self.preserve_comment:
            return get_toi_for_new_line_option(self, oFile)
        elif self.action == 'new_line' and self.preserve_comment:
            return get_toi_for_new_line_option_with_preserve_comment(self, oFile)
        else:
            return get_toi_for_move_left_option(self, oFile)

    def _analyze(self, lToi):
        if self.action == 'new_line' and not self.preserve_comment:
            analyze_new_line(self, lToi)
        elif self.action == 'new_line' and self.preserve_comment:
            analyze_new_line_with_preserve_comment(self, lToi)
        else:
            analyze_move_left(self, lToi)

    def _fix_violation(self, oViolation):
        if self.action == 'new_line' and not self.preserve_comment:
            fix_new_line_violations(oViolation)
        elif self.action == 'new_line' and self.preserve_comment:
            fix_new_line_with_preserve_comment_violations(oViolation)
        else:
            fix_move_left_violations(oViolation)


def tokens_are_next_to_each_other(lTokens):
    if len(lTokens) == 2:
        return True
    return False


def get_toi_for_new_line_option(self, oFile):
    lReturn = []
    lToi = oFile.get_token_and_n_tokens_before_it([self.oToken], 2)
    for oToi in lToi:
        lTokens = oToi.get_tokens()
        if isinstance(lTokens[0], parser.carriage_return) or isinstance(lTokens[1], parser.carriage_return):
            continue
        lReturn.append(oToi)
    return lReturn


def get_toi_for_new_line_option_with_preserve_comment(self, oFile):
    lReturn = []
    lToi = oFile.get_line_which_includes_tokens([self.oToken])
    for oToi in lToi:
        lTokens = oToi.get_tokens()
        if not rules_utils.token_at_the_beginning_of_a_line(self.oToken, lTokens):
            lReturn.append(oToi)
    return lReturn


def get_toi_for_move_left_option(self, oFile):
    lReturn = []
    lToi = oFile.get_tokens_between_non_whitespace_token_and_token(self.oToken)
    for oToi in lToi:
        if not tokens_are_next_to_each_other(oToi.get_tokens()):
            lReturn.append(oToi)
    return lReturn


def analyze_new_line(self, lToi):
    for oToi in lToi:
        lTokens = oToi.get_tokens()
        sSolution = f'Move {lTokens[-1].get_value()} to next line.'
        oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
        self.add_violation(oViolation)


def analyze_new_line_with_preserve_comment(self, lToi):
    for oToi in lToi:
        lTokens = oToi.get_tokens()
        iTokenIndex = oToi.token_index
        sSolution = f'Move {lTokens[iTokenIndex].get_value()} to next line.'
        oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
        self.add_violation(oViolation)


def analyze_move_left(self, lToi):
    for oToi in lToi:
        lTokens = oToi.get_tokens()
        if rules_utils.number_of_carriage_returns(lTokens) > 0:
            oViolation = create_move_left_violation(self, oToi)
            self.add_violation(oViolation)


def create_move_left_violation(self, oToi):
    lTokens = oToi.get_tokens()
    oFirstToken = lTokens[0]
    oLastToken = lTokens[-1]
    sSolution = f'Move {oLastToken.get_value()} next to {oFirstToken.get_value()}.'
    oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
    oViolation.insert_whitespace = False
    oViolation.insert_whitespace = self.insert_whitespace
    return oViolation


def fix_new_line_violations(oViolation):
    lTokens = oViolation.get_tokens()
    if isinstance(lTokens[1], parser.whitespace):
        rules_utils.insert_carriage_return(lTokens, -2)
    else:
        rules_utils.insert_carriage_return(lTokens, -1)
    oViolation.set_tokens(lTokens)


def fix_new_line_with_preserve_comment_violations(oViolation):
    lTokens = oViolation.get_tokens()
    iTokenIndex = oViolation.oTokens.token_index
    lTemp = []
    if isinstance(lTokens[-1], parser.comment):
        lTemp.append(lTokens.pop())
        if isinstance(lTokens[-1], parser.whitespace):
            lTemp.insert(0, lTokens.pop())
    rules_utils.insert_carriage_return(lTokens, iTokenIndex)
    lTokens[iTokenIndex:iTokenIndex] = lTemp

    oViolation.set_tokens(lTokens)


def fix_move_left_violations(oViolation):
    lTokens = oViolation.get_tokens()

    rules_utils.insert_token(lTokens, 1, lTokens.pop())
    if oViolation.insert_whitespace:
        rules_utils.insert_token(lTokens, 1, parser.whitespace(' '))

    lNewTokens = utils.remove_consecutive_whitespace_tokens(lTokens)
    lNewTokens = utils.fix_blank_lines(lNewTokens)

    oViolation.set_tokens(lNewTokens)
