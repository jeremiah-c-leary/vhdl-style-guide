
from vsg import rule
from vsg import check
from vsg import fix
from vsg import utils


class rule_001(rule.rule):
    '''
    Function rule 001 checks for the proper indentation at the beginning of the line.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'function'
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isFunctionKeyword or oLine.isFunctionBegin or oLine.isFunctionEnd or oLine.isFunctionReturn:
            check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            fix.indent(self, utils.get_violating_line(oFile, dViolation))
