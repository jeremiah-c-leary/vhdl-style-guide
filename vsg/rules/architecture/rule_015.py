
from vsg.rules import line_below_rule


class rule_015(line_below_rule):
    '''
    Architecture rule 015 checks for a blank line below the architecture keyword.
    '''

    def __init__(self):
        line_below_rule.__init__(self, 'architecture', '015', 'isArchitectureKeyword')
