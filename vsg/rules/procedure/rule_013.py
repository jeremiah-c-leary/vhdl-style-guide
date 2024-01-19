
from vsg.rules import multiline_subprogram_specification_structure as Rule

from vsg import token

oSubprogramSpecification = token.procedure_specification

lTokenPairs = []
lTokenPairs.append([token.procedure_specification.procedure_keyword, token.procedure_specification.close_parenthesis])


class rule_013(Rule):
    '''
    This rule checks the structure of procedure specifications.

    |configuring_multiline_subprogram_specification_statement_rules_link|

    **Violation**

    .. code-block:: vhdl

        procedure my_procedure (i_arg1 : integer;i_arg2 : boolean);

    **Fix**

    .. code-block:: vhdl

        procedure my_procedure (
          i_arg1 : integer;
          i_arg2 : boolean
        );

    '''

    def __init__(self):
        Rule.__init__(self, 'procedure', '013')
        self.lTokenPairs = lTokenPairs
        self.oSubprogramSpecification = oSubprogramSpecification
