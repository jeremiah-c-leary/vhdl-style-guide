
from vsg.depricated_rule import Depricated


class rule_005(Depricated):

    def __init__(self):
        Depricated.__init__(self, 'sequential', '005')
        self.message.append('Rule ' + self.unique_id + ' has been merged into process_400.')
