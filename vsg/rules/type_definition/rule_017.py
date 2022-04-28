

from vsg.rules import move_token_next_to_another_token as Rule

from vsg.token import full_type_declaration as token


class rule_017(Rule):
    '''
    This rule checks the identifier is on the same line as the type keyword.

    **Violation**

    .. code-block:: vhdl

       type
       t_record is

    **Fix**

    .. code-block:: vhdl

       type t_record
       is
    '''

    def __init__(self):
        Rule.__init__(self, 'type', '017', token.type_keyword, token.identifier)
        self.solution = 'Ensure identifier is on the same line as the *type* keyword.'
