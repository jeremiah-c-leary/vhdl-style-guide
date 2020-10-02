

from vsg import rule_item
from vsg import utils
from vsg import parser

from vsg import violation


class remove_excessive_blank_lines_above_line_starting_with_token(rule_item.Rule):
    '''
    Checks for excessive blank lines below a line ending with a given token

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    token: token object type list
       token object that a blank line below should appear
    '''

    def __init__(self, name, identifier, lTokens):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = 'Insert blank line below'
        self.phase = 3
        self.lTokens = lTokens

    def analyze(self, oFile):
        lToi = oFile.get_blank_lines_above_line_starting_with_token(self.lTokens)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iCount = 0
            for oToken in lTokens:
                if isinstance(oToken, parser.blank_line):
                    iCount += 1
            if iCount > 1:
                oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
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
            lNewTokens = lTokens[0:2]
            oViolation.set_tokens(lNewTokens)
        oFile.update(self.violations)
