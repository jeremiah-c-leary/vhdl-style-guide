
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.for_generate_statement.generate_label, token.for_generate_statement.label_colon])
lTokens.append([token.if_generate_statement.generate_label, token.if_generate_statement.label_colon])
lTokens.append([token.case_generate_statement.generate_label, token.case_generate_statement.label_colon])

class rule_002(single_space_between_token_pairs):
    '''
    This rule checks for a single space between the label and the colon.

    **Violation**

    .. code-block:: vhdl

       ram_array: for i in 0 to 7 generate

    **Fix**

    .. code-block:: vhdl

       ram_array : for i in 0 to 7 generate
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'generate', '002', lTokens)
        self.solution = 'Ensure a single space between label and :.'
