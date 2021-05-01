
from vsg import parser
from vsg import rule
from vsg import violation

from vsg.rules import utils as rules_utils


class single_space_after_token(rule.Rule):
    '''
    Checks for a single space between two tokens.

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
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 2
        self.lTokens = lTokens

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_token_and_n_tokens_after_it(self.lTokens, 1)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if isinstance(lTokens[1], parser.carriage_return):
                continue
            if not isinstance(lTokens[1], parser.whitespace):
                sSolution = 'Ensure a single space after ' + lTokens[0].get_value()
                oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                oViolation.set_action('insert')
                self.add_violation(oViolation)
            else:
                if lTokens[1].get_value() != ' ':
                    sSolution = 'Ensure a single space after ' + lTokens[0].get_value()
                    oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                    oViolation.set_action('adjust')
                    self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        sAction = oViolation.get_action()
        if sAction == 'insert':
            rules_utils.insert_whitespace(lTokens, 1)
        elif sAction == 'adjust':
            lTokens[1].set_value(' ')
        oViolation.set_tokens(lTokens)
