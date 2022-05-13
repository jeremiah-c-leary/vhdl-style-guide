

from vsg import parser
from vsg import violation

from vsg.rule_group import whitespace
from vsg.rules import utils as rules_utils

from vsg.vhdlFile import utils


class Rule(whitespace.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    left_token : token object
       The left token to check for a space between the right token

    right_token : token object
       The right token to check for a space between the left token
    '''

    def __init__(self, name, identifier):
        whitespace.Rule.__init__(self, name=name, identifier=identifier)
        self.left_token = None
        self.right_token = None
        self.maximum_number_of_spaces = 1
        self.configuration.append('maximum_number_of_spaces')
        self.minimum_number_of_spaces = 1
        self.configuration.append('minimum_number_of_spaces')

    def _get_tokens_of_interest(self, oFile):
        lToi_a = oFile.get_sequence_of_tokens_matching([self.left_token, parser.whitespace, self.right_token])
        lToi_b = oFile.get_sequence_of_tokens_matching([self.left_token, self.right_token])

        return utils.combine_two_token_class_lists(lToi_a, lToi_b)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if len(lTokens) == 2:
                self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))
            else:
                iWhitespaces = len(lTokens[1].get_value())
                if iWhitespaces != self.maximum_number_of_spaces and iWhitespaces != self.minimum_number_of_spaces:
                    oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
                    dAction = {}
                    dAction['spaces'] = self.maximum_number_of_spaces
                    oViolation.set_action(dAction)
                    self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        if isinstance(lTokens[1], parser.whitespace):
            lTokens[1].set_value(' '*dAction['spaces'])
        else:
            rules_utils.insert_whitespace(lTokens, dAction['spaces'])
        oViolation.set_tokens(lTokens)
