# -*- coding: utf-8 -*-

from vsg.deprecated_rule import Rule


class rule_505(Rule):
    """
    This rule has been deprecated and replaced with rule `subprogram_kind_500 <subprogram_kind_rules.html#subprogram-kind-500>`_.
    """

    def __init__(self):
        Rule.__init__(self)
        self.message.append("Rule " + self.unique_id + " has been replaced with subprogram_kind_500.")
