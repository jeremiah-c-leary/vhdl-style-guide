
from vsg.rules import indent_rule


class rule_009(indent_rule):
    '''Component rule 009 checks for spaces before the "end" keyword.'''

    def __init__(self):
        indent_rule.__init__(self, 'component', '009', 'isComponentEnd')
        self.solution = 'Ensure proper indentation.'
