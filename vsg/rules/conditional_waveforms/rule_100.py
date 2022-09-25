
from vsg.rules.whitespace_before_token import Rule

from vsg.token import conditional_waveforms as token


class rule_100(Rule):
    '''
    This rule checks for a single space before the **when** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       wr_en <= '0'when (rd_en = '0') else '1';

    **Fix**

    .. code-block:: vhdl

       wr_en <= '0' when (rd_en = '0') else '1';
    '''

    def __init__(self):
        Rule.__init__(self, 'conditional_waveforms', '100', [token.when_keyword])
