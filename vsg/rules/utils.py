
from vsg import parser


def add_optional_item(lTokens, oViolation, oInsertToken):
    lTokens.append(parser.whitespace(' '))
    lTokens.append(oInsertToken)
    oViolation.set_tokens(lTokens)


def remove_optional_item(oViolation, oInsertToken):
    lTokens = oViolation.get_tokens()
    if isinstance(lTokens[0], parser.whitespace):
        oViolation.set_tokens([])
    else:
        oViolation.set_tokens([lTokens[0]])


def is_single_line(oToi):
    lTokens = oToi.get_tokens()
    for oToken in lTokens:
        if isinstance(oToken, parser.carriage_return):
            return False
    return True


def number_of_carriage_returns(lTokens):
    iReturn = 0
    for oToken in lTokens:
        if isinstance(oToken, parser.carriage_return):
            iReturn += 1
    return iReturn


def number_of_tokens_in_token_list(lTokens, lTokenList):
    iReturn = 0
    for oToken in lTokens:
        for oTokenItem in lTokenList:
            if oToken == type(oTokenItem):
                iReturn += 1
    return iReturn


def print_debug(lTokens):
    sPrint = ''
    for oToken in lTokens:
        sPrint += oToken.get_value()
    print(sPrint)


def does_line_start_with_comment(lTokens):
    if isinstance(lTokens[0], parser.comment):
        return True
    if isinstance(lTokens[0], parser.whitespace) and isinstance(lTokens[1], parser.comment):
        return True
    return False


def get_toi_parameters(oToi):
    return oToi.get_line_number(), oToi.get_tokens()


def insert_token(lTokens, index, oToken):
    try:
        oToken = update_code_tags(lTokens[index], oToken)
    except IndexError:
        oToken = update_code_tags(lTokens[0], oToken)

    lTokens.insert(index, oToken)


def append_token(lTokens, oToken):
    oToken = update_code_tags(lTokens[-1], oToken)
    lTokens.append(oToken)


def update_code_tags(oToken1, oToken2):
    oToken2.code_tags = oToken1.code_tags
    return oToken2


def insert_whitespace(lTokens, index, num=1):
    insert_token(lTokens, index, parser.whitespace(' '*num))


def insert_carriage_return(lTokens, index):
    insert_token(lTokens, index, parser.carriage_return())


def insert_blank_line(lTokens, index):
    insert_token(lTokens, index, parser.blank_line())


def append_whitespace(lTokens, num=1):
    append_token(lTokens, parser.whitespace(' '*num))


def append_carriage_return(lTokens):
    append_token(lTokens, parser.carriage_return())


def append_blank_line(lTokens):
    append_token(lTokens, parser.blank_line())


def get_index_of_token_in_list(oToken, lTokens):
    for iToken, token in enumerate(lTokens):
        if isinstance(token, oToken):
            return iToken
    return None


def get_number_of_carriage_returns_before_token(oStopToken, lTokens):
    iReturn = 0
    for oToken in lTokens:
        if isinstance(oToken, parser.carriage_return):
            iReturn += 1
        if isinstance(oToken, oStopToken):
            break
    return iReturn


def get_indent_of_line(lTokens):
    if isinstance(lTokens[0], parser.whitespace):
        return lTokens[1].get_indent()
    else:
        return lTokens[0].get_indent()


def whitespace_before_token_index(lTokens, iIndex):
    if isinstance(lTokens[iIndex - 1], parser.whitespace):
        return True
    return False


def remove_token_sequence_from_token_list(lRemoveTokens, lTokens):
    lRemoveIndexes = find_indexes_of_token_sequence(lRemoveTokens, lTokens)
    return remove_slices_from_list_at_indexes(lTokens, lRemoveIndexes, len(lRemoveTokens))


def find_indexes_of_token_sequence(lRemoveTokens, lTokens):
    iTokenListLength = len(lTokens)
    iLength = len(lRemoveTokens)
    lReturn = []
    for iIndex in range(0, iTokenListLength - 1 - iLength):
        for iToken in range(0, iLength):
            if not isinstance(lTokens[iIndex + iToken], lRemoveTokens[iToken]):
                break
        else:
            lReturn.append(iIndex)
    return lReturn


def remove_slices_from_list_at_indexes(lReturn, lRemoveIndexes, iLength):
    if len(lRemoveIndexes) > 0:
        lRemoveIndexes.reverse()
        for iIndex in lRemoveIndexes:
            iEnd = iIndex + iLength
            lReturn = lReturn[0:iIndex] + lReturn[iEnd::]
    return lReturn
