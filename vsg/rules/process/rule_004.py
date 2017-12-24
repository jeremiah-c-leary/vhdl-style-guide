
from vsg import rule
from vsg import utilities
from vsg import fix
from vsg import check


class rule_004(rule.rule):
    '''
    Process rule 004 checks the "begin" keyword is lower case.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'process'
        self.identifier = '004'
        self.solution = 'Lowercase the "begin" keyword.'
        self.phase = 6

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessBegin:
                check.is_lowercase(self, utilities.get_first_word(oLine), iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(self, oFile.lines[iLineNumber], 'begin')
