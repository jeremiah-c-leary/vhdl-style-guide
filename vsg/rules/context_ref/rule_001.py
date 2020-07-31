
from vsg import parser
from vsg.rules import indent_item_rule


class rule_001(indent_item_rule):
    '''
    Checks for indent on the context reference keyword.
    '''
    def __init__(self):
        indent_item_rule.__init__(self, 'context_ref', '001', parser.context_reference_keyword)
