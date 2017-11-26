
from vsg.rules.comment import comment_rule
from vsg import check


class rule_001(comment_rule):
    '''Case rule 001 checks for the proper alignment of comments.'''

    def __init__(self):
        comment_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4
        self.correctCommentColumn = []

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isComment:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._fix_indent(oFile.lines[iLineNumber])
