
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_and_not_on_same_line_as_token

from vsg.token import procedure_specification as token


class rule_011(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_and_not_on_same_line_as_token):
    '''
    This rule checks for a procedure parameter on the same line as the procedure keyword when the parameters are on multiple lines.

    **Violation**

    .. code-block:: vhdl

       procedure average_samples (constant a : in integer;
         signal d : out std_logic
       ) is
       begin


    **Fix**

    .. code-block:: vhdl

       procedure average_samples (
         constant a : in integer;
         signal d : out std_logic
       ) is
       begin
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_and_not_on_same_line_as_token.__init__(self, 'procedure', '011', token.open_parenthesis, token.close_parenthesis)
        self.solution = 'Move procedure parameter to the next line.'
