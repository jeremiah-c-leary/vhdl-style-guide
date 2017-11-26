
from vsg.rules.type import type_rule

import re
import copy


class rule_009(type_rule):
    '''
    Type rule 009 checks for enumerated types after the open parenthesis on a multi-line type declaration.
    '''

    def __init__(self):
        type_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Move enumerated type to it\'s own line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isTypeKeyword and not oLine.isTypeEnd:
                if re.match('^.*\sis\s*\(\w', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oFile.lines.insert(iLineNumber + 1, copy.deepcopy(oFile.lines[iLineNumber]))
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(oLine.line.split('(')[0] + ' (')
            oLine = oFile.lines[iLineNumber + 1]
            oLine.update_line('  ' + oLine.line.split('(')[1])
            oLine.isTypeKeyword = False
            oLine.indentLevel += 1
