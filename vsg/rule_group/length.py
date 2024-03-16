# -*- coding: utf-8 -*-

from vsg import rule, severity


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
        self.phase = 7
        self.fixable = False
        self.groups.append("length")
        self.severity = severity.warning("Warning")
        self.configuration.append("length")
        self.configuration_documentation_link = "configuring_length_rules_link"
