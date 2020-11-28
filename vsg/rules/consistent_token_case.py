
from vsg import rule
from vsg import parser
from vsg import violation

from vsg.vhdlFile import utils


class consistent_token_case(rule.Rule):
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

    def __init__(self, name, identifier, lTokens, lIgnore=[]):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 6
        self.subphase = 2
        self.lTokens = lTokens
        self.lIgnoreTokens = lIgnore

    def analyze(self, oFile):
        lTargetTypes = oFile.get_tokens_matching(self.lTokens)
        oToi = oFile.get_all_tokens()
        iLine, lTokens = utils.get_toi_parameters(oToi)

        for iToken, oToken in enumerate(lTokens):

            iLine = utils.increment_line_number(iLine, oToken)

            if is_token_in_ignore_token_list(oToken, self.lIgnoreTokens):
                continue

            for oTargetType in lTargetTypes:
                sTokenValue = oToken.get_value()
                sTargetType = oTargetType.get_tokens()[0].get_value()
                if sTokenValue.lower() == sTargetType.lower():
                    if sTokenValue != sTargetType:
                        sSolution = 'Change "' + sTokenValue + '" to "' + sTargetType + '"'
                        oNewToi = oToi.extract_tokens(iToken, iToken)
                        oViolation = violation.New(iLine, oNewToi, sSolution)
                        dAction = {}
                        dAction['constant'] = sTargetType
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
