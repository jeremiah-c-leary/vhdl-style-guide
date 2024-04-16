# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_015(deprecated_rule.Rule):
    """
    This rule has been replaced with the following rules:

    * `generate_020 <generate_rules.html#generate-020>`_
    * `generate_021 <generate_rules.html#generate-021>`_
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " has been replaced with the following rules:")
        self.message.append("  * generate_020")
        self.message.append("  * generate_021")
