
from vsg.rules import indent_rule


class rule_002(indent_rule):
    '''
    Port rule 002 checks indentation of the "port" keyword.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'port', '002', 'isPortKeyword')
