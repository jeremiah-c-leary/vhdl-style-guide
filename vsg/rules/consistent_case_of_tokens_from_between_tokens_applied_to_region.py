
from vsg import violation

from vsg.vhdlFile import utils
from vsg.rule_group import case


class consistent_case_of_tokens_from_between_tokens_applied_to_region(case.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens: list of token type objects
       token type to apply the case check against
    '''

    def __init__(self, name, identifier, lTokens, oStart, oEnd, oRegionStart, oRegionEnd, lIgnore=None):
        case.Rule.__init__(self, name=name, identifier=identifier)
        self.subphase = 2
        self.lTokens = lTokens
        self.oStart = oStart
        self.oEnd = oEnd
        self.oRegionStart = oRegionStart
        self.oRegionEnd = oRegionEnd
        if lIgnore is None:
            self.lIgnoreTokens = []
        else:
            self.lIgnoreTokens = lIgnore

    def analyze(self, oFile):
        self._print_debug_message('Analyzing rule: ' + self.unique_id)

        lTargetTypes = oFile.get_tokens_matching_in_range_bounded_by_tokens(self.lTokens, self.oStart, self.oEnd)
        lTargetValues = []
        lTargetValuesLower = []
        for oTargetType in lTargetTypes:
            oToken = oTargetType.get_tokens()[0]
            lTargetValues.append(oToken.get_value())
            lTargetValuesLower.append(oToken.get_value().lower())

        lToi = oFile.get_tokens_bounded_by(self.oRegionStart, self.oRegionEnd)

        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)

            for iToken, oToken in enumerate(lTokens):

                iLine = utils.increment_line_number(iLine, oToken)

                if is_token_in_ignore_token_list(oToken, self.lIgnoreTokens):
                    continue

                sTokenValue = oToken.get_value()
                sTokenValueLower = sTokenValue.lower()

                for sTargetValue, sTargetValueLower in zip(lTargetValues, lTargetValuesLower):
                    if sTokenValueLower == sTargetValueLower:
                        if sTokenValue != sTargetValue:
                            sSolution = 'Change "' + sTokenValue + '" to "' + sTargetValue + '"'
                            oNewToi = oToi.extract_tokens(iToken, iToken)
                            oViolation = violation.New(iLine, oNewToi, sSolution)
                            dAction = {}
                            dAction['constant'] = sTargetValue
                            dAction['found'] = sTokenValue
                            oViolation.set_action(dAction)
                            self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dActions = oViolation.get_action()
        lTokens[0].set_value(dActions['constant'])
        oViolation.set_tokens(lTokens)


def is_token_in_ignore_token_list(oToken, lIgnoreTokens):
    for oIgnoreToken in lIgnoreTokens:
        if isinstance(oToken, oIgnoreToken):
            return True
    return False
