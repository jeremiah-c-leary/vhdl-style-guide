
from vsg.depricated_rule import Depricated


class rule_003(Depricated):

    def __init__(self):
        Depricated.__init__(self, 'type', '003')
        self.message.append('Rule ' + self.unique_id + ' has been replaced with the following rules:')
        self.message.append('  function_015')
        self.message.append('  package_019')
        self.message.append('  procedure_010')
        self.message.append('  architecture_029')
