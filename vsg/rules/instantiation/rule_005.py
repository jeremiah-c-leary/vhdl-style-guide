
from vsg import rule

import copy


class rule_005(rule.rule):
    '''
    Instantiation rule 005 checks the instantiation declaration and
    "port map" keywords are not on the same line.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '005'
        self.solution = 'Place "port map" keywords on the next line by itself'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationDeclaration and oLine.isInstantiationPortKeyword:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oLine = oFile.lines[iLineNumber]
            iIndex = oLine.lineLower.find(' port ')
            oFile.lines.insert(iLineNumber + 1, copy.deepcopy(oLine))
            oLine.update_line(oLine.line[:iIndex])
            oLine.isInstantiationPortKeyword = False
            oLine.isInstantiationPortEnd = False
            oLine = oFile.lines[iLineNumber + 1]
            oLine.update_line(oLine.line[iIndex:])
            oLine.isInstantiationDeclaration = False
            oLine.indentLevel += 1
