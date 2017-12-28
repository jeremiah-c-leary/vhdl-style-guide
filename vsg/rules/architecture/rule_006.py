
from vsg import rule
from vsg import utilities

import re


class rule_006(rule.rule):
    '''
    Architecture rule 006 checks if the "is" keyword is on the same line as the "architecture" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'architecture', '006')
        self.solution = 'Ensure "is" keyword is on the same line as the "architecture" keyword.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isArchitectureKeyword and \
               re.match('^\s*architecture\s+\w+\s+of\s+\w+', oLine.line, re.IGNORECASE) and \
               not re.match('^\s*architecture\s+\w+\s+of\s+\w+\s+is', oLine.line, re.IGNORECASE):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub(r'^(\s*architecture\s+\w+\s+of\s+\w+)', r'\1 is', oLine.line, re.IGNORECASE))
            utilities.search_for_and_remove_keyword(oFile, iLineNumber, 'is')
