
from vsg import parser
from vsg import rule
from vsg import violation

from vsg.rules import utils as rules_utils


class rule_002(rule.Rule):
    '''
    Checks the expressions in if statements are enclosed in ()'s.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.
    '''

    def __init__(self):
        rule.Rule.__init__(self, 'if', '002')
        self.phase = 1
        self.parenthesis = 'insert'
        self.configuration.append('parenthesis')

    def _get_tokens_of_interest(self, oFile):
        if self.parenthesis == 'insert':
            return oFile.get_if_statement_conditions()
        return oFile.get_if_statement_conditions(fRemoveWhitespace=False)

    def _analyze(self, lToi):
        for oToi in lToi:
            if insert_parenthesis(self.parenthesis):
                check_insert_parenthesis(self, oToi)
            else:
                check_remove_parenthesis(self, oToi)

    def _fix_violation(self, oViolation):
        if insert_parenthesis(self.parenthesis):
            add_enclosing_parens(oViolation)
        else:
            remove_enclosing_parens(oViolation)


def remove_enclosing_parens(oViolation):
    lTokens = oViolation.get_tokens()
    dAction = oViolation.get_action()

    lNewTokens = remove_open_paren(lTokens, dAction)
    iDelta = len(lTokens) - len(lNewTokens)
    lNewTokens = remove_close_paren(lNewTokens, dAction, iDelta)
    oViolation.set_tokens(lNewTokens)


def remove_close_paren(lTokens, dAction, iDelta):
    lReturn = []
    for iToken, oToken in enumerate(lTokens):
        if iToken + iDelta not in dAction['right_remove']:
            lReturn.append(oToken)
    lReturn.extend(dAction['right_insert'])
    return lReturn


def remove_open_paren(lTokens, dAction):
    lReturn = []
    lReturn.extend(dAction['left_insert'])
    for iToken, oToken in enumerate(lTokens):
        if iToken not in dAction['left_remove']:
            lReturn.append(oToken)
    return lReturn


def add_enclosing_parens(oViolation):
    lTokens = oViolation.get_tokens()
    dAction = oViolation.get_action()
    rules_utils.insert_token(lTokens, 0, parser.open_parenthesis())
    lTokens.append(parser.close_parenthesis())
    oViolation.set_tokens(lTokens)


def check_insert_parenthesis(self, oToi):
    lTokens = oToi.get_tokens()
    if not enclosing_parens_found(lTokens):
        oViolation = create_insert_violation(oToi)
        self.add_violation(oViolation)


def create_insert_violation(oToi):
    sSolution = 'Enclose condition in ()\'s.'
    dAction = {}
    dAction['action'] = 'insert'
    oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
    oViolation.set_action(dAction)
    return oViolation


def check_remove_parenthesis(self, oToi):
    lTokens = oToi.get_tokens()
    if enclosing_parens_found(lTokens):
        oViolation = create_remove_violation(oToi, lTokens)
        self.add_violation(oViolation)


def create_remove_violation(oToi, lTokens):
        sSolution = 'Remove enclosing ()\'s'
        dAction = create_remove_action_dict(lTokens)

        oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
        oViolation.set_action(dAction)
        return oViolation


def create_remove_action_dict(lTokens):
        dAction = {}
        dAction['action'] = 'remove'
        analyze_open_paren_cases(lTokens, dAction)
        analyze_close_paren_cases(lTokens, dAction)
        return dAction


def enclosing_parens_found(lTokens):
    if condition_starts_with_parenthesis(lTokens) and condition_ends_with_parenthesis(lTokens):
        lParens = build_parenthesis_list(lTokens)
        lNewParens = remove_inner_parenthesis(lParens)

        if len(lNewParens) == 2 and parens_match(lParens, lNewParens):
            return True
    return False


def analyze_close_paren_cases(lTokens, dAction):

    iLength = len(lTokens)
    if close_paren_space(lTokens):
        dAction['right_remove'] = [iLength - 1]
        dAction['right_insert'] = []
    elif space_close_paren_space(lTokens):
        dAction['right_remove'] = [iLength - 1, iLength - 2]
        dAction['right_insert'] = []
    elif space_close_paren(lTokens):
        dAction['right_remove'] = [iLength - 2]
        dAction['right_insert'] = []
    else:
        dAction['right_remove'] = [iLength - 1]
        dAction['right_insert'] = [parser.whitespace(' ')]


