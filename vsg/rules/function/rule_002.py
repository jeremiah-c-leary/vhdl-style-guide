
from vsg.depricated_rule import Depricated


class rule_002(Depricated):

    def __init__(self):
        Depricated.__init__(self, 'function', '002')
        self.message.append('Rule ' + self.unique_id + ' has been merged into function_100.')
