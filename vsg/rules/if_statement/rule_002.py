
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
        return oFile.get_if_statement_conditions()

    def _analyze(self, lToi):
        for oToi in lToi:
            if insert_parenthesis(self.parenthesis):
                self._check_insert_parenthesis(oToi)
            else:
                self._check_remove_parenthesis(oToi)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        if insert_parenthesis(dAction['action']):
            rules_utils.insert_token(lTokens, 0, parser.open_parenthesis())
            lTokens.append(parser.close_parenthesis())
            oViolation.set_tokens(lTokens)
        else:
            lNewTokens = lTokens[1:-1]
            oViolation.set_tokens(lNewTokens)

    def _check_insert_parenthesis(self, oToi):
        lTokens = oToi.get_tokens()
        if (not isinstance(lTokens[0], parser.open_parenthesis) or
                not isinstance(lTokens[-1], parser.close_parenthesis)):
            sSolution = 'Enclose condition in ()\'s.'
            dAction = {}
            dAction['action'] = 'insert'
            oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
            oViolation.set_action(dAction)
            self.add_violation(oViolation)
        else:
            lParens = build_parenthesis_list(lTokens)
            lNewParens = remove_inner_parenthesis(lParens)
            if missing_enclosed_parens(lParens, lNewParens):
                sSolution = 'Enclose condition in ()\'s.'
                dAction = {}
                dAction['action'] = 'insert'
                oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                oViolation.set_action(dAction)
                self.add_violation(oViolation)

    def _check_remove_parenthesis(self, oToi):
        lTokens = oToi.get_tokens()
        if (isinstance(lTokens[0], parser.open_parenthesis) and
                isinstance(lTokens[-1], parser.close_parenthesis)):
            lParens = build_parenthesis_list(lTokens)
            lNewParens = remove_inner_parenthesis(lParens)

            if len(lNewParens) == 2:
                if parens_match(lParens, lNewParens):
                    sSolution = 'Remove enclosing ()\'s'
                    dAction = {}
                    dAction['action'] = 'remove'
                    oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                    oViolation.set_action(dAction)
                    self.add_violation(oViolation)


def insert_parenthesis(option):
    if option == 'insert':
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
