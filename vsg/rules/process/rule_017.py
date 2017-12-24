
from vsg import rule
from vsg import check
from vsg import fix


class rule_017(rule.rule):
    '''
    Process rule 017 checks the process label is uppercase.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'process', '017')
        self.solution = 'Uppercase process label.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessLabel:
                lLine = oLine.line.split(':')
                check.is_uppercase(self, lLine[0], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            lLine = oFile.lines[iLineNumber].line.split(':')
            fix.upper_case(self, oFile.lines[iLineNumber], lLine[0].rstrip().lstrip())
