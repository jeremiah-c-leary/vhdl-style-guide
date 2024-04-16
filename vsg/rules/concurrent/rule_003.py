# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import multiline_alignment_between_tokens

lTokenPairs = []
lTokenPairs.append([token.concurrent_simple_signal_assignment.assignment, token.concurrent_simple_signal_assignment.semicolon])


class rule_003(multiline_alignment_between_tokens):
    """
    This rule checks alignment of multiline concurrent simple signal assignments.
    Successive lines should align to the space after the assignment operator.
    However, there is a special case if there are parenthesis in the assignment.
    If the parenthesis are not closed on the same line, then the next line will be aligned to the parenthesis.
    Aligning to the parenthesis improves readability.

    |configuring_multiline_indent_rules_link|

    **Violation**

    .. code-block:: vhdl

       O_FOO <= (1 => q_foo(63 downto 32),
                0 => q_foo(31 downto  0));

       n_foo <= resize(unsigned(I_FOO) +
                unsigned(I_BAR), q_foo'length);

    **Fix**

    .. code-block:: vhdl

       O_FOO <= (1 => q_foo(63 downto 32),
                 0 => q_foo(31 downto  0));

       n_foo <= resize(unsigned(I_FOO) +
                       unsigned(I_BAR), q_foo'length);
    """

    def __init__(self):
        super().__init__(lTokenPairs)
        self.phase = 5
        self.subphase = 2
