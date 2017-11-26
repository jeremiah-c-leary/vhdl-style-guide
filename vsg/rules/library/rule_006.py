
from vsg.rules.library import library_rule

import re


class rule_006(library_rule):
    '''
    Library rule 006 checks for a single space after the use keyword.
    '''

    def __init__(self):
        library_rule.__init__(self)
        self.identifier = '006'
        self.solution = 'Remove extra spaces after "use" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isLibraryUse:
                if re.match('^\s*\S+\s\s+', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.line = re.sub(r'^(\s*\S+)\s+', r'\1 ', oLine.line)
            oLine.lineLower = oLine.line.lower()
