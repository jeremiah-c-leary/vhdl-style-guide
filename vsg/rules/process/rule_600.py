
from vsg.rules import token_suffix

from vsg import token

lTokens = []
lTokens.append(token.process_statement.process_label)
lTokens.append(token.process_statement.end_process_label)


class rule_600(token_suffix):
    '''
    This rule checks for valid suffixes on process labels.
    The default suffix is *\_proc*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       main: process () is

    **Fix**

    .. code-block:: vhdl

       main_proc: process () is
    '''

    def __init__(self):
        token_suffix.__init__(self, 'process', '600', lTokens)
        self.suffixes = ['_proc']
        self.solution = 'Process labels'
