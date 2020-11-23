
from vsg import parser
from vsg import rule
from vsg import violation

from vsg.vhdlFile import utils


class rule_012(rule.Rule):
    '''
    Checks for consecutive blank lines.

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
        rule.Rule.__init__(self, 'whitespace', '012')
        self.solution = None
        self.phase = 3
        self.subphase = 3
        self.numBlankLines = 1
        self.configuration.append('numBlankLines')

    def analyze(self, oFile):
        oToi = oFile.get_all_tokens()
        iLine, lTokens = utils.get_toi_parameters(oToi)
        iCount = 0
        for iToken, oToken in enumerate(lTokens[:len(lTokens) - 1]):
            iLine = utils.increment_line_number(iLine, oToken)

            if isinstance(oToken, parser.blank_line):
                if iCount == 0:
                    iLineNumber = iLine
                    iStartToken = iToken
                iCount += 1

            if isinstance(oToken, parser.carriage_return):
                if not isinstance(lTokens[iToken + 1], parser.blank_line):
                    if iCount > self.numBlankLines:
                        sSolution = 'Remove ' + str(iCount - self.numBlankLines) + ' blank line(s) below'
                        lExtractedTokens = oToi.extract_tokens(iStartToken, iToken)
                        oViolation = violation.New(iLineNumber, lExtractedTokens, sSolution)
                        dAction = {}
                        dAction['remove'] = iCount - self.numBlankLines
                        oViolation.set_action(dAction)
                        self.add_violation(oViolation)
     
                    iCount = 0

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
            dAction = oViolation.get_action()
            lTokens = lTokens[2*dAction['remove']:]
            oViolation.set_tokens(lTokens)
               
        oFile.update(self.violations)
