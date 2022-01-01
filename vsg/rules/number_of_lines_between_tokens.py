
from vsg.rule_group import length
from vsg import violation


class number_of_lines_between_tokens(length.Rule):
    '''
    Checks the number of lines between tokens do not exceed a specified number

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    '''

    def __init__(self, name, identifier, oLeftToken, oRightToken, iLines):
        length.Rule.__init__(self, name=name, identifier=identifier)
        self.length = iLines
        self.oLeftToken = oLeftToken
        self.oRightToken = oRightToken

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_line_count_between_tokens(self.oLeftToken, self.oRightToken)

    def _analyze(self, lToi):
        for oToi in lToi:
            if oToi.get_token_value() > self.length:
                sSolution = 'Reduce process to less than ' + str(self.length) + ' lines'
                oViolation = violation.New(oToi.get_line_number(), None, sSolution)
                self.add_violation(oViolation)
