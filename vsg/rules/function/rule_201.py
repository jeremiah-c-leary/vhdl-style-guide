
from vsg.depricated_rule import Depricated


class rule_201(Depricated):

    def __init__(self):
        Depricated.__init__(self, 'function', '201')
        self.message.append('Rule ' + self.unique_id + ' has been moved to rule subprogram_body_201.')
