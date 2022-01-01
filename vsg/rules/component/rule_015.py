
from vsg import deprecated_rule


class rule_015(deprecated_rule.Rule):
    '''
    This rule has been depricated.
    The **component** keyword is required per the LRM.
    '''

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'component', '015')
        self.message.append('Rule ' + self.unique_id + ' is required per the LRM.')
