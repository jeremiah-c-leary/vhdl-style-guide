
from vsg import parser
from vsg.rule_group import length
from vsg import violation


class file_length(length.Rule):
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
        length.Rule.__init__(self, name=name, identifier=identifier)
        self.length = 2000

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching([parser.carriage_return])

    def _analyze(self, lToi):
        if len(lToi) > self.length:
            sSolution = 'Reduce file length to less than ' + str(self.length) + ' lines'
            oViolation = violation.New(self.length, None, sSolution)
            self.add_violation(oViolation)
