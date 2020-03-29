
from vsg import rule
from vsg import line
from vsg import utils

import re


class rule_010(rule.rule):
    '''
    Process rule 010 checks the "begin" keyword is on it's own line.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'process', '010')
        self.solution = 'Place "begin" keyword on seperate line.'
        self.phase = 1

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.isProcessBegin and not re.match('^\s*begin', oLine.line, re.IGNORECASE):
            dViolation = utils.create_violation_dict(iLineNumber)
            self.add_violation(dViolation)

    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            iLineNumber = utils.get_violation_linenumber(dViolation)
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(re.sub('begin', ' '*len('begin'), oLine.line, 1, flags=re.IGNORECASE))
            oLine.isProcessBegin = False
            oFile.lines.insert(iLineNumber + 1, line.line('  begin'))
            oFile.lines[iLineNumber + 1].isProcessBegin = True
            oFile.lines[iLineNumber + 1].indentLevel = oLine.indentLevel
