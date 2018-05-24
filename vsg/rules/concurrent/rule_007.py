
from vsg import rule

import re
import copy


class rule_007(rule.rule):
    '''
    Concurrent rule 007 checks for code after the "else" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'concurrent'
        self.identifier = '007'
        self.solution = 'Move code after "else" to the next line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.insideConcurrent and re.match('^.*\selse\s+[\w|\']', oLine.lineNoComment.lower()):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oLine = oFile.lines[iLineNumber]
            iIndex = oLine.line.find(' else') + len(' else')
            oFile.lines.insert(iLineNumber + 1, copy.deepcopy(oLine))
            oLine.isEndConcurrent = False
            oLine.update_line(oLine.line[:iIndex])
            oLine = oFile.lines[iLineNumber + 1]
            oLine.isConcurrentBegin = False
            oLine.update_line(oLine.line[iIndex:])
