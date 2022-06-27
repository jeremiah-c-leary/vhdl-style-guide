
from vsg.deprecated_rule import Rule


class rule_600(Rule):
    '''
    This rule has been moved to library_500.
    '''

    def __init__(self):
        Rule.__init__(self, 'library', '600')
        self.message.append('Rule ' + self.unique_id + ' has been moved to rule library_500.')