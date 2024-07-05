# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_008(deprecated_rule.Rule):
    """
    The function of this rule has been included in rule case_201.
    """

    def __init__(self):
        super().__init__()
        self.message.append("The function of rule " + self.unique_id + " has been included in rule case_201:")
