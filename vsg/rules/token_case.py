

from vsg import rule_item
from vsg import utils
from vsg import parser

from vsg import violation


class token_case(rule_item.Rule):
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

    def __init__(self, name, identifier, token):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 6
        self.case = 'lower'
        self.configuration.append('case')
        self.oToken = token

    def analyze(self, oFile):
        lTokens = oFile.get_tokens_matching([self.oToken])
        for oToken in lTokens:
            sObjectValue = oToken.get_tokens()[0].get_value()
            if self.case == 'lower':
                if not sObjectValue.islower():
                    sSolution = 'Change "' + sObjectValue + '" to "' + sObjectValue.lower() + '"'
                    self.add_violation(violation.New(oToken.get_line_number(), oToken, sSolution))
            if self.case == 'upper':
                if not sObjectValue.isupper():
                    sSolution = 'Change "' + sObjectValue + '" to "' + sObjectValue.upper() + '"'
                    self.add_violation(violation.New(oToken.get_line_number(), oToken, sSolution))


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
            if self.case == 'lower':
                lTokens[0].set_value(lTokens[0].get_value().lower())
            if self.case == 'upper':
                lTokens[0].set_value(lTokens[0].get_value().upper())
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)

