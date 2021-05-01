
from vsg import parser
from vsg import rule
from vsg import violation

from vsg.rules import utils as rules_utils

from vsg.vhdlFile import utils


class remove_carriage_returns_between_token_pairs(rule.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of parser object types
       object types to check the prefix

    lPrefixes : string list
       acceptable prefixes
    '''

    def __init__(self, name, identifier, lTokens, bInsertSpace=False):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.lTokens = lTokens
        self.bInsertSpace = bInsertSpace

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for oToken in self.lTokens:
            lToi_a = oFile.get_tokens_bounded_by(oToken[0], oToken[1])
            lToi = utils.combine_two_token_class_lists(lToi, lToi_a)
        return lToi

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            for oToken in lTokens:
                if isinstance(oToken, parser.carriage_return):
                    oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
                    self.add_violation(oViolation)
                    break

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()

        lTokens = utils.remove_carriage_returns_from_token_list(lTokens)
        lTokens = utils.remove_consecutive_whitespace_tokens(lTokens)
        if self.bInsertSpace:
            if not isinstance(lTokens[1], parser.whitespace):
                rules_utils.insert_whitespace(lTokens, 1)

        oViolation.set_tokens(lTokens)
