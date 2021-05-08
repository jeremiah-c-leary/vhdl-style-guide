
from vsg.depricated_rule import Depricated


class rule_024(Depricated):

    def __init__(self):
        Depricated.__init__(self, 'instantiation', '024')
        self.message.append('Rule ' + self.unique_id + ' has been split into rules:')
        self.message.append('  generic_map_008')
        self.message.append('  rule port_map_005')
