
from vsg import rule

import re


class rule_018(rule.rule):
    '''
    Process rule 018 checks the "end process" has a label.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'process', '018')
        self.solution = 'Add a label for the "end process".'
        self.phase = 1

    def _fix_violations(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndProcess and not re.match('^\s*\S+\s+\S+\s+\S+', oLine.line):
                if iLineNumber in self.dFix['processLabel']:
                    oMatch = re.search(r'^(\s*)\S+\s+\S+', oLine.line)
                    oLine.line = oMatch.group(1) + 'end process ' + self.dFix['processLabel'][iLineNumber] + ';'

    def analyze(self, oFile):
        self.dFix['processLabel'] = {}
        labelStack = ''
        for iLineNumber, oLine in enumerate(oFile.lines):
            if self._is_vsg_off(oLine):
                continue
            if oLine.isProcessKeyword:
                iProcStartLine = iLineNumber
                oMatch = re.match('^\s*(\S+)\s*:\s*process', oLine.lineLower)
                if oMatch:
                    iProcLabelLine = iLineNumber
                    labelStack = oMatch.group(1)
            if oLine.isEndProcess:
                if not re.match('^\s*\S+\s+\S+\s+\S+', oLine.line):
                    self.add_violation(iLineNumber)
                if labelStack and iProcStartLine == iProcLabelLine:
                    self.dFix['processLabel'][iLineNumber] = labelStack
                labelStack = ''
