
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
        self.allow_end_ifs = False
        self.configuration.append('allow_end_ifs')
        self.allow_end_process = False
        self.configuration.append('allow_end_process')
        self.except_end_case = False
        self.configuration.append('except_end_case')

    def _get_tokens_of_interest(self, oFile):
        self._update_hierarchy_limits()
        self._update_allow_tokens()
            
        if self.style == 'require_blank_line':
            if self.lHierarchyLimits is None:
                lToi = oFile.get_line_below_line_ending_with_token(self.lTokens)
            else:
                lToi = oFile.get_line_below_line_ending_with_token_with_hierarchy(self.lTokens, self.lHierarchyLimits)
            lReturn = []
            for oToi in lToi:
                if self.except_end_case:
                    if not oToi.tokens_start_with_types([parser.whitespace, token.case_statement.end_keyword]):
                        oNextLineToi = oFile.get_line_succeeding_line(oToi.get_line_number())
                        if oNextLineToi.tokens_start_with_types([parser.whitespace, token.case_statement.end_keyword]):
                            oToi.style = 'no_blank_line'
#                            print(oToi.get_tokens())
#                            print(oToi.get_line_number())
                            oMyToi_w_carraige_return = oFile.get_line_number(oToi.get_line_number())
                            oMyToi_w_carraige_return.style = 'no_blank_line'
                            lReturn.append(oMyToi_w_carraige_return)
                        else:
                            oToi.style = 'require_blank_line'
                              
                            lReturn.append(oToi)
                    else:
                        oToi.style = 'require_blank_line'
#                        lReturn.append(oToi)
                else:
                    oToi.style = 'require_blank_line'
                    lReturn.append(oToi)
        elif self.style == 'no_blank_line':
            lToi = oFile.get_blank_lines_below_line_ending_with_token(self.lTokens, self.lHierarchyLimits)
            lReturn = []
            for oToi in lToi:
                oToi.style = 'no_blank_line'
#                print(oToi.get_line_number())
                lReturn.append(oToi)

        return lReturn

    def _update_allow_tokens(self):
        if self.allow_end_ifs:
            self.lAllowTokens.append(token.if_statement.end_keyword)
        if self.allow_end_process:
            self.lAllowTokens.append(token.process_statement.end_keyword)
#        if self.except_end_case:
#            self.lAllowTokens.append(token.case_statement.end_keyword)

#        print(self.lAllowTokens)

    def _is_except_token(self, oToi, oFile):
        if not self.except_end_case:
            return False
        elif self.except_end_case and self.style == 'require_blank_line':
            if oToi.tokens_start_with_types([parser.whitespace, token.case_statement.end_keyword]):
                return True
#            oNextLineToi = oFile.get_line_succeeding_line(oToi.get_line_number())
#            if oNextLineToi.tokens_start_with_types([parser.whitespace, token.case_statement.end_keyword]):
#                return True
        return False
    

