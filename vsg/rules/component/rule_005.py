
from vsg import rule
from vsg import fix

import re


class rule_005(rule.rule):
    '''Component rule 005 checks the "is" keyword is on the same line as the component keyword.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'component'
        self.identifier = '005'
        self.solution = 'Add "is" keyword to same line as "component" keyword.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentDeclaration and not re.match('^\s*component\s+\w+\s+is', oLine.line, re.IGNORECASE):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'^(\s*component\s+\w+)', r'\1 is', oLine.lineLower, re.IGNORECASE))
            # Search for "is" on the next line
            fix.replace_is_keyword(oFile, iLineNumber)
