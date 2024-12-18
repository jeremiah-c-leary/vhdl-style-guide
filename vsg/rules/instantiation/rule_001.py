# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_001(deprecated_rule.Rule):
    """
    This rule has been split into the following rules:

    * :ref:`instantiation_300`
    * :ref:`generic_map_300`
    * :ref:`generic_map_301`
    * :ref:`generic_map_302`
    * :ref:`port_map_300`
    * :ref:`port_map_301`
    * :ref:`port_map_302`
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " has been split into the following rules:")
        self.message.append("  instantiation_300")
        self.message.append("  generic_map_300")
        self.message.append("  generic_map_301")
        self.message.append("  generic_map_302")
        self.message.append("  port_map_300")
        self.message.append("  port_map_301")
        self.message.append("  port_map_302")
