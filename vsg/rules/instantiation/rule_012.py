
from vsg import rule
from vsg import utils

import copy


class rule_012(rule.rule):
    '''
    Instantiation rule 012 checks the instantiation declaration and
    "generic map" keywords are not on the same line.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '012'
        self.solution = 'Place "generic map" keywords on the next line by \
                         itself'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isInstantiationDeclaration and oLine.isInstantiationGenericKeyword:
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            iLineNumber = utils.get_violation_linenumber(dViolation)
            oLine = oFile.lines[iLineNumber]
            iIndex = oLine.lineLower.find(' generic ')
            oFile.lines.insert(iLineNumber + 1, copy.deepcopy(oLine))
            oLine.update_line(oLine.line[:iIndex])
            oLine.isInstantiationGenericKeyword = False
            oLine = oFile.lines[iLineNumber + 1]
            oLine.update_line(oLine.line[iIndex:])
            oLine.isInstantiationDeclaration = False
            oLine.indentLevel += 1
