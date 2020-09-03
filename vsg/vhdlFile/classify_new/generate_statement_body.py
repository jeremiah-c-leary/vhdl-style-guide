
from vsg import parser
from vsg.token import generate_statement_body as token

from vsg.vhdlFile.classify_new import block_declarative_part
from vsg.vhdlFile.classify_new import concurrent_statement

from vsg.vhdlFile import utils


def classify(iObject, lObjects):
    '''
    generate_statement_body ::=
            [ block_declarative_part
        begin ]
            { concurrent_statement }
        [ end [ alternative_label ] ; ]
    '''
    bBlockDeclarativePartFound = False
    iToken = utils.find_next_token(iObject, lObjects)
    iPrevious = iToken
    iToken = utils.detect_submodule(iObject, lObjects, block_declarative_part)

    if iToken != iPrevious:
        bBlockDeclarativePartFound = True
        iToken = utils.classify_begin_keyword(iToken, token.begin_keyword, lObjects)

    iLast = 0
    while iToken != iLast:
        iToken = utils.find_next_token(iToken, lObjects)
        iLast = iToken
        if utils.object_value_is(lObjects, iToken,  'elsif'):
            return iToken
        if utils.object_value_is(lObjects, iToken,  'else'):
            return iToken
        if utils.object_value_is(lObjects, iToken,  'when'):
            return iToken
        iToken = concurrent_statement.detect(iToken, lObjects)

    if bBlockDeclarativePartFound:
        iStart, iEnd = utils.get_range(lObjects, iToken, ';')
        for iToken in range(iStart, iEnd + 1):
            if not utils.is_item(lObjects, iToken):
                continue
            if utils.classify_token('end', token.end_keyword, iToken, lObjects):
                continue
            if utils.classify_token(';', token.semicolon, iToken, lObjects):
                continue
            utils.assign_token(lObjects, iToken, token.alternative_label)

    return iToken
