

from vsg import parser
from vsg import rule
from vsg import violation

from vsg.vhdlFile import utils


class whitespace_before_token(rule.Rule):
    '''
    Checks for a at least a single space before a token.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    token : token object
       reference token check for a whitespace before
    '''

    def __init__(self, name, identifier, lTokens):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 2
        self.lTokens = lTokens

    def analyze(self, oFile):

        self._print_debug_message('Analyzing rule: ' + self.name + '_' + self.identifier)
        dAnalysis = {}
        lToi = []
        for oToken in self.lTokens:
            lToi_a = oFile.get_token_and_n_tokens_before_it(oToken, 1)
            lToi = utils.combine_two_token_class_lists(lToi, lToi_a)
 
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLine = oToi.get_line_number()

            if isinstance(lTokens[0], parser.whitespace):
                continue

            if isinstance(lTokens[0], parser.carriage_return):
                continue

            oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
            self.violations.append(oViolation)


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
            lTokens.insert(1, parser.whitespace(' '))
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)

