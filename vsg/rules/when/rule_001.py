
import re

from vsg import rule
from vsg import utils


class rule_001(rule.rule):
    '''
    With rule 001 checks the when and else keywords are on the same line
    '''

    def __init__(self):
        rule.rule.__init__(self, 'when', '001')
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.insideWhen:
            if re.match('^\s*else', oLine.line, flags=re.IGNORECASE):
                dViolation = utils.create_violation_dict(iLineNumber)
                self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations:
            iLineNumber = utils.get_violation_line_number(dViolation)
            oPreviousLine = oFile.lines[iLineNumber - 1]
            oLine = oFile.lines[iLineNumber]
            iIndex = utils.end_of_line_index(oPreviousLine)
            oPreviousLine.update_line(oPreviousLine.line[:iIndex] + ' else' + oPreviousLine.line[iIndex:])
            utils.clear_keyword_from_line(oLine, 'else')
