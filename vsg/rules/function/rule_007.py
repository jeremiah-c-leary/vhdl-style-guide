
from vsg.depricated_rule import Depricated


class rule_007(Depricated):

    def __init__(self):
        Depricated.__init__(self, 'function', '007')
        self.message.append('Rule ' + self.unique_id + ' has been moved to rule subprogram_body_205.')
