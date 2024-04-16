# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_010(deprecated_rule.Rule):
    """
    The function of this rule has been superseded by the following rules:

    * ieee_500
    * subtype_002
    * type_014
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " has been superseded by the following rules:")
        self.message.append("  ieee_500")
        self.message.append("  subtype_002")
        self.message.append("  type_014")
