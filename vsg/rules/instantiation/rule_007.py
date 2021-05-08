
from vsg.depricated_rule import Depricated


class rule_007(Depricated):

    def __init__(self):
        Depricated.__init__(self, 'instantiation', '007')
        self.message.append('Rule ' + self.unique_id + ' has been renamed to port_map_004.')
