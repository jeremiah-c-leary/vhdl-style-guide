
from vsg.rules import indent_rule


class rule_002(indent_rule):
    '''
    Procedure rule 002 checks the indent of the **begin** keyword.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'procedure', '002', 'isProcedureBegin')
