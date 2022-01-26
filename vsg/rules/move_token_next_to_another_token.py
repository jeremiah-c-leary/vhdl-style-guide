

from vsg import parser
from vsg import violation

from vsg.rules import utils as rules_utils
from vsg.rule_group import structure
from vsg.vhdlFile import utils


class move_token_next_to_another_token(structure.Rule):
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

    def __init__(self, name, identifier, anchor_token, token_to_move):
        structure.Rule.__init__(self, name, identifier)
        self.subphase = 2
        self.anchor_token = anchor_token
        self.token_to_move = token_to_move

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by(self.anchor_token, self.token_to_move, bIncludeTillEndOfLine=True)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if not utils.are_next_consecutive_token_types([parser.whitespace, self.token_to_move], 1, lTokens) and \
               not utils.are_next_consecutive_token_types([self.token_to_move], 1, lTokens):
                oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
                oViolation.set_remap()
                oViolation.fix_blank_lines = True
                self.add_violation(oViolation)


    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        iIndex = oViolation.get_token_value()

        rules_utils.insert_token(lTokens, 1, lTokens.pop(iIndex))
        rules_utils.insert_whitespace(lTokens, 1)
        lNewTokens = utils.remove_consecutive_whitespace_tokens(lTokens)
        lNewTokens = utils.fix_blank_lines(lNewTokens)

        oViolation.set_tokens(lNewTokens)
