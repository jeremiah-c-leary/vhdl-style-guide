
from vsg import deprecated_rule


class rule_001(deprecated_rule.Rule):
    '''
    This rule has been superceeded by:

    * `attribute_declaration_300 <attribute_declaration_rules.html#attribute-declaration-300>`_
    * `attribute_specification_300 <attribute_specification_rules.html#attribute-specification-300>`_
    '''

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'attribute', '001')
        self.message.append('Rule ' + self.unique_id + ' has been superceeded by attribute_declaration_300 and attribute_specification_300.')
