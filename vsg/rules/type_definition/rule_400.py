
from vsg.rules import align_tokens_in_region_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.element_declaration.colon)

oStartToken = token.record_type_definition.record_keyword

oEndToken = token.record_type_definition.end_keyword


class rule_400(align_tokens_in_region_between_tokens):
    '''
    This rule checks the colons are in the same column for all elements in the block declarative part.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       type t_some_record is record
         element_1 : natural;
         some_other_element : natural;
         yet_another_element : natural;
       end record;

    **Fix**

    .. code-block:: vhdl

       type t_some_record is record
         element_1           : natural;
         some_other_element  : natural;
         yet_another_element : natural;
       end record;
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens.__init__(self, 'type', '400', lAlign, oStartToken, oEndToken)
