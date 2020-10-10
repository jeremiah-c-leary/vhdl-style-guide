

from vsg import parser
from vsg import rule_item
from vsg import violation

from vsg.vhdlFile import utils


class remove_token_and_whitespace_before_it(rule_item.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : token object type list
       tokens to remove

    '''

    def __init__(self, name, identifier, lTokens):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.lTokens = lTokens


    def analyze(self, oFile):

        lToi = oFile.get_token_and_n_tokens_before_it(self.lTokens[0], 1)
        for oToi in lToi:
           self.violations.append(violation.New(oToi.get_line_number(), oToi, self.solution))


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
            if isinstance(lTokens[0], parser.whitespace):
                oViolation.set_tokens([])
            else:
                oViolation.set_tokens(lTokens[1])
        oFile.update(self.violations)
