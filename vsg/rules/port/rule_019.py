
from vsg import rule
from vsg import fix
from vsg import check


class rule_019(rule.rule):
    '''
    Port rule 019 checks the port direction is lowercase.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'port', '019')
        self.solution = 'Change port direction to lowercase.'
        self.phase = 6

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isPortDeclaration:
            sLine = oLine.line.split(':')[1]
            check.is_lowercase(self, sLine.split()[0], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            sLine = oFile.lines[iLineNumber].line.split(':')[1]
            fix.lower_case(oFile.lines[iLineNumber], sLine.split()[0])
