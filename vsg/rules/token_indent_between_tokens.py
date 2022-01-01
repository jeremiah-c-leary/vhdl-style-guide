
from vsg.rule_group import indent
from vsg import parser
from vsg import violation

from vsg.rules import utils as rules_utils


class token_indent_between_tokens(indent.Rule):
    '''
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    trigger : parser object type
       object type to apply the case check against
    '''

    def __init__(self, name, identifier, lTokens, oStart, oEnd, bInclusive=False):
        indent.Rule.__init__(self, name=name, identifier=identifier)
        self.lTokens = lTokens
        self.oStart = oStart
        self.oEnd = oEnd
        self.bInclusive = bInclusive

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_at_beginning_of_line_matching_between_tokens(self.lTokens, self.oStart, self.oEnd, self.bInclusive)

    def _analyze(self, lToi):
        for oToi in lToi:
            lTokens = oToi.get_tokens()

            if len(lTokens) == 2 and lTokens[1].get_indent() == 0:
                sSolution = "Indent level 0"
                oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                oViolation.set_action('remove_whitespace')
                self.add_violation(oViolation)
            elif len(lTokens) == 2:
                iWhitespace = len(lTokens[0].get_value())
                iIndent = self.indentSize * lTokens[1].get_indent()
                if iWhitespace != iIndent:
                    sSolution = 'Indent level ' + str(lTokens[1].get_indent())
                    oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                    oViolation.set_action('adjust_whitespace')
                    self.add_violation(oViolation)
            elif len(lTokens) == 1:
                if lTokens[0].get_indent() != 0:
                    sSolution = 'Indent level ' + str(lTokens[0].get_indent())
                    oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                    oViolation.set_action('add_whitespace')
                    self.add_violation(oViolation)

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
