

from vsg import rule_item
from vsg import utils
from vsg import parser

from vsg import violation


class blank_line_below_line_ending_with_token(rule_item.Rule):
    '''
    Checks for a blank line below a line ending with a given token

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
        lToi = oFile.get_line_below_line_ending_with_token(self.lTokens)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if len(lTokens) == 1:
                if isinstance(lTokens[0], parser.blank_line):
                    continue
                if isinstance(lTokens[0], parser.comment):
                    continue
            elif len(lTokens) == 2:
                if isinstance(lTokens[0], parser.whitespace) and isinstance(lTokens[1], parser.comment):
                    continue
            else:
                oViolation = violation.New(oToi.get_line_number() - 1, oToi, self.solution)
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
            lTokens.insert(0, parser.carriage_return())
            lTokens.insert(0, parser.blank_line())
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)
