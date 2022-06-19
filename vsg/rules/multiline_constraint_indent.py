
from vsg import parser
from vsg import violation

from vsg import token

from vsg.rules import utils as rules_utils
from vsg.rule_group import alignment
from vsg.vhdlFile import utils


class multiline_constraint_indent(alignment.Rule):
    '''
    '''

    def __init__(self, name, identifier):
        alignment.Rule.__init__(self, name=name, identifier=identifier)
        self.oStartToken = None
        self.oEndToken = None

    def _get_tokens_of_interest(self, oFile):
        lReturn = []
        lToi = oFile.get_tokens_bounded_by(self.oStartToken, self.oEndToken)
        for oToi in lToi:
            if not oToi.token_type_exists(parser.carriage_return):
                continue
            lTokens = oToi.get_tokens()
            iEndToken = 0
            for iToken, oToken in enumerate(lTokens):
                if isinstance(oToken, token.index_constraint.close_parenthesis) or isinstance(oToken, token.record_constraint.close_parenthesis):
                    iEndToken = iToken
            if iEndToken > 0:
                lReturn.append(oToi.extract_tokens(0, iEndToken))
                lReturn[-1].iFirstLine, lReturn[-1].iFirstLineIndent = _get_first_line_info(oToi.get_line_number(), oFile)
                lReturn[-1].iAssignColumn = oFile.get_column_of_token_index(oToi.get_start_index())

        return lReturn


    def _analyze(self, lToi):
#        lToi = self._get_tokens_of_interest(oFile)
        print('Got here')
     
        for oToi in lToi:
            iLine, lTokens = utils.get_toi_parameters(oToi)
#            print('='*5 + str(iLine) + '='*70)

#            iFirstLine, iFirstLineIndent = _get_first_line_info(iLine, oFile)
            iFirstLine = oToi.iFirstLine
#            iFirstLineIndent = oToi.iFirstLineIndent

#            iAssignColumn = oFile.get_column_of_token_index(oToi.get_start_index())
            iAssignColumn = oToi.iAssignColumn
            iColumn = iAssignColumn

            dActualIndent = {}

            dActualIndent[iLine] = oToi.iFirstLineIndent
            lParens = []
            dIndex = {}

            bStartsWithParen = _starts_with_paren(lTokens)

            for iToken, oToken in enumerate(lTokens):

                iLine = utils.increment_line_number(iLine, oToken)

                if isinstance(oToken, parser.blank_line):
                    continue

                if isinstance(oToken, parser.carriage_return):
                    iColumn = 0
                    dActualIndent[iLine] = _set_indent(iToken, lTokens)
                    dIndex[iLine] = iToken + 1
                    continue

                iColumn += len(oToken.get_value())

                if isinstance(oToken, parser.close_parenthesis):
                    dParen = {}
                    dParen['type'] = 'close'
                    dParen['line'] = iLine
                    dParen['column'] = iColumn
                    dParen['begin_line'] = utils.does_token_start_line(iToken, lTokens)
                    lParens.append(dParen)

                if isinstance(oToken, parser.open_parenthesis):
                    dParen = {}
                    dParen['type'] = 'open'
                    dParen['line'] = iLine
                    dParen['column'] = iColumn
                    dParen['begin_line'] = utils.does_token_start_line(iToken, lTokens)
                    lParens.append(dParen)

            iLastLine = iLine

            dExpectedIndent = _analyze_align_paren_no(iFirstLine, iLastLine, lParens, self.indentSize, dActualIndent, bStartsWithParen)
            print(dExpectedIndent)

            for iLine in range(iFirstLine, iLastLine + 1):
                if dActualIndent[iLine] is None:
                    continue
                if indents_match(dActualIndent[iLine], dExpectedIndent[iLine]):
                    continue

                oViolation = build_violation(iLine, oToi, iToken, dExpectedIndent, dIndex, dActualIndent)
                self.add_violation(oViolation)


    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
#        print(dAction)
        if dAction['action'] == 'adjust':
            lTokens[0].set_value(' '*dAction['column'])
        else:
            rules_utils.insert_whitespace(lTokens, 0, dAction['column'])

        oViolation.set_tokens(lTokens)


