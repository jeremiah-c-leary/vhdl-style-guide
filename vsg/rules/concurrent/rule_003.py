
from vsg.rules import multiline_alignment_between_tokens

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.concurrent_simple_signal_assignment.assignment, token.concurrent_simple_signal_assignment.semicolon])


class rule_003(multiline_alignment_between_tokens):
    '''
    This rule checks alignment of multiline concurrent simple signal assignments.
    Succesive lines should align to the space after the assignment operator.
    However, there is a special case if there are parenthesis in the assignment.
    If the parenthesis are not closed on the same line, then the next line will be aligned to the parenthesis.
    Aligning to the parenthesis improves readability.

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
    '''

    def __init__(self):
        multiline_alignment_between_tokens.__init__(self, 'concurrent', '003', lTokenPairs)
        self.phase = 5
        self.subphase = 2
