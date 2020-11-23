
from vsg import rule
from vsg import violation

from vsg.token import port_clause as token
from vsg.token import mode


class rule_023(rule.Rule):
    '''
    Checks for the existance of port modes.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    trigger : parser object type
       object type to apply the case check against
    '''

    def __init__(self):
        rule.Rule.__init__(self, name='port', identifier='023')
        self.solution = 'Add mode'
        self.phase = 1 
        self.fixable = False

    def analyze(self, oFile):
        lToi = oFile.get_interface_elements_between_tokens(token.open_parenthesis, token.close_parenthesis)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            for oToken in lTokens:
                if isinstance(oToken, mode.mode):
                    break
            else:
                self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))

    def fix(self, oFile):
        '''
        Applies fixes for any rule violations.
        '''
        return None
