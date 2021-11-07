
from vsg import deprecated_rule


class rule_001(deprecated_rule.Rule):

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'attribute', '001')
        self.message.append('Rule ' + self.unique_id + ' has been superceeded by attribute_declaration_300 and attribute_specification_300.')
