
from vsg import fix
from vsg import check
from vsg import rule


class line_below_rule(rule.rule):

    def __init__(self):
        rule.rule.__init__(self)
        self.solution = 'Insert blank line below.'
        self.phase = 3

    def analyze(self, oFile):
        lFailureLines = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.__dict__[self.condition]:
                check.is_blank_line_after(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            fix.insert_blank_line_below(self, oFile, iLineNumber)
