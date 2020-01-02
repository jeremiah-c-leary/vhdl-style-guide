
from vsg import rule
from vsg import fix
from vsg import check

import re


class rule_012(rule.rule):
    '''
    Component rule 012 checks component name is uppercase in "end" keyword line.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'component'
        self.identifier = '012'
        self.solution = None
        self.case = 'upper'
        self.phase = 6
        self.configuration.append('case')

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isComponentEnd and re.match('^\s*end\s+component\s+\w+', oLine.line, re.IGNORECASE):
            lLine = oLine.line.split()
            if self.case == 'upper':
                check.is_uppercase(self, lLine[2], iLineNumber)
            else:
                check.is_lowercase(self, lLine[2], iLineNumber)
            self.dFix[iLineNumber] = 2

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            iIndex = self.dFix[iLineNumber]
            if self.case == 'upper':
                fix.upper_case(oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[iIndex])
            else:
                fix.lower_case(oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[iIndex])

    def _get_solution(self, iLineNumber):
        if self.case == 'upper':
            return 'Uppercase component name.'
        else:
            return 'Lowercase component name.'
