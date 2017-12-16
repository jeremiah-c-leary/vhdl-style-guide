
from vsg import rule
from vsg import check
from vsg import fix


class single_space_before_rule(rule.rule):
    '''
    Single space before rule checks for a single space before a user specified keyword.
    '''

    def __init__(self, name=None, identifier=None, sTrigger=None, sWord=None):
        rule.rule.__init__(self, name=name, identifier=identifier)
        self.phase = 2
        self.sTrigger = sTrigger
        self.sWord = sWord
        self.solution = None

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.__dict__[self.sTrigger]:
                check.is_single_space_before(self, self.sWord, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            fix.enforce_one_space_before_word(self, oLine, self.sWord)
