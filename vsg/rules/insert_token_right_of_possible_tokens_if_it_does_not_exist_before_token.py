

from vsg import parser
from vsg import rule_item
from vsg import violation

from vsg.vhdlFile import utils


class insert_token_right_of_possible_tokens_if_it_does_not_exist_before_token(rule_item.Rule):
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
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.oInsertToken = insert_token
        self.lAnchorTokens = anchor_tokens
        self.oEndToken = end_token

    def analyze(self, oFile):
        lToi = oFile.get_tokens_bounded_by(self.lAnchorTokens[0], self.oEndToken)
        for oToi in lToi:

            iLine, lTokens = utils.get_toi_parameters(oToi)

            if utils.does_token_type_exist_in_list_of_tokens(type(self.oInsertToken), lTokens):
                continue

            dAction = {}
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


    def fix(self, oFile):
        '''
        Applies fixes for any rule violations.
        '''
        if self.fixable:
            self.analyze(oFile)
            self._print_debug_message('Fixing rule: ' + self.name + '_' + self.identifier)
            self._fix_violation(oFile)
            self.violations = []

    def _fix_violation(self, oFile):
        for oViolation in self.violations:
            lTokens = oViolation.get_tokens()
            lTokens.insert(1, self.oInsertToken)
            lTokens.insert(1, parser.whitespace(' '))
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)



