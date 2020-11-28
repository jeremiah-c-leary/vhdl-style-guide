
from vsg import rule
from vsg import violation


class token_case(rule.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of token types
       The token types to check the case on.
    '''

    def __init__(self, name, identifier, lTokens):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 6
        self.case = 'lower'
        self.configuration.append('case')
        self.lTokens = lTokens

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching(self.lTokens)

    def _analyze(self, lToi):
        for oToi in lToi:
            sObjectValue = oToi.get_tokens()[0].get_value()
            if self.case == 'lower':
                if not sObjectValue.islower():
                    sSolution = 'Change "' + sObjectValue + '" to "' + sObjectValue.lower() + '"'
                    self.add_violation(violation.New(oToi.get_line_number(), oToi, sSolution))
            if self.case == 'upper':
                if not sObjectValue.isupper():
                    sSolution = 'Change "' + sObjectValue + '" to "' + sObjectValue.upper() + '"'
                    self.add_violation(violation.New(oToi.get_line_number(), oToi, sSolution))

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if self.case == 'lower':
            lTokens[0].set_value(lTokens[0].get_value().lower())
        if self.case == 'upper':
            lTokens[0].set_value(lTokens[0].get_value().upper())
        oViolation.set_tokens(lTokens)
