

from vsg import parser
from vsg import rule_item
from vsg import violation


class insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token(rule_item.Rule):
    '''
    Checks for the existence of a token and will insert it if it does not exist.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    insert_token : token object
       token to insert if it does not exist.

    anchor_token : token object
       token to check if insert_token exists to the right of

    value_token : token object
       token to pull the value from
    '''

    def __init__(self, name, identifier, insert_token, anchor_token, left_token, right_token, value_token):
        rule_item.Rule.__init__(self, name=name, identifier=identifier)
        self.solution = None
        self.phase = 1
        self.insert_token = insert_token
        self.anchor_token = anchor_token
        self.left_token = left_token
        self.right_token = right_token
        self.value_token = value_token

    def analyze(self, oFile):
        lToi = oFile.get_tokens_between_tokens_inclusive_while_storing_value_from_token(self.left_token, self.right_token, self.value_token)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            bFound = False
            iLine = oToi.get_line_number()
            for oToken in lTokens:
               if isinstance(oToken, parser.carriage_return):
                   iLine += 1
               if isinstance(oToken, self.insert_token):
                   bFound = True
                   break
            if not bFound:
                self.add_violation(violation.New(iLine, oToi, self.solution))

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
            for iIndex in range(0, len(lTokens)):
                if isinstance(lTokens[iIndex], self.anchor_token):
                    lTokens.insert(iIndex, self.insert_token(oViolation.get_token_value()))
                    lTokens.insert(iIndex, parser.whitespace(' '))
            oViolation.set_tokens(lTokens)
        oFile.update(self.violations)
