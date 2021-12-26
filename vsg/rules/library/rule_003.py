
from vsg.rules import previous_line

from vsg import token

lTokens = []
lTokens.append(token.library_clause.keyword)


class rule_003(previous_line):
    '''
    This rule checks for blank lines or comments above the entity keyword.

    Refer to the section `Configuring Previous Line Rules <configuring.html#configuring-previous-line-rules>`_ for options.

    There is an additional **allow_library_clause** option which can be set.
    Refer to section `Reporting Single Rule Configuration <configuring.html#reporting-single-rule-configuration>`_ for details on finding configuration options for individual rules.

    allow_library_clause
    ^^^^^^^^^^^^^^^^^^^^

    When set to **True**, it allows consecutive library clauses.

    **Violation**

    .. code-block:: vhdl

       library ieee;
         use ieee.std_logic_1164.all;
       library top_dsn;
       library fifo_dsn;

    **Fix**

    .. code-block:: vhdl

       library ieee;
         use ieee.std_logic_1164.all;

       library top_dsn;
       library fifo_dsn;
    '''

    def __init__(self):
        previous_line.__init__(self, 'library', '003', lTokens)
        self.allow_library_clause = False
        self.configuration.append('allow_library_clause')
        self.style = 'require_blank_line'

    def _set_allow_tokens(self):
        if self.allow_library_clause:
            self.lAllowTokens = []
            self.lAllowTokens.append(token.library_clause.keyword)
