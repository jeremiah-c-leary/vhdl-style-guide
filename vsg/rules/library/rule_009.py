
from vsg import rule
from vsg import check
from vsg import fix
from vsg import utils


class rule_009(rule.rule):
    '''
    Library rule 009 checks consecutive comment lines above a "use" keyword
    in a library declaration "use" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'library'
        self.identifier = '009'
        self.solution = 'Align comment with "use" keyword.'
        self.phase = 4

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isLibraryUse:
            check.indent_of_comments_above(self, oFile, iLineNumber)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            iLineNumber = utils.get_violation_linenumber(dViolation)
            oFile.lines[iLineNumber].indentLevel = dViolation['indent']
            fix.indent(self, oFile.lines[iLineNumber])
