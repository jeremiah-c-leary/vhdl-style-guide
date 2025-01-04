# -*- coding: utf-8 -*-

from vsg.deprecated_rule import Rule


class rule_502(Rule):
    """
    This rule has been deprecated and replaced with rule `parameter_specification_501 <parameter_specification_rules.html#parameter-specification-501>`_.
    """

    def __init__(self):
        Rule.__init__(self)
        self.message.append("Rule " + self.unique_id + " has been replaced with parameter_specification_501.")
