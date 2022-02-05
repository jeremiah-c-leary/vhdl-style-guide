
from vsg.rules import single_space_between_tokens

from vsg.token import loop_statement as token


class rule_103(single_space_between_tokens):
    '''
    This rule checks if a label exists that a single space exists between the label and the colon.

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
        single_space_between_tokens.__init__(self, 'loop_statement', '103', token.loop_label, token.label_colon)
        self.solution = 'Ensure a single space between label and :.'
