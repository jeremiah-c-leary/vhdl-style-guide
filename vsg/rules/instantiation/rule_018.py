
from vsg import rule
from vsg import check
from vsg import fix


class rule_018(rule.rule):
    '''
    Instantiation rule 018 checks for a single space between map and (
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '018'
        self.solution = 'Ensure a single space exists between "map" and (.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationGenericKeyword or oLine.isInstantiationPortKeyword:
                check.is_single_space_after(self, 'map', oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.enforce_one_space_after_word(self, oFile.lines[iLineNumber], 'map')
