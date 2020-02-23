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
        self.fProcessHadBeginLabel = False

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isProcessKeyword:
            if oLine.isProcessLabel:
                self.previousLabel = utils.extract_label(oLine)[0]
                self.fProcessHadBeginLabel = True
        if oLine.isEndProcess:
            if not oLine.isProcessEndLabel:
                dViolation = utils.create_violation_dict(iLineNumber)
                if self.fProcessHadBeginLabel:
                    dViolation['processLabel'] = self.previousLabel
                self.add_violation(dViolation)
            self.fProcessHadBeginLabel = False

    def _fix_violations(self, oFile):
         for dViolation in self.violations:
             try:
                 oLine = oFile.lines[dViolation['lineNumber']]
                 sLine = oLine.line
                 iIndex = oLine.lineLower.find('process') + len('process')
                 oLine.update_line(sLine[:iIndex] + ' ' + dViolation['processLabel'] + sLine[iIndex:])
                 oLine.isProcessEndLabel = True
             except KeyError:
                 pass
