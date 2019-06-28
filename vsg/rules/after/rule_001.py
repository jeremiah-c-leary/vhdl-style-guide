
import re

from vsg import rule
from vsg import utils


class rule_001(rule.rule):
    '''
    After rule 001 checks for the "after" keyword in signal assignments in clock processes.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'after', '001')
        self.fixable = False
        self.phase = 1

    def _pre_analyze(self):
        self.sequentialStatement = ""

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.insideClockProcess:
            if oLine.isSequentialEnd:
                self.sequentialStatement += oLine.lineNoComment.replace('--', '  ')
                print(self.sequentialStatement)
                if not re.match('^\s*.*\safter\s', self.sequentialStatement):
                    self.add_violation(iLineNumber) 
                self.sequentialStatement = ""
            elif oLine.insideSequential:
                self.sequentialStatement += oLine.lineNoComment.replace('--', '  ')
            elif oLine.isSequential:
                self.sequentialStatement = oLine.lineNoComment.replace('--', '  ')
