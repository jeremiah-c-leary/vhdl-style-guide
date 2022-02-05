

from vsg import parser
from vsg import violation

from vsg.vhdlFile import utils
from vsg.rule_group import whitespace
from vsg.rules import utils as rules_utils


class spaces_before_and_after_tokens_when_bounded_by_tokens(whitespace.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of token type pairs
       The tokens to check for a single space between
    '''

    def __init__(self, name, identifier, lTokens, lBetween):
        whitespace.Rule.__init__(self, name=name, identifier=identifier)
        self.lTokens = lTokens
        self.spaces_before = 1
        self.configuration.append('spaces_before')
        self.spaces_after = 4
        self.configuration.append('spaces_after')
        self.lBetween = lBetween
        self.nTokens = 2

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_n_tokens_before_and_after_tokens_bounded_by_tokens(self.nTokens, self.lTokens, self.lBetween)

    def _analyze(self, lToi):
        for oToi in lToi:

            fStartLine = rules_utils.token_list_is_the_beginning_of_a_line(oToi.get_tokens())

            myToi = oToi.extract_tokens(1, 3)

            iLine, lTokens = utils.get_toi_parameters(myToi)
            dAction = {}

            if not fStartLine:
                check_spaces_on_left_side(lTokens, dAction, self.spaces_before)

            check_spaces_on_right_side(lTokens, dAction, self.spaces_after)

            if violations_found(dAction):
                sSolution = create_solution_text(dAction, self.spaces_before, self.spaces_after, lTokens)
                oViolation = violation.New(iLine, myToi, sSolution)
                oViolation.set_action(dAction)
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        fix_left_violations(self, dAction, lTokens)
        fix_right_violations(self, dAction, lTokens)
        oViolation.set_tokens(lTokens)


def fix_left_violations(self, dAction, lTokens):
    if not left_action_exists(dAction):
        return
    if dAction['left']['action'] == 'adjust':
        lTokens[0].set_value(' '*self.spaces_before)
    elif dAction['left']['action'] == 'remove':
        lTokens.pop(0)
    else:
        rules_utils.insert_whitespace(lTokens, self.spaces_before)


def fix_right_violations(self, dAction, lTokens):
    if not right_action_exists(dAction):
        return
    if dAction['right']['action'] == 'adjust':
        lTokens[-1].set_value(' '*self.spaces_after)
    else:
        rules_utils.insert_whitespace(lTokens, len(lTokens) - self.spaces_after)


def right_action_exists(dAction):
    if 'right' in list(dAction.keys()):
        return True
    return False


def left_action_exists(dAction):
    if 'left' in list(dAction.keys()):
        return True
    return False


def create_solution_text(dAction, iNumSpacesBefore, iNumSpacesAfter, lTokens):
    sReturn = ''
    sReturn += create_left_solution(dAction, iNumSpacesBefore, lTokens)
    sReturn += create_right_solution(dAction, iNumSpacesAfter, lTokens)
    return sReturn


def create_left_solution(dAction, iNumSpaces, lTokens):
    sReturn = ''
    if left_action_exists(dAction):
        sReturn = create_solution(dAction, 'left', iNumSpaces, lTokens)
    return sReturn


def create_right_solution(dAction, iNumSpaces, lTokens):
    sReturn = ''
    if right_action_exists(dAction):
        sReturn = create_solution(dAction, 'right', iNumSpaces, lTokens)
    return sReturn


def create_solution(dAction, sKey, iNumSpaces, lTokens):
    sSide = dAction[sKey]['side']
    sTokenValue = lTokens[1].get_value()
    if dAction[sKey]['action'] == 'adjust':
        sReturn = f'Change number of spaces {sSide} *{sTokenValue}* to {iNumSpaces}.  '
    elif dAction[sKey]['action'] == 'remove':
        sReturn = f'Remove all space(s) {sSide} *{sTokenValue}*. '
    else:
        sReturn = f'Add {iNumSpaces} space(s) {sSide} *{sTokenValue}*.  '
    return sReturn.strip()


def check_spaces_on_left_side(lTokens, dAction, iSpaces):
    check_for_adjustment_of_existing_whitespace(lTokens, dAction, iSpaces)
    check_for_removal_of_existing_whitespace(lTokens, dAction, iSpaces)
    check_for_insertion_of_missing_whitespace(lTokens, dAction, iSpaces)


def check_for_adjustment_of_existing_whitespace(lTokens, dAction, iSpaces):
    oLeft = lTokens[0]
    if isinstance(oLeft, parser.whitespace) and iSpaces > 0:
        set_adjust_action('left', oLeft, dAction, iSpaces)


def check_for_removal_of_existing_whitespace(lTokens, dAction, iSpaces):
    oLeft = lTokens[0]
    if isinstance(oLeft, parser.whitespace) and iSpaces == 0:
        set_remove_action('left', dAction)


def check_for_insertion_of_missing_whitespace(lTokens, dAction, iSpaces):
    oLeft = lTokens[0]
    if not isinstance(oLeft, parser.whitespace) and iSpaces > 0:
        set_insert_action('left', dAction)


def check_spaces_on_right_side(lTokens, dAction, iSpaces):
    oRight = lTokens[-1]
    if isinstance(oRight, parser.whitespace):
        set_adjust_action('right', oRight, dAction, iSpaces)
    else:
        set_insert_action('right', dAction)


def set_adjust_action(sSide, oToken, dAction, iSpaces):
    if iSpaces != len(oToken.get_value()):
        dAction[sSide] = {}
        dAction[sSide]['action'] = 'adjust'
        set_side_of_action(sSide, dAction)


def set_remove_action(sSide, dAction):
    dAction[sSide] = {}
    dAction[sSide]['action'] = 'remove'
    set_side_of_action(sSide, dAction)


def set_insert_action(sSide, dAction):
    dAction[sSide] = {}
    dAction[sSide]['action'] = 'insert'
    set_side_of_action(sSide, dAction)


def set_side_of_action(sSide, dAction):
    if sSide == 'right':
        dAction[sSide]['side'] = 'after'
    else:
        dAction[sSide]['side'] = 'before'


def violations_found(dAction):
    if len(list(dAction.keys())) > 0:
        return True
    return False
