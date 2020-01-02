
import re

from vsg import rule
from vsg import utils


class rule_001(rule.rule):
    '''
    Checks for and fixes words case.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    sTrigger : string
       The line attribute the rule applies to.

    Attribute
    ----------

    self.phase : integer = 6
       Sets the phase the rule will run in.

    self.solution : string = None
       Instructions on how to fix the violation.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'range', '001')
        self.phase = 6
        self.solution = 'Change downto keyword to '
        self.case = 'lower'
        self.configuration.append('case')

    def _analyze(self, oFile, oLine, iLineNumber):
        if re.match('^.*\sdownto[\s|$]', oLine.lineNoComment, re.IGNORECASE):
            if self.case == 'lower':
                if not re.match('^.*\sdownto[\s|$]', oLine.lineNoComment):
                    self.add_violation(iLineNumber)
                    _save_string_index_of_downto(self, oLine, iLineNumber)
            else:
                if not re.match('^.*\sDOWNTO[\s|$]', oLine.lineNoComment):
                    self.add_violation(iLineNumber)
                    _save_string_index_of_downto(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            oLine = oFile.lines[iLineNumber]
            iIndex = self.dFix['violations'][iLineNumber]
            if self.case == 'lower':
                utils.replace_word_by_index(oLine, iIndex, ' downto')
            else:
                utils.replace_word_by_index(oLine, iIndex, ' DOWNTO')

    def _get_solution(self, iLineNumber):
        return self.solution + self.case + 'case.'


def _save_string_index_of_downto(self, oLine, iLineNumber):
    sLine = oLine.lineNoComment.lower()
    iIndex = sLine.find(' downto')
    self.dFix['violations'][iLineNumber] = iIndex
