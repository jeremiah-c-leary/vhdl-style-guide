
from vsg import rule
from vsg import check
from abc import abstractmethod


class suffix_rule(rule.rule):
    '''
    Checks for identifiers suffixes. This rule can not fix!

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

    self.phase : integer = 7
       Sets the phase the rule will run in.

    self.solution : string = None
       Instructions on how to fix the violation.
    '''

    def __init__(self, name=None, identifier=None, sTrigger=None):
        rule.rule.__init__(self, name, identifier)
        self.phase = 7
        self.solution = None
        self.sTrigger = sTrigger
        self.suffixes = None
        self.fixable = False  # The user will have to fix any desired suffixes.
        self.disable = True
        self.configuration.append('suffixes')

    @abstractmethod
    def _extract(self, oLine):
        pass

    def _analyze(self, oFile, oLine, iLineNumber):
        if oLine.__dict__[self.sTrigger]:
            words = self._extract(oLine)

            check.has_suffix(self, self.suffixes, words, iLineNumber)

    def _get_solution(self, iLineNumber):
        return self.solution + ' identifiers should end with one of ' + str(self.suffixes) + ' suffixes.'
