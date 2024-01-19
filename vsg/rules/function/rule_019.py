
from vsg.rules import multiline_subprogram_specification_structure as Rule

from vsg import token

oSubprogramSpecification = token.function_specification

lTokenPairs = []
lTokenPairs.append([token.function_specification.function_keyword, token.function_specification.close_parenthesis])


class rule_019(Rule):
    '''
    This rule checks the structure of function specifications.

    |configuring_multiline_subprogram_specification_statement_rules_link|

    **Violation**

    .. code-block:: vhdl

        function my_function (i_arg1 : integer; i_arg2 : boolean) return integer;

    **Fix**

    .. code-block:: vhdl

        function my_function (
          i_arg1 : integer;
          i_arg2 : boolean
        ) return integer;

    '''

    def __init__(self):
        Rule.__init__(self, 'function', '019')
        self.lTokenPairs = lTokenPairs
        self.oSubprogramSpecification = oSubprogramSpecification
