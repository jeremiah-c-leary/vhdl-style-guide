
from vsg.deprecated_rule import Rule


class rule_202(Rule):
    '''
    This rule has been moved to rule `subprogram_body_202 <subprogram_body_rules.html#subprogram-body-202>`_.
    '''

    def __init__(self):
        Rule.__init__(self, 'function', '202')
        self.message.append('Rule ' + self.unique_id + ' has been moved to rule subprogram_body_202.')
