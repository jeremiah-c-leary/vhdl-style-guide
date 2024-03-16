# -*- coding: utf-8 -*-

from vsg import parser, violation
from vsg.rule_group import indent
from vsg.rules import utils as rules_utils


class token_indent(indent.Rule):
    """
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of token types
       token type to apply the indent rule
    """

    def __init__(self, lTokens):
        super().__init__()
        self.lTokens = lTokens

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_at_beginning_of_line_matching(self.lTokens)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if indent_should_be_zero_but_has_leading_whitespace(lTokens):
                create_zero_indent_violation(self, oToi)
            elif indent_exists_but_is_incorrect(self, lTokens):
                create_indent_violation(self, oToi, lTokens)
            elif no_indent_exists_but_should(self, lTokens):
                create_no_indent_violation(self, oToi, lTokens)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if oViolation.get_action() == "remove_whitespace":
            oViolation.set_tokens([lTokens[1]])
        elif oViolation.get_action() == "adjust_whitespace":
            if self.indent_style == "spaces":
                lTokens[0].set_value(lTokens[1].get_indent() * self.indent_size * " ")
                lTokens[0].has_tab = False
            elif self.indent_style == "smart_tabs":
                lTokens[0].set_value(lTokens[1].get_indent() * "\t")
                lTokens[0].has_tab = True
            oViolation.set_tokens(lTokens)
        elif oViolation.get_action() == "add_whitespace":
            if self.indent_style == "spaces":
                rules_utils.insert_whitespace(lTokens, 0, lTokens[0].get_indent() * self.indent_size)
            else:
                rules_utils.insert_whitespace(lTokens, 0, lTokens[0].get_indent(), "\t")
            oViolation.set_tokens(lTokens)


def indent_should_be_zero_but_has_leading_whitespace(lTokens):
    if len(lTokens) == 2 and lTokens[1].get_indent() == 0:
        return True
    return False


def create_zero_indent_violation(self, oToi):
    sSolution = "Indent level 0"
    create_violation(self, oToi, sSolution, "remove_whitespace")


def indent_exists_but_is_incorrect(self, lTokens):
    if len(lTokens) == 2:
        if lTokens[1].get_indent() is None:
            return False
        sWhitespace = lTokens[0].get_value()
        if self.indent_style == "spaces":
            sIndent = " " * (self.indent_size * lTokens[1].get_indent())
        else:
            sIndent = "\t" * (lTokens[1].get_indent())
        if sWhitespace != sIndent:
            return True
    return False


def create_indent_violation(self, oToi, lTokens):
    sSolution = create_adjust_indent_solution(self, lTokens)
    create_violation(self, oToi, sSolution, "adjust_whitespace")


def no_indent_exists_but_should(self, lTokens):
    if not len(lTokens) == 1:
        return False

    if lTokens[0].get_indent() is None:
        return False
    if self.indent_size == 0:
        return False
    if lTokens[0].get_indent() != 0:
        return True

    return False


def create_no_indent_violation(self, oToi, lTokens):
    sSolution = create_no_indent_solution(self, lTokens)
    create_violation(self, oToi, sSolution, "add_whitespace")


def create_violation(self, oToi, sSolution, sAction):
    oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
    oViolation.set_action(sAction)
    self.add_violation(oViolation)


def create_adjust_indent_solution(self, lTokens):
    return create_indent_solution(self, lTokens[1])


def create_no_indent_solution(self, lTokens):
    return create_indent_solution(self, lTokens[0])


def create_indent_solution(self, oToken):
    iIndentLevel = oToken.get_indent()
    if self.indent_style == "spaces":
        sSolution = "Use " + str(iIndentLevel * self.indent_size) + " spaces for indent"
    elif self.indent_style == "smart_tabs":
        sSolution = "Use " + str(iIndentLevel) + " tab(s) for indent"
    return sSolution
