
from vsg import rule

import re


class rule_033(rule.rule):
    '''
    Instantiation rule 033 checks for the component keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '033'
        self.solution = 'Remove component keyword'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isInstantiationDeclaration and not oLine.isDirectInstantiationDeclaration:
            if re.match('^\s*\w+\s*:\s*component', oLine.line, flags=re.IGNORECASE):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            sLine = oFile.lines[iLineNumber].line
            sLine = re.sub(r'(^\s*\w+\s*:)(\s*)component(\s+)', r'\1 ', sLine, flags=re.IGNORECASE)
            oFile.lines[iLineNumber].update_line(sLine)
