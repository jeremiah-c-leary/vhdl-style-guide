
from vsg.deprecated_rule import Rule


class rule_205(Rule):
    '''
    This rule has been moved to rule `subprogram_body_205 <subprogram_body_rules.html#subprogram-body-205>`_.
    '''

    def __init__(self):
        Rule.__init__(self, 'procedure', '205')
        self.message.append('Rule ' + self.unique_id + ' has been moved to rule subprogram_body_205.')
