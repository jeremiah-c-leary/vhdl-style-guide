# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_300(deprecated_rule.Rule):
    """
    The function of this rule has been superseded with comment indent updates and is handled by rule comment_010.
    """

    def __init__(self):
        super().__init__()
        self.message.append("The function of rule " + self.unique_id + " is covered by rule comment_010.")
