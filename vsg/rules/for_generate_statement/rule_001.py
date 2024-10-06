# -*- coding: utf-8 -*-

from vsg.rules import insert_token_right_of_token_if_it_does_not_exist_before_token
from vsg.token.for_generate_statement import end_keyword, generate_keyword
from vsg.token.generate_statement_body import begin_keyword


class rule_001(insert_token_right_of_token_if_it_does_not_exist_before_token):
    """
    This rule checks for the existence of the **begin** keyword.

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
        super().__init__(begin_keyword("begin"), generate_keyword, end_keyword)
        self.solution = "*begin* keyword"
        self.groups.append("structure::optional")
        self.disable = True
