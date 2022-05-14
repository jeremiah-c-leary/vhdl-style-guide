

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
        self.number_of_spaces = 1
        self.configuration.append('number_of_spaces')

    def _get_tokens_of_interest(self, oFile):
        lToi_a = oFile.get_sequence_of_tokens_matching([self.left_token, parser.whitespace, self.right_token])
        lToi_b = oFile.get_sequence_of_tokens_matching([self.left_token, self.right_token])

        return utils.combine_two_token_class_lists(lToi_a, lToi_b)

    def _analyze(self, lToi):
        for oToi in lToi:
            if self.number_of_spaces_is_an_integer():
                self.analyze_integer_spaces(oToi)
            elif self.number_of_spaces_is_gte():
                self.analyze_gte_spaces(oToi)
            elif self.number_of_spaces_is_gt():
                self.analyze_gt_spaces(oToi)

    def number_of_spaces_is_gt(self):
        if self.number_of_spaces.startswith('>'):
            return True
        return False

    def analyze_gt_spaces(self, oToi):
        iSpaces = int(self.number_of_spaces[1:]) + 1
        iWhitespaces = extract_length_of_whitespace(oToi)
        if iWhitespaces < iSpaces:
            self.create_violation(oToi, iSpaces)

    def number_of_spaces_is_gte(self):
        if self.number_of_spaces.startswith('>='):
            return True
        return False

    def analyze_gte_spaces(self, oToi):
        iSpaces = int(self.number_of_spaces[2:])
        iWhitespaces = extract_length_of_whitespace(oToi)
        if iWhitespaces < iSpaces:
            self.create_violation(oToi, iSpaces)

    def number_of_spaces_is_an_integer(self):
        if isinstance(self.number_of_spaces, str):
            return False
        return True

    def analyze_integer_spaces(self, oToi):
        iWhitespaces = extract_length_of_whitespace(oToi)
        if iWhitespaces != self.number_of_spaces:
            self.create_violation(oToi, self.number_of_spaces)

    def create_violation(self, oToi, iNumSpaces):
        sSolution = self.create_solution(oToi, iNumSpaces)
        oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
        dAction = {}
        dAction['spaces'] = iNumSpaces
        oViolation.set_action(dAction)
        self.add_violation(oViolation)

    def create_solution(self, oToi, iNumSpaces):
        lTokens = oToi.get_tokens()
        sSolution = f'Change the number of spaces between {lTokens[0].get_value()} and {lTokens[2].get_value()} to {str(iNumSpaces)}'
        return sSolution

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        if isinstance(lTokens[1], parser.whitespace):
            lTokens[1].set_value(' '*dAction['spaces'])
        else:
            rules_utils.insert_whitespace(lTokens, dAction['spaces'])
        oViolation.set_tokens(lTokens)


def extract_length_of_whitespace(oToi):
    lTokens = oToi.get_tokens()
    iWhitespaces = len(lTokens[1].get_value())
    return iWhitespaces

