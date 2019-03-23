
from vsg import rule
from vsg import utils
import re


class rule_012(rule.rule):
    '''
    Case rule 012 ensures code does not exist after the => operator.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'case', '012')
        self.solution = 'Move code after the => operator to it\'s own line.'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isCaseWhenEnd and re.match('^.*=>\s*\w', oLine.line):
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            utils.split_line_after_word(oFile, iLineNumber, '=>')
            oFile.lines[iLineNumber + 1].isCaseWhenEnd = False
            oFile.lines[iLineNumber + 1].insideCaseWhen = False
            oFile.lines[iLineNumber + 1].indentLevel += 1
            utils.reclassify_line(oFile, iLineNumber)
