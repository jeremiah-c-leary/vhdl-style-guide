
from vsg.rules import indent_rule


class rule_005(indent_rule):
    '''
    Procedure rule 005 checks the indent of lines in the procedure declarative region.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'procedure', '005', 'insideProcedureDeclarative', 'isBlank')
