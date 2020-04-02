
from vsg import rule
from vsg import utils

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
        dSignals = {}
        for iLineNumber, oLine in enumerate(oFile.lines):
            if self._is_vsg_off(oLine):
                continue
            if oLine.isSignal and re.match('^\s*signal\s+\S+,\s*\S+\s*:', oLine.line, flags=re.IGNORECASE):
                dSignals[iLineNumber] = {}
                dSignals[iLineNumber]['comma'] = 0
                for iIndex, sChar in enumerate(oLine.line):
                    if dSignals[iLineNumber]['comma'] > 0 and not sChar == ' ':
                        iMaxSignalIndex = max(iMaxSignalIndex, iIndex + 1)
                        dSignals[iLineNumber]['signal'] = iIndex + 1
                        break
                    if sChar == ',':
                        dSignals[iLineNumber]['comma'] = iIndex + 1
                        lIndexes.append(iLineNumber)
            if oLine.isArchitectureBegin:
                for iIndex in lIndexes:
                    dSignals[iIndex]['max'] = iMaxSignalIndex
                    if iMaxSignalIndex > dSignals[iIndex]['signal']:
                        dViolation = utils.create_violation_dict(iIndex)
                        dViolation['comma'] = dSignals[iIndex]['comma']
                        dViolation['signal'] = dSignals[iIndex]['signal']
                        dViolation['max'] = dSignals[iIndex]['max']
                        self.add_violation(dViolation)
                lIndexes = []

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            oLine = utils.get_violating_line(oFile, dViolation)
            iComma = dViolation['comma']
            iAddNumSpaces = dViolation['max'] - dViolation['signal']
            oLine.update_line(oLine.line[:iComma] + iAddNumSpaces*' ' + oLine.line[iComma:])
