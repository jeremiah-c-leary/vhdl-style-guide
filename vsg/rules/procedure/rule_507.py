# -*- coding: utf-8 -*-

from vsg import parser, token
from vsg.rules import consistent_token_case as Rule

lTokens = []
lTokens.append(token.procedure_specification.designator)

lNames = []
lNames.append(token.procedure_call.procedure_name)


class rule_507(Rule):
    """
    This rule checks for consistent capitalization of procedure names.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is

         procedure average_samples is
         begin
         end procedure average_samples

       begin

         Average_samples;

         PROC1 : process () is
         begin

            AVERAGE_SAMPLES;

         end process;

       end architecture rtl;

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is

         procedure average_samples is
         begin
         end procedure average_samples

       begin

         average_samples;

         PROC1 : process () is
         begin

            average_samples;

         end process;

       end architecture rtl;
    """

    def __init__(self):
        super().__init__(lTokens, lNames)
