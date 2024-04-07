# -*- coding: utf-8 -*-

from vsg import rule


class Rule(rule.Rule):
    """
    Class for assigning rules to the case group.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.
    """

    def __init__(self):
        super().__init__()
        self.phase = 6
        self.groups.append("case")
        self.configuration_documentation_link = "configuring_uppercase_and_lowercase_rules_link"
        self.remap = False
