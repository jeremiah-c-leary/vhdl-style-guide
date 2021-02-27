
from vsg import parser
from vsg import rule
from vsg import severity
from vsg import violation


class file_length(rule.Rule):
    '''
    Checks the length of the file.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    '''

    def __init__(self, name, identifier):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.phase = 7
        self.fixable = False  # The user will have to fix line length violations
        self.severity = severity.warning('Warning')
        self.length = 2000
        self.configuration.append('length')

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching([parser.carriage_return])

    def _analyze(self, lToi):
        if len(lToi) > self.length:
            sSolution = 'Reduce file length to less than ' + str(self.length) + ' lines'
            oViolation = violation.New(self.length, None, sSolution)
            self.add_violation(oViolation)
