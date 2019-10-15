
from vsg import rule

import re


class rule_011(rule.rule):
    '''
    Generate rule 011 checks the "end generate" has a label.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'generate', '011')
        self.solution = 'Add a label for the "end generate".'
        self.phase = 1

    def _pre_analyze(self):
        self.sGenerateName = ''

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isGenerateLabel:
           self.sGenerateName = oLine.line.lstrip().split(':')[0]
        if oLine.isGenerateEnd and not re.match('^\s*\S+\s+\S+\s+\S+', oLine.line):
            self.add_violation(iLineNumber)
            self.dFix['violations'][iLineNumber] = self.sGenerateName

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            sLine = oLine.line
            iIndex = oLine.lineLower.find('generate') + len('generate')
            oLine.update_line(sLine[:iIndex] + ' ' + self.dFix['violations'][iLineNumber] + sLine[iIndex:])
