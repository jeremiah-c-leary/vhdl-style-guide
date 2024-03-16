# -*- coding: utf-8 -*-

from vsg import parser
from vsg.rules import remove_spaces_before_token_rule


class rule_004(remove_spaces_before_token_rule):
    """
    This rule checks for spaces before commas.

    **Violation**

    .. code-block:: vhdl

       wr_en => wr_en    ,
       rd_en => rd_en,

    **Fix**

    .. code-block:: vhdl

       wr_en => wr_en,
       rd_en => rd_en,
    """

    def __init__(self):
        super().__init__(parser.comma)
        self.solution = "Remove spaces before commas."
        self.configuration_documentation_link = None
