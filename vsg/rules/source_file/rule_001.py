
from vsg import rule


class rule_001(rule.rule):
    '''
    Checks the length of the file and determines if the file is empty.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'source_file', '001')
        self.phase = 1
        # These are filled out when creating a new rule
        self.name = 'source_file'
        self.identifier = '001'
        self.fixable = False
        self.solution = 'File not found.'

    def analyze(self, oFile):
        if len(oFile.lines) == 1:
            self.add_violation(0)
