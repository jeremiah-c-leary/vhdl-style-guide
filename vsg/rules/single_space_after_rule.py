
from vsg import rule
from vsg import check
from vsg import fix


class single_space_after_rule(rule.rule):
    '''
    Single space after rule checks for a single space after a user specified keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.phase = 2
        self.sTrigger = None
        self.sWord = None
        self.identifier = None
        self.solution = None

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.__dict__[self.sTrigger]:
                check.is_single_space_after(self, self.sWord, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            fix.enforce_one_space_after_word(self, oLine, self.sWord)
