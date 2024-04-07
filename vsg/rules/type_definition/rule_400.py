# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import align_tokens_in_region_between_tokens

lAlign = []
lAlign.append(token.element_declaration.colon)

oStartToken = token.record_type_definition.record_keyword

oEndToken = token.record_type_definition.end_keyword


class rule_400(align_tokens_in_region_between_tokens):
    """
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
    """

    def __init__(self):
        super().__init__(lAlign, oStartToken, oEndToken)
        self.configuration.remove("case_control_statements_ends_group")
        self.configuration.remove("if_control_statements_ends_group")
        self.configuration.remove("loop_control_statements_ends_group")
