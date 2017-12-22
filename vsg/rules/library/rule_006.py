

from vsg.rules import single_space_after_rule


class rule_006(single_space_after_rule):
    '''
    Library rule 006 checks for a single space after the use keyword.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'library', '006', 'isLibraryUse', 'use')
        self.solution = 'Remove extra spaces after "use" keyword.'
