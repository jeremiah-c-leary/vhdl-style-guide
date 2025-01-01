# -*- coding: utf-8 -*-

from vsg.deprecated_rule import Rule


class rule_014(Rule):
    """
    This rule has been deprecated and replaced with rule `subprogram_kind_501 <subprogram_kind_rules.html#subprogram-kind-501>`_.
    """

    def __init__(self):
        Rule.__init__(self)
        self.message.append("Rule " + self.unique_id + " has been replaced with subprogram_kind_501.")
