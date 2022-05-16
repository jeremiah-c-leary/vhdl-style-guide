
from vsg.deprecated_rule import Rule


class rule_007(Rule):
    '''
    This rule has been moved to rule `subprogram_body_205 <subprogram_body_rules.html#subprogram-body-205>`_.
    '''

    def __init__(self):
        Rule.__init__(self, 'function', '007')
        self.message.append('Rule ' + self.unique_id + ' has been moved to rule subprogram_body_205.')
