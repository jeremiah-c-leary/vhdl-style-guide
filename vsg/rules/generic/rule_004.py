
from vsg import rule
from vsg import check
from vsg import fix


class rule_004(rule.rule):
    '''
    Generic rule 004 checks indentation of generics.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'generic', '004')
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericDeclaration and not oLine.isEndGenericMap:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.indent(self, oFile.lines[iLineNumber])
