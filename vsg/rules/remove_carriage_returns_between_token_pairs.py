

from vsg import parser
from vsg import rule_item
from vsg import token
from vsg.vhdlFile import utils
from vsg import violation


class remove_carriage_returns_between_token_pairs(rule_item.Rule):
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

    def __init__(self, name, identifier, lTokens):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.lTokens = lTokens

    def analyze(self, oFile):

        lToi = []
        for oToken in self.lTokens:
            lToi_a = oFile.get_tokens_bounded_by(oToken[0], oToken[1])
            lToi = utils.combine_two_token_class_lists(lToi, lToi_a)

        for oToi in lToi:
            lTokens = oToi.get_tokens()
            for oToken in lTokens:
                if isinstance(oToken, parser.carriage_return):
                    oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
                    self.add_violation(oViolation)
                    break

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

            lTokens = utils.remove_carriage_returns_from_token_list(lTokens)
            lTokens = utils.remove_consecutive_whitespace_tokens(lTokens)

            oViolation.set_tokens(lTokens)
               
        oFile.update(self.violations)
