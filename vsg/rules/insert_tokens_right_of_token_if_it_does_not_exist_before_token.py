

from vsg import parser
from vsg import violation

from vsg.vhdlFile import utils
from vsg.rule_group import structure


class insert_tokens_right_of_token_if_it_does_not_exist_before_token(structure.Rule):
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

    anchor_token : token object type
       token to check if insert_token exists to the right of

    end_token : token object type
       token that bounds the search for the insert_token
    '''

    def __init__(self, name, identifier, insert_tokens, anchor_token, end_token):
        structure.Rule.__init__(self, name=name, identifier=identifier)
        self.insert_tokens = insert_tokens
        self.anchor_token = anchor_token
        self.end_token = end_token
        self.action = 'add'
        self.configuration.append('action')

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by(self.anchor_token, self.end_token)

    def _analyze(self, lToi):
        if self.action == 'add':
            for oToi in lToi:
                lTokens = oToi.get_tokens()

                for oToken in lTokens:
                    if isinstance(oToken, type(self.insert_tokens[0])):
                        break
                else:
                    sSolution = self.action.capitalize() + ' ' + self.solution
                    self.add_violation(violation.New(oToi.get_line_number(), oToi, sSolution))
        else:
            for oToi in lToi:
                lTokens = oToi.get_tokens()
                for iToken, oToken in enumerate(lTokens):
                    if isinstance(oToken, type(self.insert_tokens[0])):
                        sSolution = self.action.capitalize() + ' ' + self.solution
                        dAction = {}
                        dAction['iStartIndex'] = iToken
                        dAction['iEndIndex'] = iToken + len(self.insert_tokens)
                        oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                        oViolation.set_action(dAction)
                        self.add_violation(oViolation)
                        break

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if self.action == 'add':
            lNewTokens = []
            lNewTokens.append(lTokens[0])
            if isinstance(lTokens[1], parser.whitespace) and isinstance(lTokens[2], parser.semicolon):
                lNewTokens.append(lTokens[1])
                lNewTokens.extend(self.insert_tokens)
                lNewTokens.extend(lTokens[2:])
            else:
                lNewTokens.append(parser.whitespace(' '))
                lNewTokens.extend(self.insert_tokens)
                lNewTokens.extend(lTokens[1:])
        else:
            dAction = oViolation.get_action()
            lNewTokens = lTokens[:dAction['iStartIndex']]
            lNewTokens.extend(lTokens[dAction['iEndIndex']:])
            lNewTokens = utils.remove_consecutive_whitespace_tokens(lNewTokens)
        oViolation.set_tokens(lNewTokens)
