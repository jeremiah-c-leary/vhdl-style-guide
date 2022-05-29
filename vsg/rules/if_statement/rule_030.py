
from vsg.rules import blank_line_below_line_ending_with_token

from vsg import parser
from vsg import token

lTokens = []
lTokens.append(token.if_statement.semicolon)


class rule_030(blank_line_below_line_ending_with_token):
    '''
    This rule checks a single blank line after the **end if**.
    In the case of nested **if** statements, the rule will be enfoced on the last **end if**.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       if (A = '1') then
         B <= '0';
       end if;
       C <= '1';

    **Fix**

    .. code-block:: vhdl

       if (A = '1') then
         B <= '0';
       end if;

       C <= '1';
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'if', '030', lTokens)
        self.lHierarchyLimits = [0]
        self.configuration.append('ignore_hierarchy')
        self.except_end_if = False
        self.configuration.append('except_end_if')
        self.except_end_process = False
        self.configuration.append('except_end_process')
        self.except_end_case = False
        self.configuration.append('except_end_case')
        self.except_end_loop = False
        self.configuration.append('except_end_loop')
        self.except_end_subprogram_body = False
        self.configuration.append('except_end_subprogram_body')

    def _get_tokens_of_interest(self, oFile):
        self._update_hierarchy_limits()

        if self.lHierarchyLimits is None:
            lToi = oFile.get_line_below_line_ending_with_token(self.lTokens, bIncludeCarriageReturn=True)
        else:
            lToi = oFile.get_line_below_line_ending_with_token_with_hierarchy(self.lTokens, self.lHierarchyLimits, bIncludeCarriageReturn=True)

        return self.set_style_in_toi_list(lToi, oFile)

    def set_style_in_toi_list(self, lToi, oFile):
        lReturn = []
        for oToi in lToi:
            oToi.style = self.style
            lReturn.append(oToi)

            self.update_style_per_exceptions(oToi, lReturn, oFile)

        return lReturn

    def update_style_per_exceptions(self, oToi, lReturn, oFile):
        if self.except_end_case:
            self.invert_style_if_token_detected(oToi, token.case_statement.end_keyword, lReturn, oFile)

        if self.except_end_process:
            self.invert_style_if_token_detected(oToi, token.process_statement.end_keyword, lReturn, oFile)

        if self.except_end_if:
            self.invert_style_if_token_detected(oToi, token.if_statement.end_keyword, lReturn, oFile)

        if self.except_end_loop:
            self.invert_style_if_token_detected(oToi, token.loop_statement.end_keyword, lReturn, oFile)

        if self.except_end_subprogram_body:
            self.invert_style_if_token_detected(oToi, token.subprogram_body.end_keyword, lReturn, oFile)

    def invert_style_if_token_detected(self, oToi, oTokenType, lReturn, oFile):
        sNewStyle = self.inverse_style()
        
        if oToi.tokens_start_with_types([parser.whitespace, oTokenType]):
           lReturn[-1].style = sNewStyle
        elif oToi.tokens_start_with_types([parser.blank_line]):
            oNextLineToi = oFile.get_line_succeeding_line(oToi.get_line_number())
            if oNextLineToi.tokens_start_with_types([parser.whitespace, oTokenType]):
                lReturn[-1].style = sNewStyle
