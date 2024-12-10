# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import consistent_subprogram_parameter_token_case as Rule


class rule_508(Rule):
    """
    This rule checks for consistent capitalization of parameter names within the subprogram body.

    **Violation**

    .. code-block:: vhdl

      function my_func (
        param1 : in integer;
        param2 : out integer
      ) return integer is
      begin

        SIG <= PARAM1 + PARAM2;

      end function my_func;

    **Fix**

    .. code-block:: vhdl

      function my_func (
        param1 : in integer;
        param2 : out integer
      ) return integer is
      begin

        SIG <= param1 + param2;

      end function my_func;

       end architecture rtl;
    """

    def __init__(self):
        super().__init__()
        self.groups.append("case::name")
        self.subprogram_token = token.function_specification
        self.start_token = token.function_specification.function_keyword
