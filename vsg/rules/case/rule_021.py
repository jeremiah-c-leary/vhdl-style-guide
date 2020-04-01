
from vsg import rule
from vsg import check
from vsg import utils
from vsg import fix


class rule_021(rule.rule):
    '''
    Case rule 021 checks consecutive comment lines above a "when" keyword
    in a case statement are aligned with the "when" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'case'
        self.identifier = '021'
        self.solution = 'Align comment with "when" keyword.'
        self.phase = 4

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isCaseWhenKeyword:
            check.indent_of_comments_above(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            iLineNumber = utils.get_violation_linenumber(dViolation)
            oFile.lines[iLineNumber].indentLevel = dViolation['indent']
            fix.indent(self, oFile.lines[iLineNumber])
