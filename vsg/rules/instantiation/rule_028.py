# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_with_prefix_suffix as Rule

lTokens = []
lTokens.append(token.instantiated_unit.entity_name)


class rule_028(Rule):
    """
    This rule checks the entity name has proper case in direct instantiations.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       instance_name : entity library.ENTITY_NAME

    **Fix**

    .. code-block:: vhdl

       instance_name : entity library.entity_name
    """

    def __init__(self):
        super().__init__(lTokens)
        self.groups.append("case::name")
