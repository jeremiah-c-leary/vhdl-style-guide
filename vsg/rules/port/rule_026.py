
from vsg import parser
from vsg import rule
from vsg import violation

from vsg.token import port_clause as token
from vsg.token import interface_unknown_declaration
from vsg.token import interface_list


class rule_026(rule.Rule):
    '''
    Checks for multiple instances of identifiers in port declarations.

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
        rule.Rule.__init__(self, name='port', identifier='026')
        self.phase = 1
        self.subphase = 2

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_interface_elements_between_tokens(token.open_parenthesis, token.close_parenthesis)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iCount = 0
            lIdentifiers = []
            lIdentifierIndexes = []
            for iToken, oToken in enumerate(lTokens):
                if isinstance(oToken, interface_unknown_declaration.identifier):
                    lIdentifiers.append(oToken.get_value())
                    iCount += 1
                    lIdentifierIndexes.append(iToken)
            if iCount > 1:
                sSolution = 'Split identifiers ' + ', '.join(lIdentifiers) + ' to individual lines.'
                dAction = {}
                if oToi == lToi[-1]:
                    dAction['last_element'] = False
                else:
                    dAction['last_element'] = True
                dAction['identifier_indexes'] = lIdentifierIndexes
                dAction['split_index'] = lIdentifierIndexes[-1] + 1
                oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                oViolation.set_action(dAction)
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        '''
        Applies fixes for any rule violations.
        '''
        lTokens = oViolation.get_tokens()
        lNewTokens = []
        dAction = oViolation.get_action()
        for iIndex in dAction['identifier_indexes']:
            lNewTokens.append(lTokens[iIndex])

            lNewTokens.extend(lTokens[dAction['split_index']:])
            if iIndex != dAction['identifier_indexes'][-1]:
                lNewTokens.append(interface_list.semicolon())
                lNewTokens.append(parser.carriage_return())
        oViolation.set_tokens(lNewTokens)
