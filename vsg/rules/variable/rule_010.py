
from vsg import deprecated_rule


class rule_010(deprecated_rule.Rule):
    '''
    The function of this rule has been superceeded by the following rules:

    * ieee_500
    * subtype_002
    * type_014
    '''
    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'variable', '010')
        self.message.append('Rule ' + self.unique_id + ' has been superceeded by the following rules:')
        self.message.append('  ieee_500')
        self.message.append('  subtype_002')
        self.message.append('  type_014')
