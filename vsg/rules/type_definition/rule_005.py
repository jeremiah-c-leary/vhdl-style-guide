
from vsg.rules import indent_rule


class rule_005(indent_rule):
    '''
    Type rule 005 checks for the proper indentation of multiline types.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'type', '005', 'insideTypeEnumerated', 'isTypeEnumeratedKeyword')
        self.solution = 'Ensure proper indentation.'
