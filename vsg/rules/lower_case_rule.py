
from vsg import rule
from vsg import fix
from vsg import check


class lower_case_rule(rule.rule):
    '''
    This class checks the first word in a line is lower case.
    '''

    def __init__(self, name=None, identifier=None, sTrigger=None, sWord=None):
        rule.rule.__init__(self, name, identifier)
        self.phase = 6
        self.solution = None
        self.sTrigger = sTrigger
        self.sWord = sWord

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.__dict__[self.sTrigger]:
                check.is_lowercase(self, oLine.line.split()[0], iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(self, oFile.lines[iLineNumber], self.sWord)
