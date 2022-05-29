
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
            
        if self.style == 'require_blank_line':
            if self.lHierarchyLimits is None:
                lToi = oFile.get_line_below_line_ending_with_token(self.lTokens)
            else:
                lToi = oFile.get_line_below_line_ending_with_token_with_hierarchy(self.lTokens, self.lHierarchyLimits)
            lReturn = []
            for oToi in lToi:
                oToi.style = self.style
                lReturn.append(oToi)

                if self.except_end_case:
                    something(oToi, token.case_statement.end_keyword, lReturn, oFile)

                if self.except_end_process:
                    something(oToi, token.process_statement.end_keyword, lReturn, oFile)

                if self.except_end_if:
                    something(oToi, token.if_statement.end_keyword, lReturn, oFile)

                if self.except_end_loop:
                    something(oToi, token.loop_statement.end_keyword, lReturn, oFile)

                if self.except_end_subprogram_body:
                    something(oToi, token.subprogram_body.end_keyword, lReturn, oFile)

#        elif self.style == 'no_blank_line':
#            lToi = oFile.get_blank_lines_below_line_ending_with_token(self.lTokens, self.lHierarchyLimits)
#            lReturn = []
#            for oToi in lToi:
#                oToi.style = 'no_blank_line'
#                lReturn.append(oToi)

        elif self.style == 'no_blank_line':
            if self.lHierarchyLimits is None:
                lToi = oFile.get_line_below_line_ending_with_token(self.lTokens, bIncludeCarriageReturn=True)
            else:
                lToi = oFile.get_line_below_line_ending_with_token_with_hierarchy(self.lTokens, self.lHierarchyLimits, bIncludeCarriageReturn=True)
            lReturn = []
            for oToi in lToi:
                oToi.style = self.style
                lReturn.append(oToi)

                if self.except_end_if:
                    something_else(oToi, token.if_statement.end_keyword, lReturn, oFile)


        return lReturn


def something(oToi, oTokenType, lReturn, oFile):
    if oToi.tokens_start_with_types([parser.whitespace, oTokenType]):
       lReturn.pop()
    else:
        oNextLineToi = oFile.get_line_succeeding_line(oToi.get_line_number())
        if oNextLineToi.tokens_start_with_types([parser.whitespace, oTokenType]) and oToi.tokens_start_with_types([parser.blank_line]):
            oMyToi_w_carraige_return = oFile.get_line_number(oToi.get_line_number())
            oMyToi_w_carraige_return.style = 'no_blank_line'
            lReturn[-1] = oMyToi_w_carraige_return


def something_else(oToi, oTokenType, lReturn, oFile):
    if oToi.tokens_start_with_types([parser.whitespace, oTokenType]):
       lReturn[-1].style = 'require_blank_line'
    elif oToi.tokens_start_with_types([parser.blank_line]):
        oNextLineToi = oFile.get_line_succeeding_line(oToi.get_line_number())
        if oNextLineToi.tokens_start_with_types([parser.whitespace, oTokenType]):
            lReturn[-1].style = 'require_blank_line'
#            oMyToi_w_carraige_return = oFile.get_line_number(oToi.get_line_number())
#            oMyToi_w_carraige_return.style = 'require_blank_line'
#            lReturn[-1] = oMyToi_w_carraige_return
