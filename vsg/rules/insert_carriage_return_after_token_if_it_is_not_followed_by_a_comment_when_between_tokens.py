

from vsg import parser
from vsg import rule_item
from vsg import violation

from vsg.vhdlFile import utils


class insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens(rule_item.Rule):
    '''
    Checks for a single space between two tokens.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    token : token object type
       The token to insert a carriage return after.

    oStart : token object type
       The starting token which defines the range

    oEnd : token object type
       The ending token which defines the range
    '''

    def __init__(self, name, identifier, lTokens, oStart, oEnd):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.lTokens = lTokens
        self.oStart = oStart
        self.oEnd = oEnd

    def analyze(self, oFile):

        lToi = oFile.get_token_and_n_tokens_after_it_when_between_tokens(self.lTokens, 2, self.oStart, self.oEnd)
        for oToi in lToi:
           lTokens = oToi.get_tokens()
           if utils.are_next_consecutive_token_types([parser.carriage_return], 1, lTokens):
               continue
           if utils.are_next_consecutive_token_types([parser.whitespace, parser.comment], 1, lTokens):
               continue
           if utils.are_next_consecutive_token_types([parser.comment, parser.carriage_return], 1, lTokens):
               continue
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
