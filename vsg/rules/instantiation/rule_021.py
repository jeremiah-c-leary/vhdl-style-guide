
from vsg import rule

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

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationPortAssignment:
                if re.match('^\s*\S+\s*=>\s*.*\s*,\s*\S+\s*=>', oLine.line):
                    sTemp = re.match('(^\s*\S+\s*=>\s*.*\s*),\s*\S+\s*=>', oLine.line).group(0)
                    if sTemp.count('(') == sTemp.count(')'):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
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
