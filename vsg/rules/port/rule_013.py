
from vsg import rule
from vsg import utils

import re
import copy


class rule_013(rule.rule):
    '''
    Port rule 013 checks for multiple ports declared on single line.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'port', '013')
        self.solution = 'Place multiple ports on their own lines.'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isPortDeclaration and re.match('^.*,.*:', oLine.lineNoComment):
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            iLineNumber = dViolation['lineNumber']
            oLine = oFile.lines[iLineNumber]
            iNumberOfPorts = oLine.line.split(':')[0].count(',') + 1
            # Replicate ports
            for iIndex in range(1, iNumberOfPorts):
                oFile.lines.insert(iLineNumber, copy.deepcopy(oLine))
            # Split ports
            for iIndex in range(0, iNumberOfPorts):
                oLine = oFile.lines[iLineNumber + iIndex]
                lLine = oLine.line.split(':')
                lPorts = lLine[0].split(',')
                oLine.update_line(lPorts[iIndex] + ' :' + lLine[1])
