

from vsg import rule_item
from vsg import utils
from vsg import parser

from vsg import violation


class consistent_token_case(rule_item.Rule):
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
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 6
        self.subphase = 2
        self.lTokens = lTokens
        self.lIgnoreTokens = lIgnore

    def analyze(self, oFile):
        lTargetTypes = oFile.get_tokens_matching(self.lTokens)
        lToi = oFile.get_tokens_matching([parser.item])
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            for oToken in lTokens:

                if is_token_in_ignore_token_list(oToken, self.lIgnoreTokens):
                    continue

                for oTargetType in lTargetTypes:
                    sTokenValue = oToken.get_value()
                    sTargetType = oTargetType.get_tokens()[0].get_value()
                    if sTokenValue.lower() == sTargetType.lower():
                        if sTokenValue != sTargetType:
                            sSolution = 'Change "' + sTokenValue + '" to "' + sTargetType + '"'
                            oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                            dAction = {}
                            dAction['constant'] = sTargetType
                            dAction['found'] = sTokenValue
                            oViolation.set_action(dAction)
                            self.add_violation(oViolation)

    def fix(self, oFile):
        '''
        Applies fixes for any rule violations.
        '''
        if self.fixable:
            self.analyze(oFile)
            self._print_debug_message('Fixing rule: ' + self.name + '_' + self.identifier)
            self._fix_violation(oFile)
            self.violations = []

    def _fix_violation(self, oFile):
        for oViolation in self.violations:
            lTokens = oViolation.get_tokens()
            dActions = oViolation.get_action()
            lTokens[0].set_value(dActions['constant'])
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)


def is_token_in_ignore_token_list(oToken, lIgnoreTokens):
    for oIgnoreToken in lIgnoreTokens:
        if isinstance(oToken, oIgnoreToken):
            return True
    return False
