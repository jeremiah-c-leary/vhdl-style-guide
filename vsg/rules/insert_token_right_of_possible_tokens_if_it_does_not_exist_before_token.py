
from vsg import parser
from vsg import rule
from vsg import violation

from vsg.vhdlFile import utils


class insert_token_right_of_possible_tokens_if_it_does_not_exist_before_token(rule.Rule):
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
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.oInsertToken = insert_token
        self.lAnchorTokens = anchor_tokens
        self.oEndToken = end_token

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by(self.lAnchorTokens[0], self.oEndToken)

    def _analyze(self, lToi):
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
                        sToken = oToken.get_value()

            sSolution = 'Add *is* keyword to the right of ' + sToken
            oViolation = violation.New(iLineNumber, oToi.extract_tokens(iIndex, iIndex), sSolution)
            self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        lTokens.insert(1, self.oInsertToken)
        lTokens.insert(1, parser.whitespace(' '))
        oViolation.set_tokens(lTokens)
