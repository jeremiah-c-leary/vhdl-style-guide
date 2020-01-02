
import re

from vsg import rule
from vsg import utils


class rule_002(rule.rule):
    '''
    Checks the case of the **to** keyword in range definitions.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'range', '002')
        self.phase = 6
        self.solution = 'Change to keyword to '
        self.case = 'lower'
        self.configuration.append('case')

    def _analyze(self, oFile, oLine, iLineNumber):
        if re.match('^.*\sto[\s|$]', oLine.lineNoComment, re.IGNORECASE):
            if self.case == 'lower':
                if not re.match('^.*\sto[\s|$]', oLine.lineNoComment):
                    self.add_violation(iLineNumber)
                    _save_string_index_of_to(self, oLine, iLineNumber)
            else:
                if not re.match('^.*\sTO[\s|$]', oLine.lineNoComment):
                    self.add_violation(iLineNumber)
                    _save_string_index_of_to(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            iIndex = self.dFix['violations'][iLineNumber]
            if self.case == 'lower':
                utils.replace_word_by_index(oLine, iIndex, ' to')
            else:
                utils.replace_word_by_index(oLine, iIndex, ' TO')

    def _get_solution(self, iLineNumber):
        return self.solution + self.case + 'case.'


def _save_string_index_of_to(self, oLine, iLineNumber):
    sLine = oLine.lineNoComment.lower()
    iIndex = sLine.find(' to')
    self.dFix['violations'][iLineNumber] = iIndex
