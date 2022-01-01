
from vsg.rule_group import case
from vsg import violation

lKeywords = []
lKeywords.append('std_logic')
lKeywords.append('std_logic_vector')
lKeywords.append('integer')
lKeywords.append('signed')
lKeywords.append('unsigned')
lKeywords.append('natural')
lKeywords.append('std_ulogic')


class token_case_n_token_after_tokens_between_tokens(case.Rule):
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

    def __init__(self, name, identifier, iToken, lTokens, oStart, oEnd, bLimitToVhdlKeywords=False):
        case.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 6
        self.case = 'lower'
        self.configuration.append('case')
        self.iToken = iToken
        self.lTokens = lTokens
        self.oStart = oStart
        self.oEnd = oEnd
        self.disabled = False
        self.bLimitToVhdlKeywords = bLimitToVhdlKeywords

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_n_token_after_tokens_between_tokens(self.iToken, self.lTokens, self.oStart, self.oEnd)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            sObjectValue = lTokens[0].get_value()
            if self.bLimitToVhdlKeywords:
                if sObjectValue.lower() not in lKeywords:
                    continue
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
