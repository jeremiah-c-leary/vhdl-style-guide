

from vsg import rule
from vsg import utils
from vsg import parser

from vsg import violation


class token_prefix(rule.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of parser object types
       object types to check the prefix

    lPrefixes : string list
       acceptable prefixes
    '''

    def __init__(self, name, identifier, lTokens):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 7
        self.lTokens = lTokens
        self.prefixes = None
        self.configuration.append('prefixes')
        self.fixable = False
        self.disable = True

    def analyze(self, oFile):
        lToi = oFile.get_tokens_matching(self.lTokens)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            sToken = lTokens[0].get_value().lower()
            bValid = False
            for sPrefix in self.prefixes:
                if sToken.startswith(sPrefix):
                    bValid = True
            if not bValid:
                sSolution = 'Prefix ' + lTokens[0].get_value() + ' with one of the following: ' + ', '.join(self.prefixes)
                oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
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
            if oViolation.get_action() == 'remove_whitespace':
                oViolation.set_tokens([lTokens[1]])
            elif oViolation.get_action() == 'adjust_whitespace':
                lTokens[0].set_value(lTokens[1].get_indent() * self.indentSize * ' ')
                oViolation.set_tokens(lTokens)
            elif oViolation.get_action() == 'add_whitespace':
                oToken = parser.whitespace(lTokens[0].get_indent() * self.indentSize * ' ')
                lTokens.insert(0, oToken)
                oViolation.set_tokens(lTokens)
               
        oFile.update(self.violations)

