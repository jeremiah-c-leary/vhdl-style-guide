
from vsg import parser
from vsg import violation

from vsg.rules import utils as rules_utils
from vsg.rule_group import structure
from vsg.vhdlFile import utils


class insert_token_right_of_possible_tokens_if_it_does_not_exist_before_token(structure.Rule):
    '''
    Checks for the existence of a token and will insert it if it does not exist.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    insert_token : token object
       token to insert if it does not exist.

    anchor_token : token object type
       token to check if insert_token exists to the right of

    end_token : token object type
       token that bounds the search for the insert_token
    '''

    def __init__(self, name, identifier, insert_token, anchor_tokens, end_token):
        structure.Rule.__init__(self, name=name, identifier=identifier)
        self.oInsertToken = insert_token
        self.lAnchorTokens = anchor_tokens
        self.oEndToken = end_token
        self.action = 'add'
        self.configuration.append('action')

    def _get_tokens_of_interest(self, oFile):
        if self.action == 'add':
            return oFile.get_tokens_bounded_by(self.lAnchorTokens[0], self.oEndToken)
        else:
            return oFile.get_token_and_n_tokens_before_it([self.oInsertToken], 1)

    def _analyze(self, lToi):
        if self.action == 'remove':
            for oToi in lToi:
                sSolution = self.action.capitalize() + ' ' + self.solution
                self.add_violation(violation.New(oToi.get_line_number(), oToi, sSolution))
            return

        for oToi in lToi:

            iLine, lTokens = utils.get_toi_parameters(oToi)

            if utils.does_token_type_exist_in_list_of_tokens(type(self.oInsertToken), lTokens):
                continue

            for iToken, oToken in enumerate(lTokens):
                iLine = utils.increment_line_number(iLine, oToken)
                for oSearch in self.lAnchorTokens:
                    if isinstance(oToken, oSearch):
                        iIndex = iToken
                        iLineNumber = iLine

            sSolution = self.action.capitalize() + ' ' + self.solution
            dAction = {}
            dAction['whitespace'] = False
            dAction['carriage_return'] = False
            if isinstance(lTokens[iIndex + 1], parser.whitespace):
                dAction['whitespace'] = True
            if isinstance(lTokens[iIndex + 1], parser.carriage_return):
                dAction['carriage_return'] = True

            oViolation = violation.New(iLineNumber, oToi.extract_tokens(iIndex, iIndex), sSolution)
            oViolation.set_action(dAction)
            self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if self.action == 'remove':
            rules_utils.remove_optional_item(oViolation, self.oInsertToken)
        else:
            dAction = oViolation.get_action()
            if isinstance(lTokens[0], parser.close_parenthesis) and dAction['carriage_return']:
                rules_utils.insert_token(lTokens, 1, self.oInsertToken)
            elif isinstance(lTokens[0], parser.close_parenthesis) and not dAction['whitespace']:
                rules_utils.insert_whitespace(lTokens, 1)
                rules_utils.insert_token(lTokens, 1, self.oInsertToken)
            else:
                rules_utils.insert_token(lTokens, 1, self.oInsertToken)
                rules_utils.insert_whitespace(lTokens, 1)
            oViolation.set_tokens(lTokens)
