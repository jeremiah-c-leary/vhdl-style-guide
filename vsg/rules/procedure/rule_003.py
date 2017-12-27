
from vsg.rules import indent_rule


class rule_003(indent_rule):
    '''
    Procedure rule 003 checks the indent of the **begin** keyword.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'procedure', '003', 'isProcedureEnd', 'isProcedureParameter')
