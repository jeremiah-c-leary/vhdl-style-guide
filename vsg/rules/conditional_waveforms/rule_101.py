
from vsg.rules.whitespace_after_token import Rule

from vsg.token import conditional_waveforms as token


class rule_101(Rule):
    '''
    This rule checks for a single space after the **when** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       wr_en <= '0' when(rd_en = '0') else '1';

    **Fix**

    .. code-block:: vhdl

       wr_en <= '0' when (rd_en = '0') else '1';
    '''

    def __init__(self):
        Rule.__init__(self, 'conditional_waveforms', '101', [token.when_keyword])
