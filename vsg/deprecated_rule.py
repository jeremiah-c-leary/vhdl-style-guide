
from vsg import rule


class Rule(rule.Rule):

    def __init__(self):
        rule.Rule.__init__(self)
        self.fixable = False
        self.disable = True
        self.phase = 0
        self.deprecated = True
        self.message = []
        self.configuration = []

    def print_output(self):
        lReturn = [f'ERROR [config-001] Rule {self.unique_id} has been deprecated.']
        for sLine in self.message:
            lReturn.append('  ' + sLine)
        return lReturn
