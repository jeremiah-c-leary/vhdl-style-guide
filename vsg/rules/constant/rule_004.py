
from vsg.rules import case_rule
from vsg import utils

class rule_004(case_rule):
    '''
    Constant rule 004 checks the constant names have proper case.
    '''

    def __init__(self):
        case_rule.__init__(self, 'constant', '004', 'isConstant', utils.extract_class_identifier_list)
        self.solution = 'Change constant names to ' + self.case + 'case'

#    def _analyze(self, oFile, oLine, iLineNumber):
#        if oLine.isConstant:
#            check.is_lowercase(self, oLine.line.split()[1], iLineNumber)
#
#    def _fix_violations(self, oFile):
#        for iLineNumber in self.violations:
#            fix.lower_case(self, oFile.lines[iLineNumber], oFile.lines[iLineNumber].line.split()[1])
