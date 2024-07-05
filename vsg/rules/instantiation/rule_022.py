# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_022(deprecated_rule.Rule):
    """
    This rule has been renamed to `port_map_007 <port_map_rules.html#port-map-007>`_.
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " has been renamed to port_map_007.")
