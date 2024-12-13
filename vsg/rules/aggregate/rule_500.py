# -*- coding: utf-8 -*-

from vsg.deprecated_rule import Rule


class rule_500(Rule):
    """
    This rule has been deprecated and replaced with rule `choice_500 <choice_rules.html#choice-500>`_.
    """

    def __init__(self):
        Rule.__init__(self)
        self.message.append("Rule " + self.unique_id + " has been merged into choice_500.")
