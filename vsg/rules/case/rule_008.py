
from vsg import deprecated_rule


class rule_008(deprecated_rule.Rule):
    '''
    The function of this rule has been included in rule case_201.
    '''
    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'case', '008')
        self.message.append('The function of rule ' + self.unique_id + ' has been included in rule case_201:')
