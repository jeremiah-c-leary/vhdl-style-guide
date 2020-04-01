
from vsg import rule
from vsg import check
from vsg import utils
from vsg import fix


class rule_032(rule.rule):
    '''
    If rule 032 checks consecutive comment lines above an "elsif" keyword
    in an if statement are aligned with the "elsif" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'if'
        self.identifier = '032'
        self.solution = 'Align comment with "elsif" keyword.'
        self.phase = 4

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isElseIfKeyword:
            check.indent_of_comments_above(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            iLineNumber = utils.get_violation_linenumber(dViolation)
            oFile.lines[iLineNumber].indentLevel = dViolation['indent']
            fix.indent(self, oFile.lines[iLineNumber])
