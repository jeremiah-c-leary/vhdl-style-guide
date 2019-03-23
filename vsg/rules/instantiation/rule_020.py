
from vsg import rule
from vsg import utils


class rule_020(rule.rule):
    '''
    Instantiation rule 020 checks for a port assignment on the same line as the port map keywords.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'instantiation'
        self.identifier = '020'
        self.solution = 'Move port assignment to it\'s own line.'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isInstantiationPortAssignment and oLine.isInstantiationPortKeyword:
            self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            utils.split_line_after_word(oFile, iLineNumber, '(')
            oFile.lines[iLineNumber].isInstantiationPortAssignment = False
            oFile.lines[iLineNumber + 1].isInstantiationPortKeyword = False
            oFile.lines[iLineNumber + 1].indentLevel += 1
