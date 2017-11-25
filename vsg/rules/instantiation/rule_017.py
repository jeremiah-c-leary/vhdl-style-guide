
from vsg.rules.instantiation import instantiation_rule

import copy


class rule_017(instantiation_rule):
    '''
    Instantiation rule 016 checks for generic map keyword and generic assignment on the same line.
    '''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '017'
        self.solution = 'Move generic assignment to it\'s own line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationGenericAssignment and oLine.isInstantiationGenericKeyword:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oFile.lines.insert(iLineNumber + 1, copy.deepcopy(oFile.lines[iLineNumber]))
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(oLine.line.split('(')[0] + ' (')
            oLine.isInstantiationGenericAssignment = False
            oLine = oFile.lines[iLineNumber + 1]
            oLine.update_line('  ' + oLine.line.split('(')[1])
            oLine.isInstantiationGenericKeyword = False
