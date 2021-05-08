
from vsg.depricated_rule import Depricated


class rule_021(Depricated):

    def __init__(self):
        Depricated.__init__(self, 'instantiation', '021')
        self.message.append('Rule ' + self.unique_id + ' has been renamed to rule port_map_009.')
