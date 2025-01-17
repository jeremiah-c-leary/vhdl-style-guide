# -*- coding: utf-8 -*-

from vsg.rules.whitespace_before_token import Rule
from vsg.token import case_generate_alternative as token


class rule_101(Rule):
    """
    This rule checks for a single space before the **=>** operator.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

      case data generate

        when 3   =>

    **Fix**

    .. code-block:: vhdl

      case data generate

        when 3 =>
    """

    def __init__(self):
        super().__init__([token.assignment])
