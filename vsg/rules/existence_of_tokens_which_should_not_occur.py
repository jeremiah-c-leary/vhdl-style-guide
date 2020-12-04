
from vsg import rule
from vsg import violation


class existence_of_tokens_which_should_not_occur(rule.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of parser object types
       object types to check the prefix

    lPrefixes : string list
       acceptable prefixes
    '''

    def __init__(self, name, identifier, lTokens):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.lTokens = lTokens
        self.fixable = False

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching(self.lTokens)

    def _analyze(self, lToi):
        for oToi in lToi:
            oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
            self.add_violation(oViolation)
