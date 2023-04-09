
from vsg.rules import insert_token_right_of_token_if_it_does_not_exist_between_tokens_using_value_from_token as Rule

from vsg import token

oInsertToken = token.subprogram_kind.procedure_keyword

oAnchorToken = token.subprogram_body.end_keyword

oLeftToken = token.procedure_specification.procedure_keyword
oRightToken = token.subprogram_body.semicolon

oValueToken = token.procedure_specification.procedure_keyword


class rule_012(Rule):
    '''
    This rule checks the procedure keyword exist in the closing of the procedure specification.

    |configuring_optional_items_link|

    **Violation**

    .. code-block:: vhdl

       procedure proc is

       end proc;

    **Fix**

    .. code-block:: vhdl

       procedure proc is

       end procedure proc;
    '''

    def __init__(self):
        Rule.__init__(self, 'procedure', '012', oInsertToken, oAnchorToken, oLeftToken, oRightToken, oValueToken)
        self.solution = 'procedure keyword'
        self.groups.append('structure::optional')
        self.filter_tokens.append(token.subprogram_declaration.semicolon)
