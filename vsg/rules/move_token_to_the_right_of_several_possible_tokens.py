

from vsg import rule
from vsg import parser

from vsg import violation

from vsg.vhdlFile import utils


class move_token_to_the_right_of_several_possible_tokens(rule.Rule):
    '''
    Moves one token next to several possible tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    oToken : token type
       The token to move.

    lTokens : list of token type
       The token types to move oToken to.
       This is an ordered list with the left item containing the token furthest way from oToken.
    '''

    def __init__(self, name, identifier, oMoveToken, lAnchorTokens):
        rule.Rule.__init__(self, name, identifier)
        self.solution = None
        self.phase = 1
        self.oMoveToken = oMoveToken
        self.lAnchorTokens = lAnchorTokens

    def analyze(self, oFile):
        lToi = oFile.get_tokens_bounded_by(self.lAnchorTokens[0], self.oMoveToken)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iInsert = 0
            bPassing = False
            iLine = oToi.get_line_number()
            dAction = {}
            for iToken, oToken in enumerate(lTokens):
                iLine = utils.increment_line_number(iLine, oToken)
                for oAnchorToken in self.lAnchorTokens:
                    if isinstance(oToken, oAnchorToken):
                        dAction['insert'] = iToken + 1
                        self.solution = 'Move "' + lTokens[-1].get_value() + '" to the right of "' + oToken.get_value() + '" on line ' + str(iLine)
                        if isinstance(lTokens[iToken + 1], self.oMoveToken):
                            bPassing = True
                            break
                if bPassing:
                    break
            else:
                oViolation = violation.New(iLine, oToi, self.solution)
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
            oToken = lTokens.pop()
            lTokens.insert(dAction['insert'], oToken)
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)

