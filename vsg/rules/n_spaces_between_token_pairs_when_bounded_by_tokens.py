
from vsg import parser
from vsg import rule
from vsg import violation

from vsg.rules import utils as rules_utils

from vsg.vhdlFile import utils


class n_spaces_between_token_pairs_when_bounded_by_tokens(rule.Rule):
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

    def __init__(self, name, identifier, iSpaces, lTokens, oStart, oEnd):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 2
        self.iSpaces = iSpaces
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

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if len(lTokens) == 2:
                self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))
            elif len(lTokens[1].get_value()) != self.iSpaces:
                self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if isinstance(lTokens[1], parser.whitespace):
            lTokens[1].set_value(' '*self.iSpaces)
        else:
            rules_utils.insert_whitespace(lTokens, 1, self.iSpaces)
        oViolation.set_tokens(lTokens)
