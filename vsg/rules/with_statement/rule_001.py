# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_001(deprecated_rule.Rule):
    """
    This rule has been replaced with rules in the selected_assignment group.
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " has been replaced by selected_assignment rules.")
