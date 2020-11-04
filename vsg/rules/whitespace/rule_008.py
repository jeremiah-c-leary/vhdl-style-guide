
from vsg import parser
from vsg import rule_item
from vsg import violation

from vsg.vhdlFile import utils


class rule_008(rule_item.Rule):
    '''
    Checks for spaces after "std_logic_vector"

    '''

    def __init__(self):
        rule_item.Rule.__init__(self, 'whitespace', '008')
        self.solution = 'Remove spaces after std_logic_vector'
        self.phase = 2

    def analyze(self, oFile):
        oToi = oFile.get_all_tokens()
        iLine, lTokens = utils.get_toi_parameters(oToi)
        for iToken, oToken in enumerate(lTokens[:len(lTokens) - 2]):

            iLine = utils.increment_line_number(iLine, oToken)

            if oToken.get_value().lower() == 'std_logic_vector':
                if utils.are_next_consecutive_token_types([parser.whitespace, parser.open_parenthesis], iToken + 1, lTokens):
                    lExtractedTokens = oToi.extract_tokens(iToken, iToken + 1)
                    oViolation = violation.New(iLine, lExtractedTokens, self.solution)
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
            lTokens.pop()
            oViolation.set_tokens(lTokens)
               
        oFile.update(self.violations)

