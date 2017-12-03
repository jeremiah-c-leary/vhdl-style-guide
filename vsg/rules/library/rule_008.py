
from vsg.rules import indent_rule


class rule_008(indent_rule):
    '''
    Library rule 008 checks indentation of the use keyword.
    '''

    def __init__(self):
        indent_rule.__init__(self)
        self.name = 'library'
        self.identifier = '008'
        self.sTrigger = 'isLibraryUse'
