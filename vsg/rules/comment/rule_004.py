
from vsg import rule


class rule_004(rule.rule):
    '''
    Comment rule 004 ensures there is at least one space before comments on a line with code.
    '''

    def __init__(self):
        rule.rule.__init__(self, name='comment', identifier='004')
        self.phase = 2
        self.solution = 'Add a space before the comment --'

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.__dict__['hasInlineComment']:
            if oLine.line[oLine.commentColumn - 1] != ' ':
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            idx = oLine.commentColumn
            oLine.update_line(" ".join((oLine.line[:idx],oLine.line[idx:])))


