
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.case_generate_statement.end_generate_keyword, token.case_generate_statement.end_generate_label])
lTokens.append([token.for_generate_statement.end_generate_keyword, token.for_generate_statement.end_generate_label])
lTokens.append([token.if_generate_statement.end_generate_keyword, token.if_generate_statement.end_generate_label])


class rule_013(single_space_between_token_pairs):
    '''
    This rule checks for a single space after the **generate** keyword and the label in the **end generate** keywords.

    **Violation**

    .. code-block:: vhdl

       end generate    ram_array;

    **Fix**

    .. code-block:: vhdl

       end generate ram_array;
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'generate', '013', lTokens)
        self.solution = 'Ensure there is only one space between the *generate* keyword and the label.'
