
from vsg import rule
from vsg.rules import case_utils


class token_case_in_range_bounded_by_tokens(rule.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of token types

    oStart : token type

    oEnd : token type
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
        self.prefix_exceptions = []
        self.suffix_exceptions = []

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching_in_range_bounded_by_tokens(self.lTokens, self.oStart, self.oEnd)

    def _analyze(self, lToi):
        check_prefix = case_utils.is_exception_enabled(self.prefix_exceptions)
        check_suffix = case_utils.is_exception_enabled(self.suffix_exceptions)
        for oToi in lToi:
            oViolation = case_utils.check_for_case_violation(oToi, self, check_prefix, check_suffix)
            if oViolation is not None:
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        lTokens[0].set_value(dAction['value'])
        oViolation.set_tokens(lTokens)
