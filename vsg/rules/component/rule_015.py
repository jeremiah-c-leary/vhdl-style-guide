# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_015(deprecated_rule.Rule):
    """
    This rule has been deprecated.
    The **component** keyword is required per the LRM.
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " is required per the LRM.")
