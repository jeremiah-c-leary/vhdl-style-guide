
from vsg.depricated_rule import Depricated


class rule_030(Depricated):

    def __init__(self):
        Depricated.__init__(self, 'instantiation', '030')
        self.message.append('Rule ' + self.unique_id + ' has been renamed to generic_map_007.')
