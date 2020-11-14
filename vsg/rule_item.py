
from vsg import rule
from vsg import utils


class Rule(rule.rule):

    def __init__(self, name, identifier):
        rule.rule.__init__(self, name, identifier)


    def fix(self, oFile):
        '''
        Applies fixes for any rule violations.
        '''
        if self.fixable:
            self.analyze(oFile)
            self._print_debug_message('Fixing rule: ' + self.name + '_' + self.identifier)
            for dViolation in self.violations[::-1]:
                self._fix_violation(oFile, dViolation)
            self.violations = []


    def _get_solution(self, iLineNumber):
        return utils.get_violation_solution_at_line_number(self.violations, iLineNumber)


    def get_violations_at_linenumber(self, iLineNumber):
        '''
        Returns a list of formatted violations.

        Parameters:

          iLineNumber (integer)

        Returns: (list of dictionaries)
        '''
        lReturn = []

        for violation in self.violations:
            if violation.get_line_number() == iLineNumber:
                lReturn.append(self._build_violation_dict_from_violation_object(violation))

        return lReturn
