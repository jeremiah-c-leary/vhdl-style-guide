
from vsg.deprecated_rule import Rule


class rule_203(Rule):
    '''
    This rule has been moved to rule `subprogram_body_203 <subprogram_rules.html#subprogram-body-203>`_.
    '''

    def __init__(self):
        Rule.__init__(self, 'function', '203')
        self.message.append('Rule ' + self.unique_id + ' has been moved to rule subprogram_body_203.')
