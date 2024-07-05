# -*- coding: utf-8 -*-

from vsg import violation
from vsg.rule_group import length


class number_of_lines_between_tokens(length.Rule):
    """
    Checks the number of lines between tokens do not exceed a specified number

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    """

    def __init__(self, oLeftToken, oRightToken, iLines):
        super().__init__()
        self.length = iLines
        self.oLeftToken = oLeftToken
        self.oRightToken = oRightToken

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_line_count_between_tokens(self.oLeftToken, self.oRightToken)

    def _analyze(self, lToi):
        for oToi in lToi:
            if oToi.get_meta_data("length") > self.length:
                sSolution = "Reduce process to less than " + str(self.length) + " lines"
                oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)

                self.add_violation(oViolation)
