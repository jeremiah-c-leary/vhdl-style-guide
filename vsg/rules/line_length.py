

from vsg.rule_group import length
from vsg import violation


class line_length(length.Rule):
    '''
    Checks for a at least a single space before a token.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    '''

    def __init__(self, name, identifier):
        length.Rule.__init__(self, name=name, identifier=identifier)
        self.disable = False
        self.length = 120
        self.solution = 'Reduce line to less than ' + str(self.length) + ' characters'

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_lines_with_length_that_exceed_column(self.length)

    def _analyze(self, lToi):
        for oToi in lToi:
            oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
            self.add_violation(oViolation)
