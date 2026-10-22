# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_100(deprecated_rule.Rule):
    """
    This rule has been split into the following rules:

    * :ref:`block_102`
    * :ref:`block_103`
    * :ref:`block_104`
    * :ref:`block_105`
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " has been split into the following rules:")
        self.message.append("  block_102")
        self.message.append("  block_103")
        self.message.append("  block_104")
        self.message.append("  block_105")
