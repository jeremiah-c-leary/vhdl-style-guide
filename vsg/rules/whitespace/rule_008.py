# -*- coding: utf-8 -*-

from vsg.deprecated_rule import Rule


class rule_008(Rule):
    """
    This rule has been deprecated and replaced with rule `index_constraint_100 <index_constraint_rules.html#index_constraint-100>`_.
    """

    def __init__(self):
        Rule.__init__(self)
        self.message.append("Rule " + self.unique_id + " has been replaced with index_constraint_100.")
