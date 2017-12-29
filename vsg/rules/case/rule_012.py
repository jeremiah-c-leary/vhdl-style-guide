
from vsg import rule
from vsg import utilities
import re


class rule_012(rule.rule):
    '''
    Case rule 012 ensures code does not exist after the => operator.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'case', '012')
        self.solution = 'Move code after the => operator to it\'s own line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseWhenEnd and re.match('^.*=>\s*\w', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            utilities.split_line_after_word(oFile, iLineNumber, '=>')
            oFile.lines[iLineNumber + 1].isCaseWhenEnd = False
            oFile.lines[iLineNumber + 1].insideCaseWhen = False
            oFile.lines[iLineNumber + 1].indentLevel += 1
            utilities.reclassify_line(oFile, iLineNumber)
