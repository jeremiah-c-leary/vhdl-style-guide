

from vsg import rule
from vsg import parser
from vsg import violation


class split_line_at_token_when_between_tokens(rule.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of parser object types
       object type to split a line at

    oStart : token type
       The start of the range

    oEnd : token type
       The end of the range
    '''

    def __init__(self, name, identifier, lTokens, oStart, oEnd):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.lTokens = lTokens
        self.oStart = oStart
        self.oEnd = oEnd

    def analyze(self, oFile):
        lToi = oFile.get_token_and_n_tokens_before_it_in_between_tokens(self.lTokens, 2, self.oStart, self.oEnd)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if isinstance(lTokens[0], parser.carriage_return) or isinstance(lTokens[1], parser.carriage_return):
                continue
            sSolution = self.solution
            oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
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
            if isinstance(lTokens[1], parser.whitespace):
                lTokens.insert(-2, parser.carriage_return())
            else:
                lTokens.insert(-1, parser.carriage_return())
            oViolation.set_tokens(lTokens)
               
        oFile.update(self.violations)

