
from vsg import parser
from vsg import rule_item
from vsg import violation

from vsg.vhdlFile import utils

lTokens = []
lTokens.append(parser.open_parenthesis)


class rule_005(rule_item.Rule):
    '''
    Checks for spaces after an open parenthesis.
    '''

    def __init__(self):
        rule_item.Rule.__init__(self, 'whitespace', '005')
        self.solution = 'Remove spaces after open (.'
        self.phase = 2
        self.iSpaces = 0
        self.lTokens = [parser.open_parenthesis]

    def analyze(self, oFile):
        lToi = []

        lToi = oFile.get_n_tokens_before_and_after_tokens(2, self.lTokens)

        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)
            dAction = {}

            oRight = lTokens[-2]
            if isinstance(oRight, parser.whitespace):
                if not utils.token_is_whitespace_or_comment(lTokens[-1]):
                    if not lTokens[-1].get_value().isnumeric():
                        oViolation = violation.New(iLine, oToi, self.solution)
                        self.add_violation(oViolation)


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
            oToken = lTokens.pop()
            lTokens.pop()
            lTokens.append(oToken)
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)
