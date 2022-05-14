
from vsg import parser

from vsg.rules.whitespace_between_tokens import Rule as WhitespaceRule


class Rule(WhitespaceRule):
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

    def __init__(self, name, identifier):
        WhitespaceRule.__init__(self, name=name, identifier=identifier)
        self.lTokens = []
        self.oFirstToken = None
        self.oExceptToken = None

    def _get_tokens_of_interest(self, oFile):
        lFilter = self._create_filter_list(oFile)
        lToi = self._extract_tois(oFile)
        lReturn = filter_toi(lFilter, lToi)
        return lReturn

    def _extract_tois(self, oFile):
        lReturn = []
        lToi = oFile.get_token_and_n_tokens_before_it([self.oFirstToken], 2)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if isinstance(lTokens[1], parser.whitespace):
                lReturn.append(oToi)
            else:
                lReturn.append(oToi.extract_tokens(1, 2))
        return lReturn

    def _create_filter_list(self, oFile):
        lExcept = oFile.get_line_which_includes_tokens([self.oExceptToken])
        lFilter = []
        for oExcept in lExcept:
            lFilter.append(oExcept.get_line_number())
        return lFilter


def filter_toi(lFilter, lToi):
    lReturn = []
    for oToi in lToi:
        if oToi.get_line_number() in lFilter:
            lReturn.append(oToi)
    return lReturn
