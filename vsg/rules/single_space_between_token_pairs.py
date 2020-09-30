

from vsg import parser
from vsg import rule_item
from vsg import violation

from vsg.vhdlFile import utils


class single_space_between_token_pairs(rule_item.Rule):
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
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 2
        self.lTokens = lTokens

    def analyze(self, oFile):
        lToi = []
        for lTokenPair in self.lTokens:
            lToi_a = oFile.get_sequence_of_tokens_matching([lTokenPair[0], parser.whitespace, lTokenPair[1]])
            lToi = utils.combine_two_token_class_lists(lToi, lToi_a)
            lToi_a = oFile.get_sequence_of_tokens_matching(lTokenPair)
            lToi = utils.combine_two_token_class_lists(lToi, lToi_a)

        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if len(lTokens) == 2:
                self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))
            elif len(lTokens[1].get_value()) != 1:
                self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))


    def fix(self, oFile):
        '''
        Applies fixes for any rule violations.
        '''
        if self.fixable:
            self.analyze(oFile)
            self._print_debug_message('Fixing rule: ' + self.name + '_' + self.identifier)
            self._fix_violation(oFile)
            self.violations = []

    def _fix_violation(self, oFile):
        for oViolation in self.violations:
            lTokens = oViolation.get_tokens()
            if isinstance(lTokens[1], parser.whitespace):
                lTokens[1].set_value(' ')
            else:
                lTokens.insert(1, parser.whitespace(' '))
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)


