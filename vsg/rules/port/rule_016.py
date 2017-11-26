
from vsg.rules.port import port_rule

import re
import copy


class rule_016(port_rule):
    '''
    Port rule 016 checks for a port definition on the same line as the port keyword.
    '''

    def __init__(self):
        port_rule.__init__(self)
        self.identifier = '016'
        self.solution = 'Move port definition to it\'s own line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortKeyword:
                if re.match('^\s*port\s*\(\s*\S+\s*:', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oFile.lines.insert(iLineNumber + 1, copy.deepcopy(oFile.lines[iLineNumber]))
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(oLine.line.split('(')[0] + ' (')
            oLine = oFile.lines[iLineNumber + 1]
            oLine.update_line('  ' + oLine.line.split('(')[1])
            oLine.isPortKeyword = False
            oLine.isPortDeclaration = True
            oLine.insidePortMap = True
            oLine.indentLevel = oFile.lines[iLineNumber].indentLevel + 1
