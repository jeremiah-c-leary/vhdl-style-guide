
from vsg import rule
from vsg import utils


class rule_017(rule.rule):
    '''
    Instantiation rule 016 checks for generic map keyword and generic assignment on the same line.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '017'
        self.solution = 'Move generic assignment to it\'s own line.'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isInstantiationGenericAssignment and oLine.isInstantiationGenericKeyword:
            self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            utils.copy_line(oFile, iLineNumber)
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(oLine.line.split('(')[0] + ' (')
            oLine.isInstantiationGenericAssignment = False
            oLine = oFile.lines[iLineNumber + 1]
            oLine.update_line('  ' + oLine.line.split('(')[1])
            oLine.isInstantiationGenericKeyword = False
            oLine.indentLevel += 1
