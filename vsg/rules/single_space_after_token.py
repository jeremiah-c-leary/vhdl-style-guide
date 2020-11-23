

from vsg import parser
from vsg import rule
from vsg import violation

from vsg.vhdlFile import utils


class single_space_after_token(rule.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : token type object list
       A list of tokens to check for a single space after.
    '''

    def __init__(self, name, identifier, lTokens):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 2
        self.lTokens = lTokens

    def analyze(self, oFile):
        lToi = oFile.get_token_and_n_tokens_after_it(self.lTokens, 1)

        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if not isinstance(lTokens[1], parser.whitespace):
                oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
                oViolation.set_action('insert')
                self.add_violation(oViolation)
            else:
                if lTokens[1].get_value() != ' ':
                    oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
                    oViolation.set_action('adjust')
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
            sAction = oViolation.get_action()
            if sAction == 'insert':
                lTokens.insert(1, parser.whitespace(' '))
            elif sAction == 'adjust':
                lTokens[1].set_value(' ')
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)


