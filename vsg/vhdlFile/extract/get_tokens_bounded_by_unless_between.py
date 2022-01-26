
from vsg.vhdlFile.extract import tokens


def get_tokens_bounded_by_unless_between(oStart, oEnd, lUnless, lAllObjects, oTokenMap):

    lReturn = []

    lStart, lEnd = oTokenMap.get_token_pair_indexes(oStart, oEnd)

    lUnlessStart, lUnlessEnd = get_unless_token_indexes(lUnless, oTokenMap)

    lNewStart, lNewEnd = filter_token_pairs(lStart, lEnd, lUnlessStart, lUnlessEnd)

    for iStart, iEnd, iIndex in zip(lNewStart, lNewEnd, lEnd):
        lTemp = lAllObjects[iStart: iEnd + 1]
        iStartLine = oTokenMap.get_line_number_of_index(iStart)
        oToi = tokens.New(iStart, iStartLine, lTemp)
        oToi.set_token_value(iIndex - iStart)
        lReturn.append(oToi)

    return lReturn


def get_unless_token_indexes(lUnless, oTokenMap):
    lReturnStart = []
    lReturnEnd = []
    for unless in lUnless:
        lStart, lEnd = oTokenMap.get_token_pair_indexes(unless[0], unless[1])
        lReturnStart.extend(lStart)
        lReturnEnd.extend(lEnd)
    return lReturnStart, lReturnEnd


def filter_token_pairs(lStart, lEnd, lUnlessStart, lUnlessEnd):
    lReturnStart = []
    lReturnEnd = []
    for iStart, iEnd in zip(lStart, lEnd):
        if not indexes_between_indexes(iStart, iEnd, lUnlessStart, lUnlessEnd):
            lReturnStart.append(iStart)
            lReturnEnd.append(iEnd)
    return lReturnStart, lReturnEnd


def indexes_between_indexes(iStart, iEnd, lUnlessStart, lUnlessEnd):
    for iUnlessStart, iUnlessEnd in zip(lUnlessStart, lUnlessEnd):
        if iUnlessStart < iStart < iUnlessEnd and \
           iUnlessStart < iEnd < iUnlessEnd:
            return True
    return False
