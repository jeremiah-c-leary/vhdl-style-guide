

from vsg import parser
from vsg import rule_item
from vsg import violation

from vsg.vhdlFile import utils


class whitespace_before_tokens_in_between_tokens(rule_item.Rule):
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

    oStart : token object type
       The beginning of the range

    oEnd : token object type
       The end of the range
    '''

    def __init__(self, name, identifier, lTokens, oStart, oEnd):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 2
        self.lTokens = lTokens
        self.oStart = oStart
        self.oEnd = oEnd

    def analyze(self, oFile):

        dAnalysis = {}

        lToi = oFile.get_token_and_n_tokens_before_it_in_between_tokens(self.lTokens, 1, self.oStart, self.oEnd)
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

