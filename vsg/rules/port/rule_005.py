# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_005(deprecated_rule.Rule):
    """
    This rule has been deprecated and its function has been included in rules **port_007**, **port_008** and **port_009**.
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " has been included in rules port_007, port_008 and port_009.")
