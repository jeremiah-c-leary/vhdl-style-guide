
from vsg import deprecated_rule


class rule_009(deprecated_rule.Rule):
    '''
    The function of this rule has been superseded and is handled by rule function_019.
    '''

    def __init__(self):
        deprecated_rule.Rule.__init__(self)
        self.message.append('The function of rule ' + self.unique_id + ' is covered by rule function_019.')
