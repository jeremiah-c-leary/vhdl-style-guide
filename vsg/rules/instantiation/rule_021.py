
from vsg import rule
from vsg import utils

import itertools
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
            if len(utils.extract_port_assignments(oLine)) > 1:
                dViolation = utils.create_violation_dict(iLineNumber)
                self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            iLineNumber = utils.get_violation_line_number(dViolation)
            oLine = oFile.lines[iLineNumber]
            lPorts = utils.extract_port_assignments(oLine)
            iNumberOfPorts = len(lPorts)
            # Replicate ports ###
            for iIndex in range(1, iNumberOfPorts):
                oFile.lines.insert(iLineNumber, copy.deepcopy(oLine))
            # Split ports
            for iIndex in range(0, iNumberOfPorts):
                oLine = oFile.lines[iLineNumber + iIndex]
                if iIndex == 0:
                    oLine.update_line(utils.extract_string_before_string(oLine.line, lPorts[iIndex]) + lPorts[iIndex] + ',')
                    oLine.isInstantiationPortEnd = False
                elif iIndex + 1 == iNumberOfPorts and oFile.lines[iLineNumber + iIndex + 1].isInstantiationPortEnd:
                    oLine.update_line(lPorts[iIndex])
                    oLine.isInstantiationPortEnd = False
                elif iIndex + 1 == iNumberOfPorts and oFile.lines[iLineNumber + iIndex].isInstantiationPortEnd:
                    sTemp = utils.extract_string_after_string(oLine.line, lPorts[iIndex])
                    oLine.update_line(lPorts[iIndex] + sTemp)
                else:
                    oLine.update_line(lPorts[iIndex] + ',')
                    oLine.isInstantiationPortEnd = False
