
from vsg import rule
from vsg import violation


class token_case_in_range_bounded_by_tokens(rule.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    trigger : parser object type
       object type to apply the case check against
    '''

    def __init__(self, name, identifier, lTokens, oStart, oEnd):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 6
        self.case = 'lower'
        self.configuration.append('case')
        self.lTokens = lTokens
        self.oStart = oStart
        self.oEnd = oEnd

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching_in_range_bounded_by_tokens(self.lTokens, self.oStart, self.oEnd)

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
