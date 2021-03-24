
from vsg import parser
from vsg import rule
from vsg import violation

from vsg.rules import utils


class rule_011(rule.Rule):
    '''
    This rule will move inline comm
    '''

    def __init__(self):
        rule.Rule.__init__(self, name='comment', identifier='011')
        self.solution = 'Move inline comment to previous line.'
        self.phase = 1
        self.disable = True
        self.lTokens = [parser.comment]

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_line_which_includes_tokens(self.lTokens)

    def _analyze(self, lToi):
        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)
            if utils.does_line_start_with_comment(lTokens):
                continue

            iWhitespace = 0
            for iToken, oToken in enumerate(lTokens):
                if isinstance(oToken, parser.comment):
                    dAction = {}
                    if isinstance(lTokens[iToken - 1], parser.whitespace):
                        dAction['iToken'] = iToken - 1
                    else:
                        dAction['iToken'] = iToken
                    
                    oViolation = violation.New(iLine, oToi, self.solution)
                    oViolation.set_action(dAction)
                    self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()

        lTemp = lTokens[dAction['iToken']:]
        lTemp.append(parser.carriage_return())
        lTemp.extend(lTokens[:dAction['iToken']])

        oViolation.set_tokens(lTemp)
