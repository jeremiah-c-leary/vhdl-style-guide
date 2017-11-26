
from vsg.rules.component import component_rule
from vsg import check


class rule_009(component_rule):
    '''Component rule 009 checks for spaces before the "end" keyword.'''

    def __init__(self):
        component_rule.__init__(self)
        self.identifier = '009'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComponentEnd:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._fix_indent(oFile.lines[iLineNumber])
