# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import consistent_subprogram_parameter_token_case as Rule


class rule_509(Rule):
    """
    This rule checks for consistent capitalization of parameter names within the subprogram body.

    **Violation**

    .. code-block:: vhdl

      procedure my_proc (
        param1 : in integer;
        param2 : out integer
      ) is
      begin

        SIG <= PARAM1 + PARAM2;

      end procedure my_proc;

    **Fix**

    .. code-block:: vhdl

      procedure my_proc (
        param1 : in integer;
        param2 : out integer
      ) is
      begin

        SIG <= param1 + param2;

      end procedure my_proc;
    """

    def __init__(self):
        super().__init__()
        self.groups.append("case::name")
        self.subprogram_token = token.procedure_specification
        self.start_token = token.procedure_specification.procedure_keyword
