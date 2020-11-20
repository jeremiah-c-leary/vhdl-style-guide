

from vsg import rule_item
from vsg import parser

from vsg import violation

from vsg.vhdlFile import utils


class move_token_next_to_another_token_if_it_exists_between_tokens(rule_item.Rule):
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
        rule_item.Rule.__init__(self, name, identifier)
        self.solution = None
        self.phase = 1
        self.subphase = 2
        self.anchor_token = anchor_token
        self.token_to_move = token_to_move
        self.between_tokens = between_tokens

    def analyze(self, oFile):
        lToi = oFile.get_tokens_bounded_by(self.between_tokens[0], self.between_tokens[1])
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
            dAction = oViolation.get_action()
            oMoveToken = lTokens.pop(dAction['moveIndex'])
            lTokens.insert(dAction['insertIndex'], oMoveToken)
            lTokens.insert(dAction['insertIndex'], parser.whitespace(' '))
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)

