
from vsg import parser
from vsg import rule
from vsg import violation

from vsg.rules import utils


class rule_100(rule.Rule):
    '''
    This rule will check for spaces after the comment keyword "--".
    '''

    def __init__(self):
        rule.Rule.__init__(self, name='comment', identifier='100')
        self.solution = 'Undefined'
        self.phase = 3
        self.disable = False
        self.lTokens = [parser.comment]

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching(self.lTokens)

    def _analyze(self, lToi):
        for oToi in lToi:
            dResults = analyze_comment(oToi)
            if space_after_comment_keyword(dResults):
                create_violation(self, oToi, dResults)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
 
        sToken = lTokens[0].get_value()
        sNewToken = sToken[0:dAction['index']] + ' ' + sToken[dAction['index']:]
        lTokens[0].set_value(sNewToken)
        oViolation.set_tokens(lTokens)


def space_after_comment_keyword(dResults):
    return dResults['violation']


def analyze_comment(oToi):
    iLine, lTokens = utils.get_toi_parameters(oToi)
    oToken = lTokens[0]
    sToken = oToken.get_value()
    dAction = {}
    dAction['violation'] = False
    if len(sToken) == 2:
        return dAction
    if sToken.startswith('-- '):
        return dAction
    if sToken.startswith('---'):
        return dAction
    if sToken[2].isalnum():
        dAction['violation'] = True
        dAction['index'] = 2
        dAction['solution'] = create_solution(2, sToken)
    elif not sToken[3].isspace():
        if sToken[3].isalnum():
            dAction['violation'] = True
            dAction['index'] = 3
            dAction['solution'] = create_solution(3, sToken)

    return dAction


def create_violation(self, oToi, dResults):
    oViolation = violation.New(oToi.get_line_number(), oToi, dResults['solution'])
    oViolation.set_action(dResults)
    self.add_violation(oViolation)


def create_solution(iIndex, sComment):
    return 'Change "' + sComment[0:iIndex + 1] + '" to "' + sComment[0:iIndex] + ' ' + sComment[iIndex + 1] + '"'
