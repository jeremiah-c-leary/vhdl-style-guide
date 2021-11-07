
from vsg import deprecated_rule


class rule_003(deprecated_rule.Rule):

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'file_statement', '003')
        self.message.append('Rule ' + self.unique_id + ' was replaced with the following rules:')
        self.message.append('  function_015')
        self.message.append('  package_019')
        self.message.append('  procedure_010')
        self.message.append('  architecture_029')
