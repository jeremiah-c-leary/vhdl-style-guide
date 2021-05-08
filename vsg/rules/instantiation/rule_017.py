
from vsg.depricated_rule import Depricated


class rule_017(Depricated):

    def __init__(self):
        Depricated.__init__(self, 'instantiation', '017')
        self.message.append('Rule ' + self.unique_id + ' has been renamed to rule generic_map_005.')
