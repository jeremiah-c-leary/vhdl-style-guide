
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.function_specification.pure_keyword, token.function_specification.function_keyword])
lTokens.append([token.function_specification.impure_keyword, token.function_specification.function_keyword])
lTokens.append([token.function_specification.function_keyword, token.function_specification.designator])
lTokens.append([token.function_specification.designator, token.function_specification.return_keyword])
lTokens.append([token.function_specification.designator, token.function_specification.open_parenthesis])
lTokens.append([token.function_specification.close_parenthesis, token.function_specification.return_keyword])
lTokens.append([token.function_specification.return_keyword, token.type_mark.name])
lTokens.append([token.type_mark.name, token.subprogram_body.is_keyword])


class rule_100(single_space_between_token_pairs):
    '''
    This rule checks for a single space between the following function elements:  **function** keyword, function designator, open parenthesis, close parenthesis, **return** keyword, return type and **is** keyword.

    **Violation**

    .. code-block:: vhdl

       function     overflow    (a: integer)     return     integer    is

    **Fix**

    .. code-block:: vhdl

       function overflow (a: integer) return integer is
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'function', '100', lTokens)
        self.solution = 'Ensure a single space between the keywords in the opening part of a function specification.'

