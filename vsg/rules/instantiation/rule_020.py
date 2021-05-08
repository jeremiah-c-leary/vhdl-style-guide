
from vsg.depricated_rule import Depricated


class rule_020(Depricated):

    def __init__(self):
        Depricated.__init__(self, 'instantiation', '020')
        self.message.append('Rule ' + self.unique_id + ' has been renamed to rule port_map_005.')
