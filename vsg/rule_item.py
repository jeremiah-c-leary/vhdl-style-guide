
from abc import abstractmethod

from vsg import rule
from vsg import utils


class Rule(rule.rule):

    def __init__(self, name, identifier):
        rule.rule.__init__(self, name, identifier)
        self.regionBegin = None
        self.regionEnd = None

    @abstractmethod
    def _get_regions(self, oFile):
        return oFile.get_region_bounded_by_items(self.regionBegin, self.regionEnd)

#    def _get_regions(self, oFile):
#        pass

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

    def analyze(self, oFile):
        '''
        Performs the analysis.
        '''
        self._print_debug_message('Analyzing rule: ' + self.name + '_' + self.identifier)
        for dRegion in self._get_regions(oFile):
            for iLine, oLine in enumerate(dRegion['lines']):
                if not self._is_vsg_off(oLine):
                    self._analyze_region(oFile, iLine, oLine, dRegion)

    def _get_solution(self, iLineNumber):
        return utils.get_violation_solution_at_line_number(self.violations, iLineNumber)

    def _analyze_region(self, oFile, iLine, oLine, dRegion):
        return None

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
