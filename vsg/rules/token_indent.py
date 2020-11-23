

from vsg import rule
from vsg import utils
from vsg import parser

from vsg import violation


class token_indent(rule.Rule):
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

    def __init__(self, name, identifier, lTokens):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 4
        self.lTokens = lTokens

    def analyze(self, oFile):
        lToi = oFile.get_tokens_at_beginning_of_line_matching(self.lTokens)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if len(lTokens) == 2 and lTokens[1].get_indent() == 0:
                sSolution = "Indent level 0"
                oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                oViolation.set_action('remove_whitespace')
                self.add_violation(oViolation)
            elif len(lTokens) == 2:
                iWhitespace = len(lTokens[0].get_value())
                iIndent = self.indentSize * lTokens[1].get_indent()
                if iWhitespace != iIndent:
                    sSolution = 'Indent level ' + str(lTokens[1].get_indent())
                    oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                    oViolation.set_action('adjust_whitespace')
                    self.add_violation(oViolation)
            elif len(lTokens) == 1:
                if lTokens[0].get_indent() != 0:
                    sSolution = 'Indent level ' + str(lTokens[0].get_indent())
                    oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                    oViolation.set_action('add_whitespace')
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

