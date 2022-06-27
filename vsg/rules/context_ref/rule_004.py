
from vsg import deprecated_rule


class rule_004(deprecated_rule.Rule):
    '''
    This rule has been split into the following rules:

    * :ref:`context_ref_500`
    * :ref:`context_ref_501`
    '''

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'context_ref', '004')
        self.message.append('Rule ' + self.unique_id + ' has been split into the following rules:')
        self.message.append('  context_ref_500')
        self.message.append('  context_ref_501')