def analyze_open_paren_cases(lTokens, dAction):
    if open_paren_space(lTokens):
        dAction['left_remove'] = [0]
        dAction['left_insert'] = []
    elif space_open_paren_space(lTokens):
        dAction['left_remove'] = [0, 1]
        dAction['left_insert'] = []
    elif space_open_paren(lTokens):
        dAction['left_remove'] = [1]
        dAction['left_insert'] = []
    else:
        dAction['left_remove'] = [0]
        dAction['left_insert'] = [parser.whitespace(' ')]


def open_paren_space(lTokens):
    if isinstance(lTokens[0], parser.open_parenthesis) and isinstance(lTokens[1], parser.whitespace):
        return True
    return False


def space_open_paren_space(lTokens):
    if isinstance(lTokens[0], parser.whitespace) and isinstance(lTokens[1], parser.open_parenthesis) and isinstance(lTokens[2], parser.whitespace):
        return True
    return False


def space_open_paren(lTokens):
    if isinstance(lTokens[0], parser.whitespace) and isinstance(lTokens[1], parser.open_parenthesis):
        return True
    return False


def insert_parenthesis(option):
    if option == 'insert':
        return True
    return False


def close_paren_space(lTokens):
    if isinstance(lTokens[-1], parser.close_parenthesis) and isinstance(lTokens[-2], parser.whitespace):
        return True
    return False


def space_close_paren_space(lTokens):
    if isinstance(lTokens[-1], parser.whitespace) and isinstance(lTokens[-2], parser.close_parenthesis) and isinstance(lTokens[-3], parser.whitespace):
        return True
    return False


def space_close_paren(lTokens):
    if isinstance(lTokens[-1], parser.whitespace) and isinstance(lTokens[-2], parser.close_parenthesis):
        return True
    return False


def build_parenthesis_list(lTokens):
    lParens = []
    for oToken in lTokens:
       if isinstance(oToken, parser.open_parenthesis):
           lParens.append(oToken)
       elif isinstance(oToken, parser.close_parenthesis):
           lParens.append(oToken)
    return lParens


def remove_inner_parenthesis(lParens):
#    print('--> remove_inner_parenthesis [' + '-'*80)
#    print(f'lParens = {lParens}')
    lNewParens = []
    bSkipCloseParen = False
    if len(lParens) <= 2:
#        print('<-- remove_inner_parenthesis::lParens <= 2 [' + '-'*80)
        return lParens

    for iParen, oParen in enumerate(lParens[:-1]):
        if bSkipCloseParen:
           bSkipCloseParen = False
           continue
        if isinstance(oParen, parser.open_parenthesis) and isinstance(lParens[iParen + 1], parser.close_parenthesis):
            bSkipCloseParen = True
            continue
        lNewParens.append(oParen)
    if isinstance(lParens[-2], parser.close_parenthesis) and isinstance(lParens[-1], parser.close_parenthesis):
       lNewParens.append(lParens[-1])

#    print(f'lNewParens = {lNewParens}')
    lReturnParens = remove_inner_parenthesis(lNewParens)
#    print(f'lReturnParens = {lReturnParens}')
#    print('<-- remove_inner_parenthesis [' + '-'*80)
    return lReturnParens


def parens_match(lParens, lNewParens):
    if lParens[0] == lNewParens[0] and lParens[-1] == lNewParens[-1]:
        return True
    return False


def missing_enclosed_parens(lParens, lNewParens):
    if len(lNewParens) == 0:
        return True
    if not parens_match(lParens, lNewParens):
        return True
    return False


def condition_starts_with_parenthesis(lTokens):
    if isinstance(lTokens[0], parser.open_parenthesis):
        return True
    elif isinstance(lTokens[1], parser.open_parenthesis):
        return True
    return False


def condition_ends_with_parenthesis(lTokens):
    if isinstance(lTokens[-1], parser.close_parenthesis):
        return True
    elif isinstance(lTokens[-2], parser.close_parenthesis):
        return True
    return False
