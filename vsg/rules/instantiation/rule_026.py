
from vsg.depricated_rule import Depricated


class rule_026(Depricated):

    def __init__(self):
        Depricated.__init__(self, 'instantiation', '026')
        self.message.append('Rule ' + self.unique_id + ' has been renamed to generic_map_003.')
