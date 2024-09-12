# -*- coding: utf-8 -*-

from vsg.rules import (
    insert_token_right_of_possible_tokens_if_it_does_not_exist_before_token,
)
from vsg.token import for_generate_statement, generate_statement_body

oInsertToken = generate_statement_body.begin_keyword("begin")
lRightTokens = [for_generate_statement.generate_keyword]
oBeforeToken = for_generate_statement.end_keyword


class rule_022(insert_token_right_of_possible_tokens_if_it_does_not_exist_before_token):
    """
    This rule checks for the existence of the **begin** keyword in for generate statements.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       ram_array : for i in 0 to 7 generate
       end generate;

    **Fix**

    .. code-block:: vhdl

       ram_array : for i in 0 to 7 generate begin
       end generate;
    """

    def __init__(self):
        super().__init__(oInsertToken, lRightTokens, oBeforeToken)
        insert_token_right_of_possible_tokens_if_it_does_not_exist_before_token.__init__(self, oInsertToken, lRightTokens, oBeforeToken)
        self.solution = "*begin* keyword"
        self.groups.append("structure::optional")
        self.disable = True
