

from vsg import parser

from vsg.rules.whitespace_between_tokens import Rule as WhitespaceRule

from vsg.vhdlFile import utils


class Rule(WhitespaceRule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of token type pairs
       The tokens to check for a single space between
    '''

    def __init__(self, name, identifier, lTokens, oStart, oEnd):
        WhitespaceRule.__init__(self, name=name, identifier=identifier)
        self.lTokens = lTokens
        self.oStart = oStart
        self.oEnd = oEnd

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for lTokenPair in self.lTokens:
            lToi_a = oFile.get_sequence_of_tokens_matching_bounded_by_tokens([lTokenPair[0], parser.whitespace, lTokenPair[1]], self.oStart, self.oEnd)
            lToi = utils.combine_two_token_class_lists(lToi, lToi_a)
            lToi_a = oFile.get_sequence_of_tokens_matching_bounded_by_tokens(lTokenPair, self.oStart, self.oEnd)
            lToi = utils.combine_two_token_class_lists(lToi, lToi_a)
        return lToi
