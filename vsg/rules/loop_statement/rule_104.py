
from vsg.rules.whitespace_after_token import Rule

from vsg.token import loop_statement as token

lTokens = []
lTokens.append(token.label_colon)


class rule_104(Rule):
    '''
    This rule checks if a label exists that a single space exists after the colon.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

         label :    for index in 4 to 23 loop
         label :  for index in 0 to 100 loop

    **Fix**

    .. code-block:: vhdl

         label : for index in 4 to 23 loop
         label : for index in 0 to 100 loop
    '''
    def __init__(self):
        Rule.__init__(self, 'loop_statement', '104', lTokens)
