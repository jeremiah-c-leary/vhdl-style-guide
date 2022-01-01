
from vsg.rule_group import indent
from vsg import parser
from vsg import violation

from vsg.rules import utils as rules_utils


class token_indent(indent.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of token types
       token type to apply the indent rule
    '''

    def __init__(self, name, identifier, lTokens):
        indent.Rule.__init__(self, name=name, identifier=identifier)
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
        if oViolation.get_action() == 'remove_whitespace':
            oViolation.set_tokens([lTokens[1]])
        elif oViolation.get_action() == 'adjust_whitespace':
            lTokens[0].set_value(lTokens[1].get_indent() * self.indentSize * ' ')
            oViolation.set_tokens(lTokens)
        elif oViolation.get_action() == 'add_whitespace':
            rules_utils.insert_whitespace(lTokens, 0, lTokens[0].get_indent() * self.indentSize)
            oViolation.set_tokens(lTokens)


def indent_should_be_zero_but_has_leading_whitespace(lTokens):
    if len(lTokens) == 2 and lTokens[1].get_indent() == 0:
        return True
    return False


def create_zero_indent_violation(self, oToi):
    sSolution = "Indent level 0"
    create_violation(self, oToi, sSolution, 'remove_whitespace')


def indent_exists_but_is_incorrect(self, lTokens):
    if len(lTokens) == 2:
        if lTokens[1].get_indent() is None:
            return False
        iWhitespace = len(lTokens[0].get_value())
        iIndent = self.indentSize * lTokens[1].get_indent()
        if iWhitespace != iIndent:
            return True
    return False


def create_indent_violation(self, oToi, lTokens):
    sSolution = 'Indent level ' + str(lTokens[1].get_indent())
    create_violation(self, oToi, sSolution, 'adjust_whitespace')


def no_indent_exists_but_should(self, lTokens):
    if not len(lTokens) == 1:
        return False

    if lTokens[0].get_indent() is None:
        return False
    if self.indentSize == 0:
        return False
    if lTokens[0].get_indent() != 0:
        return True

    return False


def create_no_indent_violation(self, oToi, lTokens):
    sSolution = 'Indent level ' + str(lTokens[0].get_indent())
    create_violation(self, oToi, sSolution, 'add_whitespace')


def create_violation(self, oToi, sSolution, sAction):
    oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
    oViolation.set_action(sAction)
    self.add_violation(oViolation)
