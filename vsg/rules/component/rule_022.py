# -*- coding: utf-8 -*-

from vsg.rules import (
    insert_token_left_of_token_if_it_does_not_exist_between_tokens_using_value_from_token as Rule,
)
from vsg.token import component_declaration as token

oInsertToken = token.component_simple_name

oAnchorToken = token.semicolon

oLeftToken = token.end_component_keyword
oRightToken = token.semicolon

oValueToken = token.identifier


class rule_022(Rule):
    """
    This rule inserts the optional **component_simple_name** if it does not exist.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       component my_component

       end component;

    **Fix**

    .. code-block:: vhdl

       component my_component is

       end component my_component;
    """

    def __init__(self):
        super().__init__(oInsertToken, oAnchorToken, oLeftToken, oRightToken, oValueToken)
        self.solution = "component_simple_name"
        self.groups.append("structure::optional")
        self.subphase = 2
