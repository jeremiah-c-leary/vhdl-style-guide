# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_502(deprecated_rule.Rule):
    """
    This rule has been deprecated.  The case of *entity_designator* should be enforced by other rules.
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " has been deprecated.")
