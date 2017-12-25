
from vsg import rule
from vsg import check
from vsg import fix


class rule_008(rule.rule):
    '''
    Function rule 008 checks the indent of function parameters when they are on multiple lines.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'function', '008')
        self.solution = 'Invalid indent'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isFunctionParameter and not oLine.isFunctionKeyword:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.indent(self, oFile.lines[iLineNumber])
