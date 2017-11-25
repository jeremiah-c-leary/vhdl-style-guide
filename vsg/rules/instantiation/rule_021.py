
from vsg.rules.instantiation import instantiation_rule

import re
import copy


class rule_021(instantiation_rule):
    '''
    Instantiation rule 021 checks multiple port assignments on the same line.
    '''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '021'
        self.solution = 'Move multiple port assignments to their own lines.'
        self.phase = 1

    def analyze(self, oFile):
        lFailureLines = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationPortAssignment:
                if re.match('^\s*\S+\s*=>\s*\S+,\s*\S+\s*=>', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oLine = oFile.lines[iLineNumber]
            iNumberOfPorts = oLine.line.count(',') + 1
            # Replicate ports ###
            for iIndex in range(1, iNumberOfPorts):
                oFile.lines.insert(iLineNumber, copy.deepcopy(oLine))
            # Split ports
            for iIndex in range(0, iNumberOfPorts):
                oLine = oFile.lines[iLineNumber + iIndex]
                lPorts = oLine.line.split(',')
                oLine.update_line(lPorts[iIndex] + ',')
