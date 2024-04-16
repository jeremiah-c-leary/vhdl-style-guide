# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_001(deprecated_rule.Rule):
    """
    This rule has been superseded by:

    * `attribute_declaration_300 <attribute_declaration_rules.html#attribute-declaration-300>`_
    * `attribute_specification_300 <attribute_specification_rules.html#attribute-specification-300>`_
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " has been superseded by attribute_declaration_300 and attribute_specification_300.")
