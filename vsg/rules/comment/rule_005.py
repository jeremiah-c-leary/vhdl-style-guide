
from vsg import rule
from vsg import check


class rule_005(rule.rule):
    '''
    Comment rule 005 checks consecutive comment lines above a "when" keyword
    in a case statement are aligned with the "when" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'comment'
        self.identifier = '005'
        self.solution = 'Align comment with "when" keyword.'
        self.phase = 4

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isCaseWhenKeyword:
            check.indent_of_comments_above(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oFile.lines[iLineNumber].indentLevel = self.dFix['violations'][iLineNumber]
