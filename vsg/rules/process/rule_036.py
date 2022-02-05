
from vsg.rules import token_prefix

from vsg import token

lTokens = []
lTokens.append(token.process_statement.process_label)
lTokens.append(token.process_statement.end_process_label)


class rule_036(token_prefix):
    '''
    This rule checks for valid prefixes on process labels.
    The default prefix is *proc\_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       main: process () is

    **Fix**

    .. code-block:: vhdl

       proc_main: process () is
    '''

    def __init__(self):
        token_prefix.__init__(self, 'process', '036', lTokens)
        self.prefixes = ['proc_']
        self.solution = 'Process labels'
