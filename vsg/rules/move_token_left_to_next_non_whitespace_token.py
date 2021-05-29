

from vsg import rule
from vsg import parser
from vsg import violation

from vsg.rules import utils as rules_utils

from vsg.vhdlFile import utils


class move_token_left_to_next_non_whitespace_token(rule.Rule):
    '''
    Moves one token to the left until it encounters a non whitespace token.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    anchor_token : token type
       The token which another token will moved next to.

    token_to_move : token type
       The token which will be moved next to the anchor token.
    '''

    def __init__(self, name, identifier, token_to_move):
        rule.Rule.__init__(self, name, identifier)
        self.solution = None
        self.phase = 1
        self.subphase = 2
        self.token_to_move = token_to_move

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_between_non_whitespace_token_and_token(self.token_to_move)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()

            if does_a_whitespace_token_separate_tokens(lTokens):
                continue
            sSolution = 'Move **then** keyword to same line as ' + lTokens[0].get_value()            
            oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
            oViolation.set_remap()
            oViolation.fix_blank_lines = True
            self.add_violation(oViolation)


    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()

        rules_utils.insert_token(lTokens, 1, lTokens.pop())
        rules_utils.insert_whitespace(lTokens, 1)
        
        lNewTokens = utils.remove_consecutive_whitespace_tokens(lTokens)
        lNewTokens = utils.remove_trailing_whitespace(lNewTokens)
        lNewTokens = utils.fix_blank_lines(lNewTokens)

        oViolation.set_tokens(lNewTokens)


def does_a_whitespace_token_separate_tokens(lTokens):
    if len(lTokens) == 3:
        return True
    return False

