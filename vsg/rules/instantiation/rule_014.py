
from vsg import rule
from vsg import line

import re


class rule_014(rule.rule):
    '''
    Instantiation rule 014 checks the closing ) for the generic map is on it's own line.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '014'
        self.solution = 'Place closing ) on it\'s own line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationGenericEnd and (oLine.isInstantiationGenericAssignment or oLine.isInstantiationGenericKeyword):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oFile.lines[iLineNumber].line = re.sub(r'\)(\s*)', r' \1 ', oFile.lines[iLineNumber].line)
            oFile.lines[iLineNumber].isInstantiationGenericEnd = False
            oFile.lines.insert(iLineNumber + 1, line.line('  )'))
            oFile.lines[iLineNumber + 1].isInstantiationGenericAssignement = False
            oFile.lines[iLineNumber + 1].isInstantiationGenericEnd = True
            oFile.lines[iLineNumber + 1].insideInstantiation = True
            oFile.lines[iLineNumber + 1].indentLevel = oFile.lines[iLineNumber].indentLevel - 1
