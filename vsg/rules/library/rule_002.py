
from vsg.rules import single_space_after_rule


class rule_002(single_space_after_rule):
    '''
    Library rule 002 checks for a single space after the library keyword.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'library', '002', 'isLibrary', 'library')
        self.solution = 'Remove extra spaces after "library" keyword.'
