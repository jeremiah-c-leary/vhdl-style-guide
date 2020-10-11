

from vsg import rule_item
from vsg import severity
from vsg import violation

from vsg.vhdlFile import utils


class line_length(rule_item.Rule):
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
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.phase = 7
        self.fixable = False  # The user will have to fix line length violations
        self.disable = False
        self.severity = severity.set_warning_severity
        self.length = 120
        self.configuration.append('length')
        self.solution = 'Reduce line to less than ' + str(self.length) + ' characters'

    def analyze(self, oFile):

        dAnalysis = {}

        lToi = oFile.get_lines_with_length_that_exceed_column(self.length)
        for oToi in lToi:
            oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
            self.violations.append(oViolation)
