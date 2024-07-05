# -*- coding: utf-8 -*-

from vsg import rule


class Rule(rule.Rule):
    """
    Class for assigning rules to the length group.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.
    """

    def __init__(self):
        super().__init__()
        self.phase = 2
        self.groups.append("whitespace")
        self.configuration_documentation_link = "configuring_whitespace_rules_link"
