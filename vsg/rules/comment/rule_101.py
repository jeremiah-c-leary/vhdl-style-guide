
from vsg import parser
from vsg import violation

from vsg.rules import utils
from vsg.rule_group import whitespace


class rule_101(whitespace.Rule):
    '''
    This rule checks for a single space after the a comment pattern.

    |configuring_whitespace_after_comment_rules_link|

    **Violation**

    .. code-block:: vhdl

       --!Comment 1
       --|Comment 2

    **Fix**

    .. code-block:: vhdl

       --! Comment 1
       --| Comment 2
    '''

    def __init__(self):
        whitespace.Rule.__init__(self, name='comment', identifier='101')
        self.solution = 'Undefined'
        self.phase = 2
        self.disable = False
        self.lTokens = [parser.comment]
        self.patterns = ['--!', '--|']
        self.configuration.append('patterns')

    def _get_tokens_of_interest(self, oFile):
        lReturn = []
        lToi = oFile.get_tokens_matching(self.lTokens)
        for oToi in lToi:
            oToken = oToi.get_tokens()[0]
            if self.pattern_match(oToken):
                oToi.set_meta_data('pattern', self.get_matching_pattern(oToken))
                lReturn.append(oToi)
        return lReturn

    def _analyze(self, lToi):
        for oToi in lToi:
            create_violation(self, oToi)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()

        sToken = lTokens[0].get_value()
        sNewToken = sToken[0:dAction['index']] + ' ' + sToken[dAction['index']:]
        lTokens[0].set_value(sNewToken)
        oViolation.set_tokens(lTokens)

    def pattern_match(self, oToken):
        sToken = oToken.get_value()
        if len(sToken) < 4:
            return False
        for sPattern in self.patterns:
            if sToken.startswith(sPattern):
                if not sToken.startswith(sPattern + ' '):
                    return True
        return False

    def get_matching_pattern(self, oToken):
        sToken = oToken.get_value()
        for sPattern in self.patterns:
            if sToken.startswith(sPattern):
                return sPattern
        return None


def create_violation_action_dict(sToken, iIndex):
    dReturn = {}
    dReturn['violation'] = True
    dReturn['index'] = iIndex
    dReturn['solution'] = create_solution(iIndex, sToken)
    return dReturn


def create_violation(self, oToi):
    iIndex = len(oToi.get_meta_data('pattern'))
    dResults = create_violation_action_dict(oToi.get_tokens()[0].get_value(), iIndex)
    oViolation = violation.New(oToi.get_line_number(), oToi, dResults['solution'])
    oViolation.set_action(dResults)
    self.add_violation(oViolation)


def create_solution(iIndex, sComment):
    return 'Change "' + sComment[0:iIndex + 1] + '" to "' + sComment[0:iIndex] + ' ' + sComment[iIndex] + '"'


