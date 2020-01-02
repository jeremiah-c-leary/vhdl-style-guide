
from vsg import rule
from vsg import check

import re


class architecture_case_rule(rule.rule):
    '''
    Architecture rule 013 checks the architecture name is upper case in the architecture declaration.
    '''

    def __init__(self, name=None, identifier=None, iIndex=None):
        rule.rule.__init__(self, name, identifier)
        self.case = 'upper'
        self.phase = 6
        self.configuration.append('case')
        self.iIndex = iIndex

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isArchitectureKeyword and re.match('^\s*\S+\s\s*\S+\s\s*of\s\s*\S+\s\s*is', oLine.lineLower):
            lLine = oLine.line.split()
            if self.case == 'upper':
                check.is_uppercase(self, lLine[self.iIndex], iLineNumber)
            else:
                check.is_lowercase(self, lLine[self.iIndex], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            sLine = oLine.lineNoComment
            if self.case == 'upper':
                sWord = sLine.split()[self.iIndex].upper()
            else:
                sWord = sLine.split()[self.iIndex].lower()
            iIndex = sLine.rfind(sLine.split()[self.iIndex])
            sLine = sLine[:iIndex] + sWord + sLine[iIndex + len(sWord):]
            oLine.update_line(sLine)

    def _get_solution(self, iLineNumber):
        return self.case + 'case ' + self.solution
