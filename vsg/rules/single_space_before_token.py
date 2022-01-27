
from vsg import parser
from vsg import violation

from vsg.rule_group import whitespace
from vsg.rules import utils


class single_space_before_token(whitespace.Rule):
    '''
    Checks for a single space before a token.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : token type object list
       A list of tokens to check for a single space before.
    '''

    def __init__(self, name, identifier, lTokens):
        whitespace.Rule.__init__(self, name=name, identifier=identifier)
        self.lTokens = lTokens

    def _get_tokens_of_interest(self, oFile):
        lToi = oFile.get_token_and_n_tokens_before_it(self.lTokens, 2)
        lReturn = remove_toi_that_begins_a_line(lToi)
        return lReturn

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if not whitespace_exists_before_token(lTokens):
                oViolation = create_insert_violation(oToi)
                self.add_violation(oViolation)
            elif utils.whitespace_is_larger_than_a_single_character(lTokens):
                oViolation = create_adjust_violation(oToi)
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        sAction = oViolation.get_action()
        if sAction == 'insert':
            utils.insert_whitespace(lTokens, 2)
        elif sAction == 'adjust':
            lTokens[1].set_value(' ')
        oViolation.set_tokens(lTokens)


def whitespace_exists_before_token(lTokens):
    if isinstance(lTokens[1], parser.whitespace):
        return True
    return False


def create_insert_violation(oToi):
    return create_violation(oToi, 'insert')


def create_adjust_violation(oToi):
    return create_violation(oToi, 'adjust')


def create_violation(oToi, sAction):
    lTokens = oToi.get_tokens()
    sSolution = 'Ensure a single space before ' + lTokens[2].get_value()
    oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
    oViolation.set_action(sAction)
    return oViolation


def remove_toi_that_begins_a_line(lToi):
    lReturn = []
    for oToi in lToi:
        lTokens = oToi.get_tokens()
        if not token_begins_a_line(lTokens):
            lReturn.append(oToi)
    return lReturn


def token_begins_a_line(lTokens):
    if isinstance(lTokens[0], parser.carriage_return) and isinstance(lTokens[1], parser.whitespace):
        return True
    if isinstance(lTokens[1], parser.carriage_return):
        return True
    return False
