
from vsg import rule
from vsg import utils

import re
import copy


class rule_021(rule.rule):
    '''
    Instantiation rule 021 checks multiple port assignments on the same line.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '021'
        self.solution = 'Move multiple port assignments to their own lines.'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isInstantiationPortAssignment:
            if re.match('^\s*\S+\s*=>\s*.*\s*,\s*\S+\s*=>', oLine.line):
                sTemp = re.match('(^\s*\S+\s*=>\s*.*\s*),\s*\S+\s*=>', oLine.line).group(0)
                if sTemp.count('(') == sTemp.count(')'):
                    dViolation = utils.create_violation_dict(iLineNumber)
                    self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            iLineNumber = dViolation['lineNumber']
            oLine = oFile.lines[iLineNumber]
            iNumberOfPorts = oLine.line.count(',')
            # Replicate ports ###
            for iIndex in range(1, iNumberOfPorts):
                oFile.lines.insert(iLineNumber, copy.deepcopy(oLine))
            # Split ports
            for iIndex in range(0, iNumberOfPorts):
                oLine = oFile.lines[iLineNumber + iIndex]
                lPorts = oLine.line.split(',')
                if iIndex == iNumberOfPorts - 1 and oFile.lines[iLineNumber + iIndex + 1].isInstantiationPortEnd:
                    oLine.update_line(lPorts[iIndex])
                else:
                    oLine.update_line(lPorts[iIndex] + ',')
