
from vsg import parser
from vsg import rule


class Rule(rule.Rule):

    def __init__(self, name, identifier):
        rule.Rule.__init__(self, name=name, identifier=identifier)
        self.fixable = False
        self.disable = True
        self.phase = 1

        self.min_height = 3
        self.configuration.append('min_height')
        self.allow_indenting = True
        self.configuration.append('allow_indenting')

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_consecutive_lines_starting_with_token(parser.comment, self.min_height)

    def fix(self, oFile, dFixOnly=None):
        '''
        Applies fixes for any rule violations.
        '''
        self.analyze(oFile)

