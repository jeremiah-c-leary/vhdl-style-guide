
from vsg.rules.component import component_rule

import re


class rule_005(component_rule):
    '''Component rule 005 checks the "is" keyword is on the same line as the component keyword.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Add "is" keyword to same line as "component" keyword.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentDeclaration:
                if not re.match('^.*\s\s*is', oLine.lineLower):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.line = re.sub(r'^(\s*component\s+\w+)', r'\1 is', oLine.line, re.IGNORECASE)
            oLine.lineLower = oLine.line.lower()
            ### Search for "is" on the next line
            iSearchIndex = iLineNumber
            while True:
                iSearchIndex += 1
                oLine = oFile.lines[iSearchIndex]
                if re.match('^\s*is', oLine.line, re.IGNORECASE):
                    oLine.line = re.sub(r'^(\s*)is', r'\1  ', oLine.line)
                    oLine.lineLower = oLine.line.lower()
                    if re.match('^\s*$', oLine.line):
                        oLine.line = ''
                        oLine.lineLower = ''
                        oLine.isBlank = True
                if oFile.lines[iSearchIndex].isGenericKeyword or oFile.lines[iSearchIndex].isPortKeyword:
                    break
