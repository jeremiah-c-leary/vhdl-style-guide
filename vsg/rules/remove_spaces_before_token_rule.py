
from vsg import parser
from vsg import rule
from vsg import violation


class remove_spaces_before_token_rule(rule.Rule):
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

        rule.Rule.__init__(self, name, identifier)
        self.phase = 2
        self.oToken = oToken
        self.solution = None
        self.bIgnoreIfLineStart = bIgnoreIfLineStart

    def analyze(self, oFile):
        lTokens = oFile.get_sequence_of_tokens_matching([parser.whitespace, self.oToken], self.bIgnoreIfLineStart)
        for oToken in lTokens:
            self.add_violation(violation.New(oToken.get_line_number(), oToken, self.solution))

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        oViolation.set_tokens(lTokens[1:])
