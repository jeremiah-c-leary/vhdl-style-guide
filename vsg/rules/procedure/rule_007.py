# -*- coding: utf-8 -*-

from vsg.deprecated_rule import Rule


class rule_007(Rule):
    """
    This rule has been moved to rule `procedure_507 <procedure_rules.html#procedure-507>`_.
    """

    def __init__(self):
        Rule.__init__(self)
        self.message.append("Rule " + self.unique_id + " has been moved to rule procedure_507.")
