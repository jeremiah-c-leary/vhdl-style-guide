
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_and_not_on_same_line_as_token

from vsg.token import function_specification as token


class rule_009(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_and_not_on_same_line_as_token):
    '''
    This rule checks for a function parameter on the same line as the function keyword when the parameters are on multiple lines.

    **Violation**

    .. code-block:: vhdl

       function func_1 (a : integer; b : integer;
         c : unsigned(3 downto 0);
         d : std_logic_vector(7 downto 0);
         e : std_logic) return integer is
       begin

       end;


    **Fix**

    .. code-block:: vhdl

       function func_1 (
         a : integer; b : integer;
         c : unsigned(3 downto 0);
         d : std_logic_vector(7 downto 0);
         e : std_logic) return integer is
       begin

       end;
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_and_not_on_same_line_as_token.__init__(self, 'function', '009', token.open_parenthesis, token.close_parenthesis)
        self.solution = 'Move function parameter to the next line.'
