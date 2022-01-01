
from vsg import parser
from vsg import violation

from vsg.token import report_statement

from vsg.rules import utils as rules_utils
from vsg.rule_group import alignment
from vsg.vhdlFile import utils


class rule_400(alignment.Rule):
    '''
    This rule checks the alignment of the report expressions.

    .. NOTE:: There is a configuration option **alignment** which changes the indent location of multiple lines.

    alignment set to 'report' (Default)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    **Violation**

    .. code-block:: vhdl

       report "FIFO width is limited" &
       " to 16 bits."
         severity FAILURE;

    **Fix**

    .. code-block:: vhdl

       report "FIFO width is limited" &
              " to 16 bits."
         severity FAILURE;

    alignment set to 'left'
    ^^^^^^^^^^^^^^^^^^^^^^^

    **Violation**

    .. code-block:: vhdl

       report "FIFO width is limited" &
       " to 16 bits."
         severity FAILURE;

    **Fix**

    .. code-block:: vhdl

         report "FIFO width is limited" &
             " to 16 bits."
           severity FAILURE;
    '''

    def __init__(self):
        alignment.Rule.__init__(self, name="report_statement", identifier="400")
        self.alignment = 'report'
        self.configuration.append('alignment')

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_starting_with_token_and_ending_with_one_of_possible_tokens([report_statement.report_keyword], [report_statement.severity_keyword, report_statement.semicolon], True, False, True)

    def analyze(self, oFile):

        self._print_debug_message('Analyzing rule: ' + self.unique_id)
        lToi = self._get_tokens_of_interest(oFile)

        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)

            iSpaces = self._calculate_column(oFile, oToi, lTokens)

            for iToken, oToken in enumerate(lTokens):
                if isinstance(oToken, parser.carriage_return):
                    iLine += 1
                    if isinstance(lTokens[iToken + 1], parser.whitespace):
                        if len(lTokens[iToken + 1].get_value()) != iSpaces:
                            self._create_violation(iLine, iSpaces, 'adjust', oToi.extract_tokens(iToken + 1, iToken + 1))
                    elif isinstance(lTokens[iToken + 1], parser.blank_line):
                            continue
                    else:
                        self._create_violation(iLine, iSpaces, 'insert', oToi.extract_tokens(iToken + 1, iToken + 1))

    def fix(self, oFile, dFixOnly=None):
        '''
        Applies fixes for any rule violations.
        '''
        if self.fixable:
            self.analyze(oFile)
            self._print_debug_message('Fixing rule: ' + self.unique_id)
            self._filter_out_fix_only_violations(dFixOnly)
            for oViolation in self.violations[::-1]:
                self._fix_violation(oViolation)
            oFile.update(self.violations)
            self.clear_violations()

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()

        if dAction['action'] == 'adjust':
            lTokens[0].set_value(' '*dAction['column'])
        else:
            rules_utils.insert_whitespace(lTokens, 0, dAction['column'])

        oViolation.set_tokens(lTokens)

    def _create_violation(self, iLine, iSpaces, sAction, lTokens):
        sSolution = 'Indent line to column ' + str(iSpaces)
        oViolation = violation.New(iLine, lTokens, sSolution)
        dAction = {}
        dAction['action'] = sAction
        dAction['column'] = iSpaces
        oViolation.set_action(dAction)
        self.add_violation(oViolation)

    def _calculate_column(self, oFile, oToi, lTokens):
        if self.alignment == 'report':
            iSpaces = oFile.get_column_of_token_index(oToi.get_start_index()) + 7
        else:
            iSpaces = (lTokens[0].indent + 2) * self.indentSize
        return iSpaces
