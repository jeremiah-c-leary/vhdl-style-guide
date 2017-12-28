
from vsg.rules import uppercase_word_rule


class rule_008(uppercase_word_rule):
    '''Component rule 008 checks the component name is uppercase in the component declaration line.'''

    def __init__(self):
        uppercase_word_rule.__init__(self, 'component', '008', 'isComponentDeclaration', 1)
        self.solution = 'Change component name to all uppercase.'
