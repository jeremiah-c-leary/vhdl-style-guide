
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.full_type_declaration.identifier, token.full_type_declaration.is_keyword])


class rule_006(single_space_between_token_pairs):
    '''
    This rule checks for a single space before the **is** keyword.

    **Violation**

    .. code-block:: vhdl

       type state_machine    is (idle, write, read, done);

    **Fix**

    .. code-block:: vhdl

       type state_machine is (idle, write, read, done);
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'type', '006', lTokens)
        self.solution = 'Ensure only a single space before the *is* keyword.'
