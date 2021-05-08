
from vsg.depricated_rule import Depricated


class rule_014(Depricated):

    def __init__(self):
        Depricated.__init__(self, 'instantiation', '014')
        self.message.append('Rule ' + self.unique_id + ' has been renamed to rule generic_map_004.')
