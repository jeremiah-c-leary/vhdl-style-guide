
from vsg import rule
from vsg import check


class rule_004(rule.rule):
    '''
    Concurrent rule 004 checks there is at least a single space before the assignment.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'concurrent'
        self.identifier = '004'
        self.solution = 'Add a single space before the <=.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isConcurrentBegin:
                check.is_single_space_before_character(self, '<=', oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(oLine.line.replace('<=', ' <='))
