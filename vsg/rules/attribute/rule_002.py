
from vsg import deprecated_rule


class rule_002(deprecated_rule.Rule):
    '''
    This rule has been superceeded by:

    * `attribute_declaration_500 <attribute_declaration_rules.html#attribute-declaration-500>`_
    * `attribute_specification_500 <attribute_specification_rules.html#attribute-specification-500>`_
    '''

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'attribute', '002')
        self.message.append('Rule ' + self.unique_id + ' has been superceeded by attribute_declaration_500 and attribute_specification_500.')
