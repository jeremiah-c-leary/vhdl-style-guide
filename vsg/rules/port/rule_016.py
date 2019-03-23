
from vsg import rule
from vsg import utils

import re


class rule_016(rule.rule):
    '''
    Port rule 016 checks for a port definition on the same line as the port keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'port', '016')
        self.solution = 'Move port definition to it\'s own line.'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isPortKeyword and re.match('^\s*port\s*\(\s*\S+\s*:', oLine.lineLower):
            self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            utils.copy_line(oFile, iLineNumber)
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(oLine.line.split('(')[0] + ' (')
            oLine = oFile.lines[iLineNumber + 1]
            oLine.update_line('  ' + oLine.line.split('(')[1])
            oLine.isPortKeyword = False
            oLine.isPortDeclaration = True
            oLine.insidePortMap = True
            oLine.indentLevel = oFile.lines[iLineNumber].indentLevel + 1
