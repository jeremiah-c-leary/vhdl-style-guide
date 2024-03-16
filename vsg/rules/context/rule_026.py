# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_026(deprecated_rule.Rule):
    """
    The function of this rule has been moved to whitespace_200.
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " has been moved to whitespace_200.")
