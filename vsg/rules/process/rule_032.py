
from vsg import deprecated_rule


class rule_032(deprecated_rule.Rule):
    '''
    This rule has been replaced with the following rules:

    * `process_037 <process_rules.html#process-037>`_
    * `process_038 <process_rules.html#process-038>`_
    '''

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'process', '032')
        self.message.append('Rule ' + self.unique_id + ' has been replaced with the following rules:')
        self.message.append('  * process_037')
        self.message.append('  * process_038')
