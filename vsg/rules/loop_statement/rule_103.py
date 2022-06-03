
from vsg.rules.whitespace_between_tokens import Rule

from vsg.token import loop_statement as token


class rule_103(Rule):
    '''
    This rule checks if a label exists that a single space exists between the label and the colon.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

         label: for index in 4 to 23 loop
         label    : for index in 0 to 100 loop

    **Fix**

    .. code-block:: vhdl

         label : for index in 4 to 23 loop
         label : for index in 0 to 100 loop
    '''
    def __init__(self):
        Rule.__init__(self, 'loop_statement', '103')
        self.left_token = token.loop_label
        self.right_token = token.label_colon
