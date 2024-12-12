# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_018(deprecated_rule.Rule):
    """
    This rule was deprecated and replaced with rules:

    * `generic_map_006 <generic_map_rules.html#generic-map-006>`_.
    * `port_map_006 <port_map_rules.html#port-map-006>`_.
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " was replaced with the following rules:")
        self.message.append("  generic_map_006")
        self.message.append("  port_map_006")
