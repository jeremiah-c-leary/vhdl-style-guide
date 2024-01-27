
from vsg import rule


class Rule(rule.Rule):

    def __init__(self):
        rule.Rule.__init__(self)
        self.fixable = False
        self.disable = True
        self.phase = 0
        self.proposed = True
        self.message = []
        self.configuration = []
        self.message.append('Rule ' + self.unique_id + ' has not been implemented.')

    def print_output(self):
        lReturn = [f'ERROR [config-001] Rule {self.unique_id} has not been implemented.']
        for sLine in self.message:
            lReturn.append('  ' + sLine)
        return lReturn
