
from vsg.rules.case import case_rule
import re


class rule_012(case_rule):
    '''Case rule 012 ensures code does not exist after the => operator.'''

    def __init__(self):
        case_rule.__init__(self)
        self.identifier = '012'
        self.solution = 'Move code after the => operator to it\'s own line.'
        self.phase = 1

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isCaseWhenEnd:
                if re.match('^.*=>\s*\w', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            self._split_line_after_word(oFile, iLineNumber, '=>')
            oFile.lines[iLineNumber + 1].isCaseWhenEnd = False
            oFile.lines[iLineNumber + 1].indentLevel += 1
