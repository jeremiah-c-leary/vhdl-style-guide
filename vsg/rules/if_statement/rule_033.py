
from vsg import rule
from vsg import check
from vsg import utils
from vsg import fix


class rule_033(rule.rule):
    '''
    If rule 033 checks consecutive comment lines above an "else" keyword
    in an if statement are aligned with the "else" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'if'
        self.identifier = '033'
        self.solution = 'Align comment with "else" keyword.'
        self.phase = 4

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isElseKeyword:
            check.indent_of_comments_above(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            iLineNumber = utils.get_violation_line_number(dViolation)
            oFile.lines[iLineNumber].indentLevel = dViolation['indent']
            fix.indent(self, oFile.lines[iLineNumber])
