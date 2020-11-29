
from vsg import parser
from vsg import rule
from vsg import violation

from vsg.vhdlFile import utils

lTokens = []
lTokens.append(parser.open_parenthesis)


class rule_005(rule.Rule):
    '''
    Checks for spaces after an open parenthesis.
    '''

    def __init__(self):
        rule.Rule.__init__(self, 'whitespace', '005')
        self.solution = 'Remove spaces after open (.'
        self.phase = 2
        self.iSpaces = 0
        self.lTokens = [parser.open_parenthesis]

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_n_tokens_before_and_after_tokens(2, self.lTokens)

    def _analyze(self, lToi):

        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)

            oRight = lTokens[-2]
            if isinstance(oRight, parser.whitespace):
                if not utils.token_is_whitespace_or_comment(lTokens[-1]):
                    if not lTokens[-1].get_value().isnumeric():
                        oViolation = violation.New(iLine, oToi, self.solution)
                        self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        oToken = lTokens.pop()
        lTokens.pop()
        lTokens.append(oToken)
        oViolation.set_tokens(lTokens)
