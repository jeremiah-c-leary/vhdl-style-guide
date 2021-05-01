

from vsg import parser
from vsg import rule
from vsg import violation

from vsg.rules import utils as rules_utils

from vsg.vhdlFile import utils


class insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_and_not_on_same_line_as_token(rule.Rule):
    '''
    Checks function parameters are on their own line except if they are all on the same line.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.
    '''

    def __init__(self, name, identifier, token, oSameLineToken):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.token = token
        self.oSameLineToken = oSameLineToken

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by(self.token, parser.carriage_return, include_trailing_whitespace=True)

    def _analyze(self, lToi):
        for oToi in lToi:
           lTokens = oToi.get_tokens()
           if utils.are_next_consecutive_token_types([parser.carriage_return], 1, lTokens):
               continue
           if utils.are_next_consecutive_token_types([parser.whitespace, parser.comment], 1, lTokens):
               continue
           if utils.are_next_consecutive_token_types([parser.comment], 1, lTokens):
               continue
           for oToken in lTokens:
               if isinstance(oToken, self.oSameLineToken):
                   break
           else:
               self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        rules_utils.insert_carriage_return(lTokens, 1)
        oViolation.set_tokens(lTokens)
