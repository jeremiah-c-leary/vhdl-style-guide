
from vsg import rule
from vsg import check


class rule_009(rule.rule):
    '''
    Comment rule 009 checks consecutive comment lines above an "else" keyword
    in an if statement are aligned with the "else" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'comment'
        self.identifier = '009'
        self.solution = 'Align comment with "else" keyword.'
        self.phase = 4

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isElseKeyword:
            check.indent_of_comments_above(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oFile.lines[iLineNumber].indentLevel = self.dFix['violations'][iLineNumber]
            sLine = oFile.lines[iLineNumber].line.strip()
            oFile.lines[iLineNumber].update_line(' ' * self.indentSize * self.dFix['violations'][iLineNumber] + sLine)
