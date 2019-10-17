
from vsg import rule
from vsg import utils
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

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isProcessBegin:
            check.is_lowercase(self, utils.get_first_word(oLine), iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(oFile.lines[iLineNumber], 'begin')
