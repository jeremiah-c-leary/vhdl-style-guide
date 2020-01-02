
import re

from vsg import rule
from vsg import fix
from vsg import check


class rule_011(rule.rule):
    '''
    Architecture rule 011 checks the architecture name case on the closing "end architecture" line.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'architecture', '011')
        self.solution = 'Uppercase architecture name.'
        self.case = 'upper'
        self.phase = 6
        self.configuration.append('case')

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isEndArchitecture and re.match('^\s*end\s+architecture\s+\w+', oLine.line, re.IGNORECASE):
            lLine = oLine.line.split()
            if self.case == 'upper':
                check.is_uppercase(self, lLine[2], iLineNumber)
            else:
                check.is_lowercase(self, lLine[2], iLineNumber)
            self.dFix[iLineNumber] = 2
        elif oLine.isEndArchitecture and re.match('^\s*end\s+\w+', oLine.line, re.IGNORECASE):
            lLine = oLine.line.split()
            self.dFix[iLineNumber] = 2
            if not lLine[1].lower().startswith('architecture'):
                self.dFix[iLineNumber] = 1
                if self.case == 'upper':
                    check.is_uppercase(self, lLine[1], iLineNumber)
                else:
                    check.is_lowercase(self, lLine[1], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            iIndex = self.dFix[iLineNumber]
            if self.case == 'upper':
                fix.upper_case(oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[iIndex])
            else:
                fix.lower_case(oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[iIndex])

    def _get_solution(self, iLineNumber):
        if self.case == 'upper':
            return 'Uppercase architecture name.'
        else:
            return 'Lowercase architecture name.'
