# -*- coding: utf-8 -*-

from vsg.rules.whitespace_between_tokens import Rule
from vsg.token import choice, element_association


class rule_100(Rule):
    """
    This rule checks for a single space between the **others** keyword and the => in an element_association.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       a <= (others=> (others    => '0'));

    **Fix**

    .. code-block:: vhdl

       a <= (others => (others => '0'));
    """

    def __init__(self):
        Rule.__init__(self)
        self.left_token = choice.others_keyword
        self.right_token = element_association.assignment
