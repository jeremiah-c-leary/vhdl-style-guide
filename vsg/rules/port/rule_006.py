# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_006(deprecated_rule.Rule):
    """
    This rule has been deprecated and its function was include in rule **port_005**.
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " has been included in rule port_005.")
