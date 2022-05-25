
from vsg.rules import blank_line_below_line_ending_with_token

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

    def _update_allow_tokens(self):
        if self.allow_end_ifs:
            self.lAllowTokens.append(token.if_statement.end_keyword)
        if self.allow_end_process:
            self.lAllowTokens.append(token.process_statement.end_keyword)


