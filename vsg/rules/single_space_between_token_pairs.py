

from vsg import parser
from vsg import rule
from vsg import violation

from vsg.rules import utils as rules_utils
from vsg.vhdlFile import utils


class single_space_between_token_pairs(rule.Rule):
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

    def __init__(self, name, identifier, lTokens, bMinimum=False, iSpaces=1):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 2
        self.lTokens = lTokens
        self.bMinimum = bMinimum
        self.iSpaces = iSpaces

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for lTokenPair in self.lTokens:
            lToi_a = oFile.get_sequence_of_tokens_matching([lTokenPair[0], parser.whitespace, lTokenPair[1]])
            lToi = utils.combine_two_token_class_lists(lToi, lToi_a)
            lToi_a = oFile.get_sequence_of_tokens_matching(lTokenPair)
            lToi = utils.combine_two_token_class_lists(lToi, lToi_a)
        return lToi

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if len(lTokens) == 2:
                sSolution = f'Add {self.iSpaces} space(s) between {lTokens[0].get_value()} and {lTokens[1].get_value()}'
                oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                self.add_violation(oViolation)
            elif self.bMinimum:
                continue
            elif len(lTokens[1].get_value()) != 1:
                sSolution = f'Change spaces between {lTokens[0].get_value()} and {lTokens[2].get_value()} to {self.iSpaces}'
                self.add_violation(violation.New(oToi.get_line_number(), oToi, sSolution))

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if isinstance(lTokens[1], parser.whitespace):
            lTokens[1].set_value(' ')
        else:
            rules_utils.insert_whitespace(lTokens, 1)
        oViolation.set_tokens(lTokens)
