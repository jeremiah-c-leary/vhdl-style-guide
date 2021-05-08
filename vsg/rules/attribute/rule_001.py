
from vsg.depricated_rule import Depricated


class rule_001(Depricated):

    def __init__(self):
        Depricated.__init__(self, 'attribute', '001')
        self.message.append('Rule ' + self.unique_id + ' has been superceeded by attribute_declaration_300 and attribute_specification_300.')
