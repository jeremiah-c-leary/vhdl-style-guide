
from vsg.rules.port import port_rule

import re
import copy


class rule_013(port_rule):
    '''
    Port rule 013 checks for multiple ports declared on single line.
    '''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '013'
        self.solution = 'Place multiple ports on their own lines.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                if re.match('^.*,.*:', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oLine = oFile.lines[iLineNumber]
            iNumberOfPorts = oLine.line.split(':')[0].count(',') + 1
            ### Replicate ports ###
            for iIndex in range(1, iNumberOfPorts):
                oFile.lines.insert(iLineNumber, copy.deepcopy(oLine))
            ### Split ports
            for iIndex in range(0, iNumberOfPorts):
                oLine = oFile.lines[iLineNumber + iIndex]
                sLine = oLine.line.split(':')[0]
                lPorts = sLine.split(',')
                oLine.update_line(lPorts[iIndex] + ' :' + oLine.line.split(':')[1])
            
