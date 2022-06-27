

from vsg.rules import move_token_next_to_another_token as Rule

from vsg.token import full_type_declaration as token


class rule_018(Rule):
    '''
    This rule checks the **is** keyword is on the same line as the identifier.

    **Violation**

    .. code-block:: vhdl

       type t_record
       is

    **Fix**

    .. code-block:: vhdl

       type t_record is
    '''

    def __init__(self):
        Rule.__init__(self, 'type', '018', token.identifier, token.is_keyword)
        self.solution = 'Ensure *is* keyword is on the same line as the identifier.'
        self.subphase = 2
