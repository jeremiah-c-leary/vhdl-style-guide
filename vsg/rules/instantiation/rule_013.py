
from vsg.depricated_rule import Depricated


class rule_013(Depricated):
    '''
    Constant rule 601 checks for prefixes in package identifiers.
    '''

    def __init__(self):
        Depricated.__init__(self, 'instantiation', '013')
        self.message.append('Rule ' + self.unique_id + ' has been renamed to rule generic_map_001.')
