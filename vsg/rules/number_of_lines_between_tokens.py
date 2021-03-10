
from vsg import rule
from vsg import severity
from vsg import violation


class number_of_lines_between_tokens(rule.Rule):
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
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.phase = 7
        self.fixable = False  # The user will have to fix line length violations
        self.severity = severity.warning('Warning')
        self.length = iLines
        self.configuration.append('length')
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
