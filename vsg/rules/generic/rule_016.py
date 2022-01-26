
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens

from vsg import token


class rule_016(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens):
    '''
    This rule checks for multiple generics defined on a single line.

    **Violation**

    .. code-block:: vhdl

      generic (
        g_width : std_logic := '0';g_depth : std_logic := '1'
      );

    **Fix**

    .. code-block:: vhdl

      generic (
        g_width : std_logic := '0';
        g_depth : std_logic := '1'
      );
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens.__init__(self, 'generic', '016', [token.interface_list.semicolon], token.generic_clause.open_parenthesis, token.generic_clause.close_parenthesis)
        self.solution = 'Move multiple generics to their own lines.'
