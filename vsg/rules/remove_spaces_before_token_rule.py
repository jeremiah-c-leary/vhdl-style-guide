
from vsg import parser
from vsg import violation

from vsg.rule_group import whitespace


class remove_spaces_before_token_rule(whitespace.Rule):
    '''
    This class removes whitespace before a given token.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    oToken : token object
       The token where spaces will be removed before.
    '''

    def __init__(self, name, identifier, oToken, bIgnoreIfLineStart=False):

        whitespace.Rule.__init__(self, name, identifier)
        self.oToken = oToken
        self.bIgnoreIfLineStart = bIgnoreIfLineStart

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_sequence_of_tokens_matching([parser.whitespace, self.oToken], self.bIgnoreIfLineStart)

    def _analyze(self, lToi):
        for oToi in lToi:
            self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        oViolation.set_tokens(lTokens[1:])
