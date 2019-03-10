
from vsg import rule

import re


class rule_012(rule.rule):
    '''
    Signal rule 012 checks the second signal in a signal declaration are aligned within the architecture declarative region.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'signal', '012')
        self.phase = 5
        self.solution = 'Align second signal with others.'

    def analyze(self, oFile):
        iMaxSignalIndex = 0
        lIndexes = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if self._is_vsg_off(oLine):
                continue
            if oLine.isSignal and re.match('^\s*signal\s+\S+,\s*\S+\s*:', oLine.line, flags=re.IGNORECASE):
                self.dFix[iLineNumber] = {}
                self.dFix[iLineNumber]['comma'] = 0
                for iIndex, sChar in enumerate(oLine.line):
                    if self.dFix[iLineNumber]['comma'] > 0 and not sChar == ' ':
                        iMaxSignalIndex = max(iMaxSignalIndex, iIndex + 1)
                        self.dFix[iLineNumber]['signal'] = iIndex + 1
                        break
                    if sChar == ',':
                        self.dFix[iLineNumber]['comma'] = iIndex + 1
                        lIndexes.append(iLineNumber)
            if oLine.isArchitectureBegin:
                for iIndex in lIndexes:
                    self.dFix[iIndex]['max'] = iMaxSignalIndex
                    if iMaxSignalIndex > self.dFix[iIndex]['signal']:
                        self.add_violation(iIndex)
                lIndexes = []

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            iComma = self.dFix[iLineNumber]['comma']
            iAddNumSpaces = self.dFix[iLineNumber]['max'] - self.dFix[iLineNumber]['signal']
            oLine.update_line(oLine.line[:iComma] + iAddNumSpaces*' ' + oLine.line[iComma:])
