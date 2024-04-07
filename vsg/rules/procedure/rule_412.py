# -*- coding: utf-8 -*-

from vsg.deprecated_rule import Rule


class rule_412(Rule):
    """
    This rule has been superseded by rule `architecture_027 <architecture_rules.html#architecture-027>`_.
    """

    def __init__(self):
        Rule.__init__(self)
        self.message.append("Rule " + self.unique_id + " has been superseded by rule architecture_027.")
