
from vsg import parser
from vsg import token
from vsg import violation

from vsg.rules import utils as rules_utils
from vsg.rule_group import structure
from vsg.vhdlFile import utils

lMoveTokens = []
lMoveTokens.append(token.conditional_expressions.else_keyword)
lMoveTokens.append(token.conditional_waveforms.else_keyword)

lTokenPairs = []
lTokenPairs.append([token.conditional_force_assignment.assignment, token.conditional_force_assignment.semicolon])
lTokenPairs.append([token.conditional_variable_assignment.assignment, token.conditional_variable_assignment.semicolon])
lTokenPairs.append([token.concurrent_conditional_signal_assignment.assignment, token.concurrent_conditional_signal_assignment.semicolon])
lTokenPairs.append([token.conditional_waveform_assignment.assignment, token.conditional_waveform_assignment.semicolon])


class rule_001(structure.Rule):
    '''
    This rule checks the **else** keyword is not at the beginning of a line.
    The else should be at the end of the preceeding line.

    **Violation**

    .. code-block:: vhdl

       wr_en <= '1' when a = '1' -- This is comment
                else '0' when b = '0'
                else c when d = '1'
                else f;

    **Fix**

    .. code-block:: vhdl

       wr_en <= '1' when a = '1' else -- This is a comment
                '0' when b = '0' else
                c when d = '1' else
                f;
    '''

    def __init__(self):
        structure.Rule.__init__(self, 'when', '001')
        self.lMoveTokens = lMoveTokens
        self.lTokenPairs = lTokenPairs

    def _get_tokens_of_interest(self, oFile):
        lToi = []
        for lTokenPair in self.lTokenPairs:
            aToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1])
            lToi = utils.combine_two_token_class_lists(lToi, aToi)
        return lToi

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iLine = oToi.get_line_number()
            oAnchorToken = None
            iMoveToLine = None
            iLeft = None

            for iToken, oToken in enumerate(lTokens):
                iLine = utils.increment_line_number(iLine, oToken)
                for oMoveToken in self.lMoveTokens:
                    if isinstance(oToken, oMoveToken):
                        if lTokens[iToken - 2] is not oAnchorToken or \
                           lTokens[iToken - 2] is oAnchorToken and isinstance(lTokens[iToken - 1], parser.carriage_return):
                            self.solution = 'Move "' + oToken.get_value() + '" to the right of "' + oAnchorToken.get_value() + '" on line ' + str(iMoveToLine)
                            if isinstance(lTokens[iToken + 1], parser.whitespace):
                                iRight = iToken + 1
                            else:
                                iRight = iToken
                            oViolation = violation.New(iLine, oToi.extract_tokens(iLeft, iRight), self.solution)
                            self.add_violation(oViolation)
                            break
                if not utils.token_is_whitespace_or_comment(oToken):
                    iLeft = iToken + 1
                    iMoveToLine = iLine
                    oAnchorToken = oToken

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if isinstance(lTokens[-1], parser.whitespace):
            lTokens.pop()
        oToken = lTokens.pop()
        rules_utils.insert_token(lTokens, 0, oToken)
        rules_utils.insert_whitespace(lTokens, 0)
        oViolation.set_tokens(lTokens)
