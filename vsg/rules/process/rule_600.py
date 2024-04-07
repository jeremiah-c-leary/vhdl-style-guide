# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_suffix

lTokens = []
lTokens.append(token.process_statement.process_label)
lTokens.append(token.process_statement.end_process_label)


class rule_600(token_suffix):
    """
    This rule checks for valid suffixes on process labels.
    The default suffix is *_proc*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       main: process () is

    **Fix**

    .. code-block:: vhdl

       main_proc: process () is
    """

    def __init__(self):
        super().__init__(lTokens)
        self.suffixes = ["_proc"]
        self.solution = "Process labels"
