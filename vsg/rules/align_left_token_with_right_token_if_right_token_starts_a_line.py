
from vsg import parser
from vsg import violation

from vsg.rules import utils as rules_utils
from vsg.rule_group import alignment
from vsg.vhdlFile import utils


class align_left_token_with_right_token_if_right_token_starts_a_line(alignment.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : token object list
       List of tokens to align

    left_token : token object
       The first token that defines the region

    right_token : token object
       The second token that defines the region
    '''

    def __init__(self, name, identifier, left_token, right_token):
        alignment.Rule.__init__(self, name=name, identifier=identifier)
        self.left_token = left_token
        self.right_token = right_token

    def analyze(self, oFile):

        lToi = oFile.get_tokens_bounded_by(self.left_token, self.right_token)
        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)

            if not utils.does_token_type_exist_in_list_of_tokens(parser.carriage_return, lTokens):
                continue

            if not utils.does_token_start_line(len(lTokens) - 1, lTokens):
                continue

            iStartIndex = oToi.get_start_index()
            iEndIndex = oToi.get_end_index()

            iRightColumn = oFile.get_column_of_token_index(iStartIndex)
            iLeftColumn = oFile.get_column_of_token_index(iEndIndex)

            if iRightColumn + 1 != iLeftColumn:
                iLineNumber = iLine + utils.count_token_types_in_list_of_tokens(parser.carriage_return, lTokens)
                sSolution = 'Move ' + lTokens[-1].get_value() + ' to column ' + str(iRightColumn)
                dAction = {}
                if iLeftColumn == 1:
                    dAction['action'] = 'insert'
                else:
                    dAction['action'] = 'adjust'
                dAction['column'] = iRightColumn
                oViolation = violation.New(iLineNumber, oToi, sSolution)
                oViolation.set_action(dAction)
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        if dAction['action'] == 'insert':
            rules_utils.insert_whitespace(lTokens, len(lTokens) - 1, dAction['column'])
        else:
            lTokens[-2].set_value(' '*dAction['column'])
        oViolation.set_tokens(lTokens)
