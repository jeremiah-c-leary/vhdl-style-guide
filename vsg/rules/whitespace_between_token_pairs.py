

from vsg import parser

from vsg.vhdlFile import utils

from vsg.rules.whitespace_between_tokens import Rule as WhitespaceRule


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

    def __init__(self, name, identifier, lTokens):
        WhitespaceRule.__init__(self, name=name, identifier=identifier)
        self.lTokens = lTokens

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for lTokenPair in self.lTokens:
            lToi_a = oFile.get_sequence_of_tokens_matching([lTokenPair[0], parser.whitespace, lTokenPair[1]])
            lToi = utils.combine_two_token_class_lists(lToi, lToi_a)
            lToi_a = oFile.get_sequence_of_tokens_matching(lTokenPair)
            lToi = utils.combine_two_token_class_lists(lToi, lToi_a)
        return lToi
