# -*- coding: utf-8 -*-

from vsg.deprecated_rule import Rule


class rule_009(Rule):
    """
    This rule has been deprecated and replaced with rule `procedure_505 <procedure_rules.html#procedure-505>`_.
    """

    def __init__(self):
        Rule.__init__(self)
        self.message.append("Rule " + self.unique_id + " has been replaced with procedure_505.")
