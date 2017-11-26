
from vsg.rules.type import type_rule
from vsg import check


class rule_005(type_rule):
    '''
    Type rule 005 checks for the proper indentation of multiline types.
    '''

    def __init__(self):
        type_rule.__init__(self)
        self.identifier = '005'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.insideType and not oLine.isTypeKeyword:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._fix_indent(oFile.lines[iLineNumber])
