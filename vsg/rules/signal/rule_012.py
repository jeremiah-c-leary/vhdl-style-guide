
from vsg import parser
from vsg import token
from vsg import violation

from vsg.rules import utils as rules_utils
from vsg.rule_group import alignment
from vsg.vhdlFile import utils


class rule_012(alignment.Rule):
    '''
    This rule checks multiple signal declarations on a single line are column aligned.

    .. NOTE::
        This rule will only cover two signals on a single line.

    **Violation**

    .. code-block:: vhdl

       signal wr_en, wr_en_f             : std_logic;
       signal rd_en_f, rd_en             : std_logic;
       signal chip_select, chip_select_f : t_user_defined_type;

    **Fix**

    .. code-block:: vhdl

       signal wr_en,       wr_en_f       : std_logic;
       signal rd_en_f,     rd_en         : std_logic;
       signal chip_select, chip_select_f : t_user_defined_type;
    '''

    def __init__(self):
        alignment.Rule.__init__(self, 'signal', '012')
        self.subphase = 2
        self.left_token = token.architecture_body.is_keyword
        self.right_token = token.architecture_body.begin_keyword
        self.lUnless = []
        self.lUnless.append([token.subprogram_body.is_keyword,token.subprogram_body.begin_keyword])
        ## attributes below are configurable by the user

        self.compact_alignment = True
        self.configuration.append('compact_alignment')

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_bounded_by(self.left_token, self.right_token)

    def _analyze(self, lToi):
        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)
            iColumn = 0
            bSignalFound = False
            bSkip = False
            dAnalysis = {}
            dTemp = {}
            for iToken, oToken in enumerate(lTokens):

               iLine = utils.increment_line_number(iLine, oToken)

               if isinstance(oToken, parser.carriage_return):
                   iColumn = 0
               else:
                   iColumn += len(oToken.get_value())

               bSkip = check_for_exclusions(bSkip, oToken, self.lUnless)
               if bSkip:
                   continue

               bSignalFound = check_for_signal_declaration(bSignalFound, oToken)
               if not bSignalFound:
                   iComma = 0
                   continue

               if isinstance(oToken, token.signal_declaration.colon):
                   bSignalFound = False
                   if iComma == 1:
                       dAnalysis[dTemp['line_number']] = dTemp
                   continue

               if isinstance(oToken, parser.comma):
                   iComma += 1
                   if iComma == 2:
                       bSignalFound = False
                       continue

                   dTemp = {}
                   dTemp['comma_column'] = iColumn
                   dTemp['comma_index'] = iToken
                   dTemp['line_number'] = iLine
                   if utils.are_next_consecutive_token_types([parser.whitespace, token.signal_declaration.identifier], iToken + 1, lTokens):
                       dTemp['identifier_column'] = iColumn + len(lTokens[iToken + 1].get_value())
                       dTemp['token_index'] = iToken + 2
                       dTemp['token_value'] = lTokens[iToken + 2].get_value()
                   elif utils.are_next_consecutive_token_types([token.signal_declaration.identifier], iToken + 1, lTokens):
                       dTemp['identifier_column'] = iColumn + 1
                       dTemp['token_index'] = iToken + 1
                       dTemp['token_value'] = lTokens[iToken + 1].get_value()
                   else:
                       bSignalFound = False

            add_adjustments_to_dAnalysis(dAnalysis, self.compact_alignment)

            for iKey in list(dAnalysis.keys()):
                if dAnalysis[iKey]['adjust'] != 0:
                    oLineTokens = oToi.extract_tokens(dAnalysis[iKey]['comma_index'], dAnalysis[iKey]['token_index'])
                    sSolution = 'Move ' + dAnalysis[iKey]['token_value'] + ' ' + str(dAnalysis[iKey]['adjust']) + ' columns'
                    oViolation = violation.New(dAnalysis[iKey]['line_number'], oLineTokens, sSolution)
                    oViolation.set_action(dAnalysis[iKey])
                    self.add_violation(oViolation)

            dAnalysis = {}

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()

        if len(lTokens) == 2:
            rules_utils.insert_whitespace(lTokens, 1)
        else:
            iLen = len(lTokens[1].get_value()) + dAction['adjust']
            lTokens[1].set_value(' '*iLen)

        oViolation.set_tokens(lTokens)


def add_adjustments_to_dAnalysis(dAnalysis, compact_alignment):
    iMaxLeftColumn = 0
    iMinLeftColumn = 9999999999999999
    iMaxTokenColumn = 0
    iMinTokenColumn = 9999999999999999

    for iKey in list(dAnalysis.keys()):
        iMaxLeftColumn = max(iMaxLeftColumn, dAnalysis[iKey]['comma_column'])
        iMinLeftColumn = min(iMinLeftColumn, dAnalysis[iKey]['comma_column'])
        iMaxTokenColumn = max(iMaxTokenColumn, dAnalysis[iKey]['identifier_column'])
        iMinTokenColumn = min(iMinTokenColumn, dAnalysis[iKey]['identifier_column'])

    if compact_alignment:
        for iKey in list(dAnalysis.keys()):
            dAnalysis[iKey]['adjust'] = iMaxLeftColumn - dAnalysis[iKey]['identifier_column'] + 1
    else:
        for iKey in list(dAnalysis.keys()):
            dAnalysis[iKey]['adjust'] = iMaxTokenColumn - dAnalysis[iKey]['identifier_column'] + 1


def check_for_exclusions(bSkip, oToken, lUnless):
    for lTokenPairs in lUnless:
        if isinstance(oToken, lTokenPairs[0]):
            return True
        if isinstance(oToken, lTokenPairs[1]):
            return False
    return bSkip


def check_for_signal_declaration(bSignalFound, oToken):
    if isinstance(oToken, token.signal_declaration.signal_keyword):
        return True
    if isinstance(oToken, token.signal_declaration.semicolon):
        return False
    return bSignalFound
