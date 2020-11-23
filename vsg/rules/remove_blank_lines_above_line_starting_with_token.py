

from vsg import parser
from vsg import rule
from vsg import violation

from vsg.vhdlFile import utils


class remove_blank_lines_above_line_starting_with_token(rule.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    token : token list
       reference tokens to remove blank lines above
    '''

    def __init__(self, name, identifier, lTokens):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 3
        self.lTokens = lTokens

    def analyze(self, oFile):

        lToi = oFile.get_consecutive_lines_starting_with_token_and_stopping_when_token_starting_line_is_found(parser.blank_line, self.lTokens[0])
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLine = oToi.get_line_number()

            iTargetIndent = lTokens[-1].get_indent()
            iWhitespaceLength = iTargetIndent * self.indentSize

            for iIndex in range(0, len(lTokens)):
               oToken = lTokens[iIndex]

               if isinstance(oToken, parser.carriage_return):
                   iLine += 1
                   for oSearchToken in self.lTokens:
                       if utils.are_next_consecutive_token_types([parser.whitespace, oSearchToken], iIndex + 1, lTokens) or \
                          utils.are_next_consecutive_token_types([oSearchToken], iIndex + 1, lTokens):
                           oViolation = violation.New(iLine, oToi, self.solution)
                           dAction = {}
                           dAction['remove_to_index'] = iIndex + 1
                           oViolation.set_action(dAction)
                           self.violations.append(oViolation)


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
            dAction = oViolation.get_action()
            lMyTokens = lTokens[dAction['remove_to_index']:]
            oViolation.set_tokens(lMyTokens)
        oFile.update(self.violations)

