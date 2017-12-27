
from vsg.rules import indent_rule


class rule_004(indent_rule):
    '''
    Procedure rule 004 checks the indent of procedure parameters.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'procedure', '004', 'isProcedureParameter', 'isProcedureKeyword')
