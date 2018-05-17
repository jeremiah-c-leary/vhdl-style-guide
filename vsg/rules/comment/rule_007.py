
from vsg import rule
from vsg import check


class rule_007(rule.rule):
    '''
    Comment rule 007 checks consecutive comment lines above a "use" keyword
    in a library declaration "use" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'comment'
        self.identifier = '007'
        self.solution = 'Align comment with "use" keyword.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isLibraryUse:
                check.indent_of_comments_above(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oFile.lines[iLineNumber].indentLevel = self.dFix['violations'][iLineNumber]