def build_violation(iLine, oToi, iToken, dExpectedIndent, dIndex, dActualIndent):
    sSolution = 'Adjust indent to column ' + str(dExpectedIndent[iLine])
    dAction = build_action_dictionary(iLine, dActualIndent, dExpectedIndent)
    iToken = dIndex[iLine]
    oViolation = violation.New(iLine, oToi.extract_tokens(iToken, iToken), sSolution)
    oViolation.set_action(dAction)
    return oViolation


def build_action_dictionary(iLine, dActualIndent, dExpectedIndent):
    dAction = {}
    dAction['line'] = iLine
    dAction['column'] = dExpectedIndent[iLine]

    if dActualIndent[iLine] > 0:
        dAction['action'] = 'adjust'
    else:
        dAction['action'] = 'insert'
    return dAction


def line_starts_with_comment(iActual):
    if iActual is None:
        return True
    return False


def indents_match(iActual, iExpected):
    if iActual == iExpected:
        return True
    return False


def calculate_start_column(oFile, oToi):
    iReturn = oFile.get_column_of_token_index(oToi.get_start_index())
    iReturn += len(oToi.get_tokens()[0].get_value())
    iReturn += 1
#    print(f'Start Column = {iReturn}')
    return iReturn


def is_token_before_carriage_return(tToken, lTokens):
    for oToken in lTokens:
        if isinstance(oToken, tToken):
            return True
        if isinstance(oToken, parser.carriage_return):
            return False
    return False


def _set_column_adjustment(iToken, lTokens):
    iReturn = 0
    if isinstance(lTokens[iToken + 1], parser.whitespace):
        if isinstance(lTokens[iToken + 2], parser.close_parenthesis):
            iReturn = -1
    else:
        if isinstance(lTokens[iToken + 1], parser.close_parenthesis):
            iReturn = -1
    return iReturn


def _set_indent(iToken, lTokens):
    iReturn = 0
    if isinstance(lTokens[iToken + 1], parser.whitespace):
        iReturn = len(lTokens[iToken + 1].get_value())
    else:
        iReturn = 0
    return iReturn


def _analyze_align_paren_no(iFirstLine, iLastLine, lParens, iIndentStep, dActualIndent, bStartsWithParen):
    print('--> _analyze_align_paren_no <-' + '-'*70)
    dExpectedIndent = {}
    dExpectedIndent[iFirstLine] = dActualIndent[iFirstLine]
    print(bStartsWithParen)
    if bStartsWithParen:
        iFirstIndent = dActualIndent[iFirstLine]
    else:
        iFirstIndent = dActualIndent[iFirstLine] + iIndentStep

    iIndent = iFirstIndent

#    print(iIndent)
    iParens = 0

    for iLine in range(iFirstLine, iLastLine + 1):
#        print('-->  ' + str(iLine) + '  <--------------------------')

        lTemp = []
        for dParen in lParens:
            if dParen['line'] == iLine:
                lTemp.append(dParen)

        if len(lTemp) == 0:
            dExpectedIndent[iLine + 1] = iIndent
            continue

        for dTemp in lTemp:
            if dTemp['type'] == 'open':
                iParens += 1
            else:
                iParens -= 1
                if dTemp['begin_line']:
                    dExpectedIndent[iLine] -= iIndentStep

        iIndent = iFirstIndent + iParens * iIndentStep

#        print(f'indent = {iIndent} | iPerens = {iParens}')
        dExpectedIndent[iLine + 1] = iIndent
#        print(dExpectedIndent)

    return dExpectedIndent


def _starts_with_paren(lTokens):
    iToken = utils.find_next_non_whitespace_token(1, lTokens)
    try:
        if isinstance(lTokens[iToken], parser.open_parenthesis):
            return True
    except IndexError:
        if isinstance(lTokens[0], parser.open_parenthesis):
            return True
    return False


def _get_first_line_info(iLine, oFile):
    lTemp = oFile.get_tokens_from_line(iLine)
    iIndent = len(lTemp.get_tokens()[0].get_value())
    return iLine, iIndent

