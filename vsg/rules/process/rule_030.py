
from vsg import parser
from vsg import token
from vsg import violation

from vsg.vhdlFile import utils
from vsg.rule_group import structure


class rule_030(structure.Rule):
    '''
    This rule checks for a single signal per line in a sensitivity list that is not the last one.
    The sensitivity list is required by the compiler, but provides no useful information to the reader.
    Therefore, the vertical spacing of the sensitivity list should be minimized.
    This will help with code readability.

    .. NOTE::  This rule is left to the user to fix.

    **Violation**

    .. code-block:: vhdl

       proc_a : process (rd_en,
                         wr_en,
                         data_in,
                         data_out,
                         rd_full,
                         wr_full
                        )

    **Fix**

    .. code-block:: vhdl

       proc_a : process (rd_en, wr_en, data_in, data_out,
                         rd_full, wr_full
                        )
    '''

    def __init__(self):
        structure.Rule.__init__(self, 'process', '030')
        self.solution = 'Compact sensitivity list to reduce the number of lines it uses.'
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
