
from vsg.rules import single_space_between_tokens

from vsg.token import loop_statement as token
from vsg.token import iteration_scheme


class rule_005(single_space_between_tokens):
    '''
    This rule checks if a label exists on a for loop that a single space exists after the colon.

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
        single_space_between_tokens.__init__(self, 'for_loop', '005', token.label_colon, iteration_scheme.for_keyword)
        self.solution = 'Ensure a single space between label and :.'
