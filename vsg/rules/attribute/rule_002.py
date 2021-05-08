
from vsg.depricated_rule import Depricated


class rule_002(Depricated):

    def __init__(self):
        Depricated.__init__(self, 'attribute', '002')
        self.message.append('Rule ' + self.unique_id + ' has been superceeded by attribute_declaration_500 and attribute_specification_500.')
