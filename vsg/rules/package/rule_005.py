
from vsg import rule

import re


class rule_005(rule.rule):
    '''
    Package rule 005 checks if the "is" keyword is on the same line as the "package" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'package'
        self.identifier = '005'
        self.solution = 'Ensure "is" keyword is on the same line as the "package" keyword.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPackageKeyword:
                lLine = oLine.lineLower.split()
                if len(lLine) < 3:
                    self.add_violation(iLineNumber)
                elif not lLine[2] == "is":
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'^(\s*package\s+\w+)', r'\1 is', oLine.line, re.IGNORECASE))
            # Search for "is" on the next line
            iSearchIndex = iLineNumber
            while True:
                iSearchIndex += 1
                oLine = oFile.lines[iSearchIndex]
                if re.match('^\s*is', oLine.line, re.IGNORECASE):
                    oLine.update_line(re.sub(r'^(\s*)is', r'\1  ', oLine.line))
                    if re.match('^\s*$', oLine.line):
                        oLine.update_line('')
                        oLine.isBlank = True
                        break
                if not oLine.isBlank:
                    break
