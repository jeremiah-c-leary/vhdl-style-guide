
from vsg.rules import single_space_after_rule


class rule_011(single_space_after_rule):
    '''
    Entity rule 011 checks for a single space after the "end" keyword
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'entity', '011', 'isEndEntityDeclaration', 'end')
        self.solution = 'Reduce spaces after "end" keyword to one.'
