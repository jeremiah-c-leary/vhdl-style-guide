
from vsg import rule
from vsg import fix
from vsg import utils
from abc import abstractmethod


class case_rule(rule.rule):
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

    def __init__(self, name=None, identifier=None, sTrigger=None):
        rule.rule.__init__(self, name, identifier)
        self.phase = 6
        self.solution = None
        self.sTrigger = sTrigger
        self.case = 'lower'
        self.configuration.append('case')

    @abstractmethod
    def _extract(self, oLine):
        pass

    def _is_uppercase(self, sString):
        if not sString == sString.upper():
            return False

        return True

    def _is_lowercase(self, sString):
        if not sString == sString.lower():
            return False

        return True

    def _analyze(self, oFile, oLine, iLineNumber):
        if self.sTrigger is None or oLine.__dict__[self.sTrigger]:
            words = self._extract(oLine)

            if self.case == 'lower':
                check_function = self._is_lowercase
            elif self.case == 'upper':
                check_function = self._is_uppercase
            else:
                raise Exception("case option needs to be 'lower' or 'upper', detected: {self.case}")

            violation = utils.create_violation_dict(iLineNumber)
            violation['words_to_fix'] = set()
            for word in words:
                if not check_function(word):
                    violation['words_to_fix'].add(word)

            if violation['words_to_fix']:
                self.add_violation(violation)

    def _fix_violations(self, oFile):
        for violation in self.violations:
            iLineNumber = utils.get_violation_linenumber(violation)
            for word in violation['words_to_fix']:
                if self.case == 'lower':
                    fix_function = fix.lower_case
                else:
                    fix_function = fix.upper_case

                fix_function(oFile.lines[iLineNumber], word)

    def _get_solution(self, iLineNumber):
        return self.solution + self.case + 'case.'
