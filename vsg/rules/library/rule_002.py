
from vsg.rules.library import library_rule

import re


class rule_002(library_rule):
    '''
    Library rule 002 checks for a single space after the library keyword.
    '''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '002'
        self.solution = 'Remove extra spaces after "library" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isLibrary:
                if re.match('^\s*\S+\s\s+', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.line = re.sub(r'^(\s*library)\s+', r'\1 ', oLine.line, flags=re.IGNORECASE)
            oLine.lineLower = oLine.line.lower()
