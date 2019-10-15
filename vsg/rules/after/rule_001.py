
import re

from vsg import rule


class rule_001(rule.rule):
    '''
    After rule 001 checks for the "after" keyword in signal assignments in clock processes.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'after', '001')
        self.phase = 1
        self.disable = True
        self.magnitude = 1
        self.units = 'ns'
        self.configuration.extend(['magnitude', 'units'])
        self.solution = 'Add after ' + str(self.magnitude) + ' ' + self.units + ' to signal in clock process'

    def _pre_analyze(self):
        self.sequentialStatement = ""

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.insideClockProcess:
            if oLine.isSequentialEnd:
                self.sequentialStatement += oLine.lineNoComment.replace('--', '  ')
                if not re.match('^\s*.*\safter\s', self.sequentialStatement):
                    self.add_violation(iLineNumber)
                self.sequentialStatement = ""
            elif oLine.insideSequential:
                self.sequentialStatement += oLine.lineNoComment.replace('--', '  ')
            elif oLine.isSequential:
                self.sequentialStatement = oLine.lineNoComment.replace('--', '  ')

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            sLine = oLine.line
            sNewLine = sLine.replace(';', ' ' + ' '.join(['after', str(self.magnitude), self.units]) + ';')
            oLine.update_line(sNewLine)
