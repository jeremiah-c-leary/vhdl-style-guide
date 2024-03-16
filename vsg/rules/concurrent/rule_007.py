# -*- coding: utf-8 -*-

from vsg import deprecated_rule


class rule_007(deprecated_rule.Rule):
    """
    This rule has been renamed to `conditional_waveforms_001 <conditional_waveforms_rules.html#conditional-waveforms-001>`_.
    """

    def __init__(self):
        super().__init__()
        self.message.append("Rule " + self.unique_id + " has been renamed to conditional_waveforms_001.")
