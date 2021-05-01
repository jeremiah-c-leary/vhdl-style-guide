

from vsg import parser
from vsg import rule
from vsg import violation

from vsg.rules import utils as rules_utils

from vsg.vhdlFile import utils


class single_space_between_tokens(rule.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    left_token : token object
       The left token to check for a space between the right token

    right_token : token object
       The right token to check for a space between the left token
    '''

    def __init__(self, name, identifier, left_token, right_token):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 2
        self.left_token = left_token
        self.right_token = right_token

    def _get_tokens_of_interest(self, oFile):
        lToi_a = oFile.get_sequence_of_tokens_matching([self.left_token, parser.whitespace, self.right_token])
        lToi_b = oFile.get_sequence_of_tokens_matching([self.left_token, self.right_token])

        return utils.combine_two_token_class_lists(lToi_a, lToi_b)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if len(lTokens) == 2:
                self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))
            elif len(lTokens[1].get_value()) != 1:
                self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if isinstance(lTokens[1], parser.whitespace):
            lTokens[1].set_value(' ')
        else:
            rules_utils.insert_whitespace(lTokens, 1)
        oViolation.set_tokens(lTokens)
