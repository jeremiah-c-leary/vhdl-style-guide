
from vsg import deprecated_rule


class rule_002(deprecated_rule.Rule):
    '''
    This rule has been split into the following rules:

    * :ref:`architecture_030`
    * :ref:`architecture_031`
    * :ref:`architecture_032`
    * :ref:`architecture_033`
    '''

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'architecture', '002')
        self.message.append('Rule ' + self.unique_id + ' has been split into the following rules:')
        self.message.append('  architecture_030')
        self.message.append('  architecture_031')
        self.message.append('  architecture_032')
        self.message.append('  architecture_033')
