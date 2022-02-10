
from vsg import parser
from vsg import violation

from vsg.rule_group import whitespace
from vsg.rules import utils


class single_space_after_token(whitespace.Rule):
    '''
    Checks for a single space after a token

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : token type object list
       A list of tokens to check for a single space after.
    '''

    def __init__(self, name, identifier, lTokens):
        whitespace.Rule.__init__(self, name=name, identifier=identifier)
        self.lTokens = lTokens

    def _get_tokens_of_interest(self, oFile):
        lToi = oFile.get_token_and_n_tokens_after_it(self.lTokens, 2)
        lToi = utils.remove_toi_if_token_is_at_the_end_of_the_line(lToi)
        return lToi

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if not whitespace_exists_after_token(lTokens):
                oViolation = create_violation(oToi, 'insert')
                self.add_violation(oViolation)
            elif utils.whitespace_is_larger_than_a_single_character(lTokens):
                oViolation = create_violation(oToi, 'adjust')
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        sAction = oViolation.get_action()
        if sAction == 'insert':
            utils.insert_whitespace(lTokens, 1)
        elif sAction == 'adjust':
            lTokens[1].set_value(' ')
        oViolation.set_tokens(lTokens)


def whitespace_exists_after_token(lTokens):
    if isinstance(lTokens[1], parser.whitespace):
        return True
    return False


def create_violation(oToi, sAdjust):
    lTokens = oToi.get_tokens()
    sSolution = 'Ensure a single space after ' + lTokens[0].get_value()
    oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
    oViolation.set_action(sAdjust)
    return oViolation
