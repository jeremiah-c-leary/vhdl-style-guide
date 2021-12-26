
from vsg import deprecated_rule


class rule_003(deprecated_rule.Rule):
    '''
    This rule was depricated and replaced with rules:

    * `function_015 <function_rules.html#function-015>`_
    * `package_019 <package_rules.html#package-019>`_
    * `procedure_010 <procedure_rules.html#procedure-010>`_
    * `architecture_029 <architecture_rules.html#architecture-029>`_
    '''

    def __init__(self):
        deprecated_rule.Rule.__init__(self, 'file', '003')
        self.message.append('Rule ' + self.unique_id + ' was replaced with the following rules:')
        self.message.append('  function_015')
        self.message.append('  package_019')
        self.message.append('  procedure_010')
        self.message.append('  architecture_029')
