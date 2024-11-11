# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_013(deprecated_rule.Rule):
    """
    This rule has been superseded by `null_statement_300 <null_statement_rules.html#null-statement-300>`_.
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " has been superseded by null_statement_300.")
