# -*- coding: utf-8 -*-

from vsg import rule


class Rule(rule.Rule):
    """
    Class for assigning rules to the indent group.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.
    """

    def __init__(self):
        super().__init__()
        self.phase = 4
        self.groups.append("indent")
