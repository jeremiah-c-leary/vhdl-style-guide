

from vsg import rule
from vsg import parser

from vsg import violation

from vsg.vhdlFile import utils


class move_token_next_to_another_token(rule.Rule):
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
        rule.Rule.__init__(self, name, identifier)
        self.solution = None
        self.phase = 1
        self.subphase = 2
        self.anchor_token = anchor_token
        self.token_to_move = token_to_move

    def analyze(self, oFile):
        lToi = oFile.get_tokens_bounded_by(self.anchor_token, self.token_to_move)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if not utils.are_next_consecutive_token_types([self.anchor_token, parser.whitespace, self.token_to_move], 0, lTokens) and \
               not utils.are_next_consecutive_token_types([self.anchor_token, self.token_to_move], 0, lTokens):
                self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution)) 


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
            lTokens.insert(1, lTokens.pop())
            lTokens.insert(1, parser.whitespace(' '))
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)

