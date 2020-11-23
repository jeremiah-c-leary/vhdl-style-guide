
import sys

from vsg import rule
from vsg import parser
from vsg import token
from vsg import vhdlFile
from vsg import violation

from vsg.token.ieee.std_logic_1164 import function

from vsg.vhdlFile import utils


class rule_002(rule.Rule):
    '''
    Checks the expressions in if statements are enclosed in ()'s.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    trigger : parser object type
       object type to apply the case check against
    '''

    def __init__(self):
        rule.Rule.__init__(self, 'if', '002')
        self.solution = None
        self.phase = 1
        self.solution = 'Enclose condition in ()\'s.'

    def analyze(self, oFile):
        lToi = oFile.get_if_statement_conditions()

        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if not isinstance(lTokens[0], parser.open_parenthesis):
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
            lTokens.insert(0, parser.open_parenthesis())
            lTokens.append(parser.close_parenthesis())

            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)
