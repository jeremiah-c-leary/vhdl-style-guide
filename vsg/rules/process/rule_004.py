
from vsg.rules.process import process_rule


class rule_004(process_rule):
    '''
    Process rule 004 checks the "begin" keyword is lower case.
    '''

    def __init__(self):
        process_rule.__init__(self)
        self.identifier = '004'
        self.solution = 'Lowercase the "begin" keyword.' 
        self.phase = 6

    def analyze(self, oFile):
        fInsideProcess = False
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isProcessBegin:
                self._is_lowercase(self._get_first_word(oLine), iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._lower_case(oFile.lines[iLineNumber], 'begin')
