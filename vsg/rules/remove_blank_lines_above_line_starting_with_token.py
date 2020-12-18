

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

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_consecutive_lines_starting_with_token_and_stopping_when_token_starting_line_is_found(parser.blank_line, self.lTokens[0])

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLine = oToi.get_line_number()

            for iToken, oToken in enumerate(lTokens):
               if isinstance(oToken, parser.carriage_return):
                   iLine += 1
                   for oSearchToken in self.lTokens:
                       if utils.are_next_consecutive_token_types([parser.whitespace, oSearchToken], iToken + 1, lTokens) or \
                          utils.are_next_consecutive_token_types([oSearchToken], iToken + 1, lTokens):
                           oViolation = violation.New(iLine, oToi, self.solution)
                           dAction = {}
                           dAction['remove_to_index'] = iToken + 1
                           oViolation.set_action(dAction)
                           self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        lMyTokens = lTokens[dAction['remove_to_index']:]
        oViolation.set_tokens(lMyTokens)
