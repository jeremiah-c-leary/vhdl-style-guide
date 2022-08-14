
from vsg import parser
from vsg import violation

from vsg.token import assertion
from vsg.token import assertion_statement
from vsg.token import concurrent_assertion_statement

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

       assert WIDTH > 16
         report "FIFO width is limited" &
       " to 16 bits."
         severity FAILURE;

    **Fix**

    .. code-block:: vhdl

       assert WIDTH > 16
         report "FIFO width is limited" &
                " to 16 bits."
         severity FAILURE;

    alignment set to 'left'
    ^^^^^^^^^^^^^^^^^^^^^^^

    **Violation**

    .. code-block:: vhdl

       assert WIDTH > 16
         report "FIFO width is limited" &
       " to 16 bits."
         severity FAILURE;

    **Fix**

    .. code-block:: vhdl

       assert WIDTH > 16
         report "FIFO width is limited" &
           " to 16 bits."
         severity FAILURE;
    '''

    def __init__(self):
        alignment.Rule.__init__(self, name="assert", identifier="400")
        self.alignment = 'report'
        self.configuration.append('alignment')
        self.phase = 4

    def _get_tokens_of_interest(self, oFile):
        lReturn = []
        lToi = oFile.get_tokens_starting_with_token_and_ending_with_one_of_possible_tokens([assertion.report_keyword], [assertion.severity_keyword, assertion_statement.semicolon, concurrent_assertion_statement.semicolon], True, False, True)
        for oToi in lToi:
            lTokens = oToi.get_tokens()
            iSpaces = self._calculate_column(oFile, oToi, lTokens)
            sWhitespace = self._expected_whitespace(oFile, oToi, lTokens)

            lIndexes = get_index_after_carriage_return(lTokens)

            for iIndex in lIndexes:
                myToi = oToi.extract_tokens(iIndex, iIndex)
                myToi.set_meta_data('iSpaces', self._calculate_column(oFile, oToi, lTokens))
                myToi.set_meta_data('sWhitespace', self._expected_whitespace(oFile, oToi, lTokens))
                lReturn.append(myToi)

        return lReturn

    def _analyze(self, lToi):
        for oToi in lToi:
            self._check_leading_whitespace(oToi)

    def _check_leading_whitespace(self, oToi):
        sWhitespace = oToi.get_meta_data('sWhitespace')
        oToken = oToi.get_tokens()[0]
        if isinstance(oToken, parser.whitespace):
            if oToken.get_value() != sWhitespace:
                self._create_violation(oToi, 'adjust')
        else:
            self._create_violation(oToi, 'insert')

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()

        if dAction['action'] == 'adjust':
            lTokens[0].set_value(dAction['whitespace'])
        else:
            rules_utils.insert_new_whitespace(lTokens, 0, dAction['whitespace'])

        oViolation.set_tokens(lTokens)

    def _create_violation(self, oToi, sAction):
        sSolution = 'Indent line to column ' + str(oToi.get_meta_data('iSpaces'))
        oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
        dAction = {}
        dAction['action'] = sAction
        dAction['column'] = oToi.get_meta_data('iSpaces')
        dAction['whitespace'] = oToi.get_meta_data('sWhitespace')
        oViolation.set_action(dAction)
        self.add_violation(oViolation)

    def _calculate_column(self, oFile, oToi, lTokens):
        if self.alignment == 'report':
            iSpaces = oFile.get_column_of_token_index(oToi.get_start_index()) + 7
        else:
            iSpaces = (lTokens[0].indent + 1) * self.indentSize
        return iSpaces

    def _expected_whitespace(self, oFile, oToi, lTokens):
        if self.indentStyle == 'smart_tabs':
            if self.alignment == 'report':
                return (lTokens[0].indent) * '\t' + ' ' * len('report ')
            else:
                return (lTokens[0].indent + 1) * '\t'
        else:
            if self.alignment == 'report':
                iSpaces = oFile.get_column_of_token_index(oToi.get_start_index()) + 7
            else:
                iSpaces = (lTokens[0].indent + 1) * self.indentSize
            return iSpaces * ' '

def get_index_after_carriage_return(lTokens):
    lReturn = []
    for iToken, oToken in enumerate(lTokens):
        if isinstance(oToken, parser.carriage_return):
            lReturn.append(iToken + 1)
    return lReturn
