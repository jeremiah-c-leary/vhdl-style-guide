# -*- coding: utf-8 -*-

from vsg.deprecated_rule import Rule


class rule_204(Rule):
    """
    This rule has been moved to rule `subprogram_body_204 <subprogram_body_rules.html#subprogram-body-204>`_.
    """

    def __init__(self):
        Rule.__init__(self)
        self.message.append("Rule " + self.unique_id + " has been moved to rule subprogram_body_204.")
