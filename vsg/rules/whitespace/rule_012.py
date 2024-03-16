# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_012(deprecated_rule.Rule):
    """
    This rule was a duplicate of whitespace_200 and has been removed.
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " has been replaced with whitespace_200.")
