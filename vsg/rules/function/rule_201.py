
from vsg.deprecated_rule import Rule


class rule_201(Rule):
    '''
    This rule has been moved to rule `subprogram_body_201 <subprogram_body_rules.html#subprogram-body-201>`_.
    '''

    def __init__(self):
        Rule.__init__(self, 'function', '201')
        self.message.append('Rule ' + self.unique_id + ' has been moved to rule subprogram_body_201.')
