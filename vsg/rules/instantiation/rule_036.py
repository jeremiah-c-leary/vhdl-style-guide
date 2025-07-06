# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import insert_tokens_right_of_token_if_it_does_not_exist_before_token

lInsertTokens = []
lInsertTokens.append(token.instantiated_unit.open_parenthesis("("))
lInsertTokens.append(token.instantiated_unit.architecture_identifier)
lInsertTokens.append(token.instantiated_unit.close_parenthesis(")"))


class rule_036(insert_tokens_right_of_token_if_it_does_not_exist_before_token):
    """
    This rule checks for the optional architecture specification in entity instantiations.

    The default action is "add".

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       cmp_test : entity work.my_module;

    **Fix**

    .. code-block:: vhdl

       cmp_test : entity work.my_module(rtl);
    """

    def __init__(self):
        super().__init__(lInsertTokens, token.instantiated_unit.entity_name, token.component_instantiation_statement.semicolon)
        self.solution = "architecture identifier"
        self.groups.append("structure::optional")
        self.fixable = False
        self.action = "add"
