
from vsg import deprecated_rule


class rule_005(deprecated_rule.Rule):
    '''
    This rule has been deprecated and it's function has been included in rules **port_007**, **port_008** and **port_009**.
    '''

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'port', '005')
        self.message.append('Rule ' + self.unique_id + ' has been included in rules port_007, port_008 and port_009.')
