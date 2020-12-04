

from vsg import parser
from vsg import rule
from vsg import violation


class insert_token_right_of_token_if_it_does_not_exist_before_token(rule.Rule):
    '''
    Checks for the existence of a token and will insert it if it does not exist.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    insert_token : token object
       token to insert if it does not exist.

    anchor_token : token object type
       token to check if insert_token exists to the right of

    end_token : token object type
       token that bounds the search for the insert_token
    '''

    def __init__(self, name, identifier, insert_token, anchor_token, end_token):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.insert_token = insert_token
        self.anchor_token = anchor_token
        self.end_token = end_token

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by(self.anchor_token, self.end_token)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            bFound = False
            for oToken in lTokens:
                if isinstance(oToken, type(self.insert_token)):
                    bFound = True
                    break
            if not bFound:
                self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        lTokens.insert(1, self.insert_token)
        lTokens.insert(1, parser.whitespace(' '))
        oViolation.set_tokens(lTokens)
