
from vsg.rules import single_space_before_token as Rule


class single_space_before_token_if_on_same_line_as_token(Rule):
    '''
    Checks for a single space before a token.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    oFirstToken : token object
       Token to check for a single space before.

    oSecondToken : token object
       Token to use as an exclusion.
    '''

    def __init__(self, name, identifier, oFirstToken, oExceptToken):
        Rule.__init__(self, name=name, identifier=identifier, lTokens=[])
        self.oFirstToken = oFirstToken
        self.oExceptToken = oExceptToken

    def _get_tokens_of_interest(self, oFile):
        lExcept = oFile.get_line_which_includes_tokens([self.oExceptToken])
        lFilter = []
        for oExcept in lExcept:
            lFilter.append(oExcept.get_line_number())
        lReturn = []
        lToi = oFile.get_token_and_n_tokens_before_it([self.oFirstToken], 2)
        for oToi in lToi:
            if oToi.get_line_number() in lFilter:
                lReturn.append(oToi)
        return lReturn
