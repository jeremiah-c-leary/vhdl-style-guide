
from vsg.rule_group import case
from vsg.rules import case_utils

lKeywords = []
lKeywords.append('std_logic')
lKeywords.append('std_logic_vector')
lKeywords.append('integer')
lKeywords.append('signed')
lKeywords.append('unsigned')
lKeywords.append('natural')
lKeywords.append('std_ulogic')


class token_case_n_token_after_tokens(case.Rule):
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

    def __init__(self, name, identifier, iToken, lTokens, bLimitToVhdlKeywords=False):
        case.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 6
        self.case = 'lower'
        self.configuration.append('case')
        self.iToken = iToken
        self.lTokens = lTokens
        self.disabled = False
        self.bLimitToVhdlKeywords = bLimitToVhdlKeywords
        self.prefix_exceptions = []
        self.suffix_exceptions = []

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_n_token_after_tokens(self.iToken, self.lTokens)

    def _analyze(self, lToi):
        check_prefix = case_utils.is_exception_enabled(self.prefix_exceptions)
        check_suffix = case_utils.is_exception_enabled(self.suffix_exceptions)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            sObjectValue = lTokens[0].get_value()
            if self.bLimitToVhdlKeywords:
                if sObjectValue.lower() not in lKeywords:
                    continue
            oViolation = case_utils.check_for_case_violation(oToi, self, check_prefix, check_suffix)
            if oViolation is not None:
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        lTokens[0].set_value(dAction['value'])
        oViolation.set_tokens(lTokens)
