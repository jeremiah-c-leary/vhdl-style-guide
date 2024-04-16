# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_003(deprecated_rule.Rule):
    """
    This rule was deprecated and replaced with rules:  function_015, package_019, procedure_010, architecture_029 and process_037.
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " has been replaced with the following rules:")
        self.message.append("  function_015, package_019, procedure_010, architecture_029 and process_037.")
