

from vsg import rule
from vsg import utils
from vsg import violation


class is_token_value_one_of(rule.Rule):
    '''
    Checks if a token value is in a list of provided values.
    '''

    def __init__(self, name, identifier, token):
        rule.Rule.__init__(self, name, identifier)
        self.names = []
        self.solution = None
        self.phase = 7
        self.fixable = False
        self.disable = True
        self.configuration.append('names')
        self.token = token


    def analyze(self, oFile):
        lower_names = []
        for sName in self.names:
            lower_names.append(sName.lower())

        lToi = oFile.get_tokens_matching([self.token])
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if not lTokens[0].get_value().lower() in lower_names:
                self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))
