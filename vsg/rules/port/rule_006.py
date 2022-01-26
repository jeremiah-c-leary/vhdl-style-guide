
from vsg import deprecated_rule


class rule_006(deprecated_rule.Rule):
    '''
    This rule has been deprecated and it's function was include in rule **port_005**.
    '''

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'port', '006')
        self.message.append('Rule ' + self.unique_id + ' has been included in rule port_005.')
