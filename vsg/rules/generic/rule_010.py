
from vsg import parser
from vsg import rule
from vsg import token
from vsg import violation

from vsg.rules import utils as rules_utils

from vsg.vhdlFile import utils

lTokens = []
lTokens.append(token.generic_clause.close_parenthesis)


class rule_010(rule.Rule):
    '''
    Moves code after the ) to the next line.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of parser object types
       object type to split a line at
    '''

    def __init__(self):
        rule.Rule.__init__(self, 'generic', '010')
        self.solution = 'Closing parenthesis must be on a line by itself.'
        self.phase = 1
        self.lTokens = lTokens

    def analyze(self, oFile):
        aToi = oFile.get_tokens_bounded_by(token.generic_clause.close_parenthesis, parser.carriage_return)
        lToi = oFile.get_token_and_n_tokens_before_it([token.generic_clause.close_parenthesis], 2)
        for iToi, oToi in enumerate(lToi):

            lTokens = oToi.get_tokens()

            if isinstance(lTokens[0], parser.carriage_return) or isinstance(lTokens[1], parser.carriage_return):
                continue

            sSolution = self.solution
            dAction = {}

            if utils.does_token_type_exist_in_list_of_tokens(parser.comment, aToi[iToi].get_tokens()):
                lNewTokens = aToi[iToi].get_tokens()
                for iToken, oToken in enumerate(lNewTokens):
                    if isinstance(oToken, parser.comment):
                        dAction['action'] = 'move'
                        if isinstance(lNewTokens[iToken - 1], parser.whitespace):
                            dAction['index'] = iToken - 2
                        else:
                            dAction['index'] = iToken - 1
                        break
            else:
                dAction['action'] = 'insert'

            oViolation = violation.New(aToi[iToi].get_line_number(), aToi[iToi], sSolution)
            oViolation.set_action(dAction)
            self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        if dAction['action'] == 'insert':
            rules_utils.insert_carriage_return(lTokens, 0)
            oViolation.set_tokens(lTokens)
        else:
            lNewTokens = lTokens[dAction['index'] + 1:]
            rules_utils.append_carriage_return(lNewTokens)
            lNewTokens.extend(lTokens[:dAction['index'] + 1])
            oViolation.set_tokens(lNewTokens)
