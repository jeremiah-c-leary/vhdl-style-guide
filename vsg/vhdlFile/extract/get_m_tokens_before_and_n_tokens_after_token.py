
from vsg import parser

from vsg.vhdlFile.extract import tokens
from vsg.vhdlFile.extract import utils


def get_m_tokens_before_and_n_tokens_after_token(iM, iN, lTokens, lAllTokens, oTokenMap):
    lReturn = []

    lIndexes = utils.get_indexes_of_token_list(lTokens, oTokenMap)

    for iIndex in lIndexes:
        iLine = oTokenMap.get_line_number_of_index(iIndex)
        iStart = iIndex - iM
        iEnd = iIndex + iN
        if start_index_exceeds_beginning_of_file(iStart):
            lMyTokens = []
            lMyTokens.append(parser.beginning_of_file())
            lMyTokens.extend(lAllTokens[0:iEnd + 1])
            oTokens = tokens.New(0, iLine, lMyTokens)
            lReturn.append(oTokens)
        else:
            lReturn.append(tokens.New(iStart, iLine, lAllTokens[iStart:iEnd + 1]))

    return lReturn


def start_index_exceeds_beginning_of_file(iStart):
    if iStart < 0:
        return True
    return False
