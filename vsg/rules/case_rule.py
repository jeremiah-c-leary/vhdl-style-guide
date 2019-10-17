
from vsg import rule
from vsg import fix
from vsg import check
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
        self.words_to_fix = set()

    @abstractmethod
    def _extract(self, oLine):
        pass

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.__dict__[self.sTrigger]:
            words = self._extract(oLine)

            # ToDo: Raise exception when case differs from lower and upper
            if self.case == 'lower':
                check_function = check.is_lowercase
            else:
                check_function = check.is_uppercase

            for word in words:
                if check_function(self, word, iLineNumber) == False:
                    self.words_to_fix.add(word)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            for word in self.words_to_fix:
                if self.case == 'lower':
                    fix_function = fix.lower_case
                else:
                    fix_function = fix.upper_case

                fix_function(oFile.lines[iLineNumber], word)

    def _get_solution(self, iLineNumber):
       return self.solution + self.case + 'case.'
