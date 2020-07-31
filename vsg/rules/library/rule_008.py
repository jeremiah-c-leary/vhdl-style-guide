
from vsg import parser
from vsg.rules import indent_item_rule


class rule_008(indent_item_rule):
    '''
    Checks for indent off the use keyword.
    '''
    def __init__(self):
        indent_item_rule.__init__(self, 'library', '008', parser.use_keyword)
