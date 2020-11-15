

from vsg import parser
from vsg import rule_item
from vsg import violation

from vsg.vhdlFile import utils


class insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_and_not_on_same_line_as_token(rule_item.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    token : token object
       The token to insert a carriage return after.
    '''

    def __init__(self, name, identifier, token, oSameLineToken):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.token = token
        self.oSameLineToken = oSameLineToken

    def analyze(self, oFile):
        lToi = oFile.get_tokens_bounded_by(self.token, parser.carriage_return)
        for oToi in lToi:
           iLine, lTokens = utils.get_toi_parameters(oToi)
           if utils.are_next_consecutive_token_types([parser.carriage_return], 1, lTokens):
               continue
           if utils.are_next_consecutive_token_types([parser.whitespace, parser.comment, parser.carriage_return], 1, lTokens):
               continue
           if utils.are_next_consecutive_token_types([parser.comment, parser.carriage_return], 1, lTokens):
               continue
           for oToken in lTokens:
               iLine = utils.increment_line_number(iLine, oToken)
               if isinstance(oToken, self.token):
                   iTokenLine = iLine
               if isinstance(oToken, self.oSameLineToken):
                   if iTokenLine == iLine:
                       break
           else:
               self.violations.append(violation.New(oToi.get_line_number(), oToi, self.solution))


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
            lTokens.insert(1, parser.carriage_return())
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)
