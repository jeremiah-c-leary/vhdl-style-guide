
from vsg import rule
from vsg import parser
from vsg import token
from vsg import violation

lTokens = []
lTokens.append(token.interface_constant_declaration.assignment)
lTokens.append(token.interface_signal_declaration.assignment)
lTokens.append(token.interface_variable_declaration.assignment)
lTokens.append(token.interface_unknown_declaration.assignment)


class rule_012(rule.Rule):
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

    def __init__(self):
        rule.Rule.__init__(self, name='port', identifier='012')
        self.solution = 'Remove assignment'
        self.phase = 1
        self.lTokens = lTokens
        self.oStart = token.port_clause.open_parenthesis
        self.oEnd = token.port_clause.close_parenthesis
        self.fixable = False

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_interface_elements_between_tokens(self.oStart, self.oEnd)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            for iToken, oToken in enumerate(lTokens):
                for oSearchToken in self.lTokens:
                    if isinstance(oToken, oSearchToken):
                        oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
                        dAction = {}
                        if isinstance(lTokens[iToken - 1], parser.whitespace):
                            dAction['index'] = iToken - 1
                        else:
                            dAction['index'] = iToken
                        oViolation.set_action(dAction)
                        self.add_violation(oViolation)
                        break

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        for iIndex in range(dAction['index'], len(lTokens)):
            if isinstance(lTokens[iIndex], parser.comment):
                if isinstance(lTokens[iIndex - 1], parser.whitespace):
                    iEnd = iIndex - 1
                else:
                    iEnd = iIndex
                break
        else:
            iEnd = iIndex
        if iEnd + 1 == len(lTokens):
            lNewTokens = lTokens[:dAction['index']]
        else:
            lNewTokens = lTokens[:dAction['index']] + lTokens[iEnd:]
        oViolation.set_tokens(lNewTokens)
