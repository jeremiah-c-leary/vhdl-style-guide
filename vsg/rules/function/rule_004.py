
from vsg.rules.function import function_rule
from vsg import utilities
from vsg import fix
from vsg import check


class rule_004(function_rule):
    '''
    Function rule 004 checks the "begin" keyword is lower case.
    '''

    def __init__(self):
        function_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Lowercase the "begin" keyword.'
        self.phase = 6

    def analyze(self, oFile):
        fInsideFunction = False
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isFunctionBegin:
                check.is_lowercase(self, utilities.get_first_word(oLine), iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.lower_case(self, oFile.lines[iLineNumber], 'begin')
