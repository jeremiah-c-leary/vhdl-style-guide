from vsg import rule
from vsg import utils

import re


class rule_018(rule.rule):
    '''
    Process rule 018 checks the "end process" has a label.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'process', '018')
        self.solution = 'Add a label for the "end process".'
        self.phase = 1
        self.subphase = 2

    def _pre_analyze(self):
        self.previousLabel = ''
        self.iProcStartLine = 0
        self.iProcLabelLine = 0

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isProcessKeyword:
            self.iProcStartLine = iLineNumber
            oMatch = re.match('^\s*\S+\s*:\s*process', oLine.lineLower)
            if oMatch:
                self.iProcLabelLine = iLineNumber
                self.previousLabel = utils.extract_label(oLine)[0]
        if oLine.isEndProcess:
            dViolation = prepare_violation_dict(iLineNumber)
            update_process_label(self, dViolation)
            if not re.match('^\s*\S+\s+\S+\s+\S+', oLine.line):
                self.add_violation(dViolation)
            self.previousLabel = ''

    def _fix_violations(self, oFile):
         for dViolation in self.violations:
             try:
                 oLine = oFile.lines[dViolation['lineNumber']]
                 sLine = oLine.line
                 iIndex = oLine.lineLower.find('process') + len('process')
                 oLine.update_line(sLine[:iIndex] + ' ' + dViolation['processLabel'] + sLine[iIndex:])
             except KeyError:
                 pass


def prepare_violation_dict(iLineNumber):
    dReturn = {}
    dReturn['lineNumber'] = iLineNumber
    return dReturn


def update_process_label(self, dViolation):
    if self.previousLabel and self.iProcStartLine == self.iProcLabelLine:
        dViolation['processLabel'] = self.previousLabel
