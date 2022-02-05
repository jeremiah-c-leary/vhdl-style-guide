
from vsg import parser
from vsg import violation

from vsg.rules import utils
from vsg.rule_group import whitespace


class rule_100(whitespace.Rule):
    '''
    This rule checks for a single space after the **--**.

    **Violation**

    .. code-block:: vhdl

       --Comment 1
       --|Comment 2
       ---Comment
       ---------------------------

    **Fix**

    .. code-block:: vhdl

       -- Comment 1
       --| Comment 2
       --- Comment
       ---------------------------
    '''

    def __init__(self):
        whitespace.Rule.__init__(self, name='comment', identifier='100')
        self.solution = 'Undefined'
        self.phase = 2
        self.disable = False
        self.lTokens = [parser.comment]

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching(self.lTokens)

    def _analyze(self, lToi):
        for oToi in lToi:
            dResults = analyze_comment(oToi)
            if no_space_after_comment_keyword(dResults):
                create_violation(self, oToi, dResults)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()

        sToken = lTokens[0].get_value()
        sNewToken = sToken[0:dAction['index']] + ' ' + sToken[dAction['index']:]
        lTokens[0].set_value(sNewToken)
        oViolation.set_tokens(lTokens)


def no_space_after_comment_keyword(dResults):
    return dResults['violation']


def analyze_comment(oToi):
    sToken = get_comment_string(oToi)
    dAction = create_passing_action_dict()

    if not valid_comment(sToken):
        dAction = check_for_invalid_comment(dAction, sToken)

    return dAction


def create_passing_action_dict():
    dReturn = {}
    dReturn['violation'] = False
    return dReturn


def get_comment_string(oToi):
    lTokens = oToi.get_tokens()
    oToken = lTokens[0]
    return oToken.get_value()


def check_for_invalid_comment(dAction, sToken):
    if is_character_after_double_dash_a_letter_or_number(sToken):
        dAction = create_violation_action_dict(sToken, 2)
    elif is_a_header_candidate(sToken):
        dAction = create_violation_action_dict(sToken, 3)
    return dAction


def is_a_header_candidate(sToken):
    if len(sToken) < 4:
        return False
    if not sToken[3].isspace() and sToken[3].isalnum():
        return True
    return False


def is_character_after_double_dash_a_letter_or_number(sToken):
    if sToken[2].isalnum():
        return True
    return False


def create_violation_action_dict(sToken, iIndex):
    dReturn = {}
    dReturn['violation'] = True
    dReturn['index'] = iIndex
    dReturn['solution'] = create_solution(iIndex, sToken)
    return dReturn


def valid_comment(sToken):
    if len(sToken) == 2:
        return True
    if sToken.startswith('-- '):
        return True
    if sToken.startswith('---'):
        return True
    return False


def create_violation(self, oToi, dResults):
    oViolation = violation.New(oToi.get_line_number(), oToi, dResults['solution'])
    oViolation.set_action(dResults)
    self.add_violation(oViolation)


def create_solution(iIndex, sComment):
    return 'Change "' + sComment[0:iIndex + 1] + '" to "' + sComment[0:iIndex] + ' ' + sComment[iIndex] + '"'
