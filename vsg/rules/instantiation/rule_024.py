# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_024(deprecated_rule.Rule):
    """
    This rule has been split into:

    * `generic_map_008 <generic_map_rules.html#generic-map-008>`_
    * `port_map_008 <port_map_rules.html#port-map-008>`_
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " has been split into rules:")
        self.message.append("  generic_map_008")
        self.message.append("  rule port_map_005")
