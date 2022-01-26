
from vsg import parser
from vsg import violation

from vsg.rules import utils as rules_utils
from vsg.rule_group import structure
from vsg.vhdlFile import utils


class move_token_next_to_another_token_if_it_exists_between_tokens(structure.Rule):
    '''
    Moves one token next to another and places a single space between them.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    anchor_token : token type
       The token which another token will moved next to.

    token_to_move : token type
       The token which will be moved next to the anchor token.
    '''

    def __init__(self, name, identifier, anchor_token, token_to_move, between_tokens):
        structure.Rule.__init__(self, name, identifier)
        self.subphase = 2
        self.anchor_token = anchor_token
        self.token_to_move = token_to_move
        self.between_tokens = between_tokens

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by(self.between_tokens[0], self.between_tokens[1], bIncludeTillEndOfLine=True)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            for iToken, oToken in enumerate(lTokens):
                if isinstance(oToken, self.anchor_token):
                    iStartIndex = iToken
                if isinstance(oToken, self.token_to_move):
                    iMoveIndex = iToken
                    if not (iStartIndex + 2 == iMoveIndex and isinstance(lTokens[iStartIndex + 1], parser.whitespace)):
                        oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
                        dAction = {}
                        dAction['insertIndex'] = iStartIndex + 1
                        dAction['moveIndex'] = iMoveIndex
                        oViolation.set_action(dAction)
                        oViolation.set_remap()
                        oViolation.fix_blank_lines = True
                        self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        oMoveToken = lTokens.pop(dAction['moveIndex'])
        rules_utils.insert_token(lTokens, dAction['insertIndex'], oMoveToken)
        rules_utils.insert_whitespace(lTokens, dAction['insertIndex'])
        lTokens = utils.fix_blank_lines(lTokens)
        oViolation.set_tokens(lTokens)
