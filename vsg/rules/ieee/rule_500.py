# -*- coding: utf-8 -*-

from vsg import deprecated_rule

lTokens = []


class rule_500(deprecated_rule.Rule):
    """
    This rule was deprecated and replaced with the following rule:

    * :ref:`type_mark_500`
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " has been replaced with the following rule:")
        self.message.append("  type_mark_500")
