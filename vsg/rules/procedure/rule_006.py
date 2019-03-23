
from vsg.rules import indent_rule


class rule_006(indent_rule):
    '''
    Procedure rule 001 checks the indent of procedures.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'procedure', '006', 'isProcedureIs', 'isProcedureParameterEnd')
