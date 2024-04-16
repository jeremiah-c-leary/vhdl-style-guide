# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_013(deprecated_rule.Rule):
    """
    This rule has been renamed to `generic_map_001 <generic_map_rules.html#generic-map-001>`_.
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " has been renamed to rule generic_map_001.")
