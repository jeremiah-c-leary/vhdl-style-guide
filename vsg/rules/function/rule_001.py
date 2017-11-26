
from vsg.rules.function import function_rule
from vsg import check


class rule_001(function_rule):
    '''
    Function rule 001 checks for the proper indentation at the beginning of the line.
    '''

    def __init__(self):
        function_rule.__init__(self)
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isFunctionKeyword or oLine.isFunctionBegin or oLine.isFunctionEnd or oLine.isFunctionReturn:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            self._fix_indent(oFile.lines[iLineNumber])
