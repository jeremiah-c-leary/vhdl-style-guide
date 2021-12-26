
from vsg import parser
from vsg import violation

from vsg.rules import utils
from vsg.rule_group import structure


class rule_011(structure.Rule):
    '''
    This rule checks for in-line comments and moves them to the line above.
    The indent of the comment will be set to the indent of the current line.

    .. NOTE:: This rule is disabled by default.

    **Violation**

    .. code-block:: vhdl

       a <= b; -- Assign signal

    **Fix**

    .. code-block:: vhdl

       -- Assign signal
       a <= b;
    '''

    def __init__(self):
        structure.Rule.__init__(self, name='comment', identifier='011')
        self.solution = 'Move inline comment to previous line.'
        self.disable = True
        self.lTokens = [parser.comment]

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_line_which_includes_tokens(self.lTokens)

    def _analyze(self, lToi):
        for oToi in lToi:
            if line_starts_with_comment(oToi):
                continue
            self._check_for_inline_comment(oToi)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()

        lTemp = lTokens[dAction['iToken']:]
        lTemp.append(parser.carriage_return())
        lTemp.extend(lTokens[:dAction['iToken']])
#        lTemp[dAction['index']].set_indent(dAction['indent'])

        oViolation.set_tokens(lTemp)

    def _check_for_inline_comment(self, oToi):
        iLine, lTokens = utils.get_toi_parameters(oToi)
        iToken = len(lTokens) - 1
        if line_has_inline_comment(lTokens, iToken):
            dAction = create_action(lTokens, iToken)
            oViolation = create_violation(iLine, oToi, self.solution, dAction)
            self.add_violation(oViolation)


def line_starts_with_comment(oToi):
    if utils.does_line_start_with_comment(oToi.get_tokens()):
        return True
    return False


def line_has_inline_comment(lTokens, iToken):
    if isinstance(lTokens[iToken], parser.comment):
        return True
    return False


def create_action(lTokens, iToken):
    dAction = {}
    if isinstance(lTokens[iToken - 1], parser.whitespace):
        dAction['iToken'] = iToken - 1
        dAction['index'] = 1
    else:
        dAction['iToken'] = iToken
        dAction['index'] = 0
#    dAction['indent'] = utils.get_indent_of_line(lTokens)
    return dAction


def create_violation(iLine, oToi, solution, dAction):
    oViolation = violation.New(iLine, oToi, solution)
    oViolation.set_action(dAction)
    return oViolation
