
from vsg import parser
from vsg import rule
from vsg import token
from vsg import violation

from vsg.vhdlFile import utils


class rule_030(rule.Rule):
    '''
    Checks for single signal declarations on sensitivity list lines.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of parser object types
       object types to check the prefix

    lSuffixes: string list
       acceptable suffixes
    '''

    def __init__(self):
        rule.Rule.__init__(self, 'process', '030')
        self.solution = 'Compact sensitivity list to reduce the number of lines it uses.'
        self.phase = 1
        self.fixable = False

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by(token.process_statement.open_parenthesis, token.process_statement.close_parenthesis)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            lTokens = utils.remove_whitespace_from_token_list(lTokens)[1:-1]
            lNewList = []
            iSignals = 0
            oSignal = None
            for oToken in lTokens:
                if isinstance(oToken, token.sensitivity_list.comma):
                    lNewList.append(parser.todo('signal name'))
                    iSignals += 1
                    oSignal = None
                elif isinstance(oToken, parser.carriage_return):
                    if oSignal is not None:
                        lNewList.append(parser.todo('signal name'))
                        iSignals += 1
                    lNewList.append(oToken)
                else:
                    oSignal = parser.todo('signal name')

            if oSignal is not None and not isinstance(oToken, parser.carriage_return):
                lNewList.append(parser.todo('signal name'))
                iSignals += 1


            if iSignals > 1:
                for iToken, oToken in enumerate(lNewList):
                    if iToken == 0:
                        continue
                    if isinstance(lNewList[iToken - 1], parser.todo) and isinstance(oToken, parser.todo):
                        break
                else:
                    oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
                    self.add_violation(oViolation)
