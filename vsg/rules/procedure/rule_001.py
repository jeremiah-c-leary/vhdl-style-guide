
from vsg.rules import indent_rule


class rule_001(indent_rule):
    '''
    Procedure rule 001 checks the indent of procedures.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'procedure', '001', 'isProcedureKeyword')
