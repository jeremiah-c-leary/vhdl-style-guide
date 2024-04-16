# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_026(deprecated_rule.Rule):
    """
    This rule has been renamed to `generic_map_003 <generic_map_rules.html#generic-map-003>`_.
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " has been renamed to generic_map_003.")
