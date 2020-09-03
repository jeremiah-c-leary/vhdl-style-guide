
from vsg import parser
from vsg.vhdlFile import utils

from vsg.token import if_generate_statement as token

from vsg.vhdlFile.classify_new import condition 
from vsg.vhdlFile.classify_new import generate_statement_body

'''
    if_generate_statement ::=
        *generate*_label :
            if [ *alternative*_label : ] condition generate
                generate_statement_body
            { elsif [ *alternative_label* : ] condition generate
                generate_statement_body }
            [ else [ *alternative_label* : ] generate
                generate_statement_body ]
            end generate [ *generate*_label ] ;
'''


def detect(iObject, lObjects):
    iItemCount = 0
    iIndex = iObject
    try:
        while iItemCount < 3:
            if type(lObjects[iIndex]) == parser.item:
                iItemCount += 1
            iIndex += 1
        else:
            if lObjects[iIndex-1].get_value().lower() == 'if':
                return classify(iObject, lObjects)
    except IndexError:
        return iObject
    return iObject


def classify(iObject, lObjects):
    iToken = utils.tokenize_label(iObject, lObjects, token.generate_label, token.label_colon)

    iToken = utils.find_next_token(iToken, lObjects)
    utils.classify_token('if', token.if_keyword, iToken, lObjects)
    iToken += 1

    iStart, iEnd = utils.get_range(lObjects, iToken, 'generate')
    iToken = condition.classify(iStart, iEnd, lObjects)

    utils.classify_token('generate', token.generate_keyword, iToken, lObjects)
    iToken = utils.find_next_token(iToken, lObjects)
    iToken = generate_statement_body.classify(iToken, lObjects)

    iLast = 0
    while iToken != iLast:
        iToken = utils.find_next_token(iToken, lObjects)
        iLast = iToken
        if utils.classify_token('elsif', token.elsif_keyword, iToken, lObjects):
            iStart, iEnd = utils.get_range(lObjects, iToken, 'generate')
            iToken = condition.classify(iStart, iEnd, lObjects)

            utils.classify_token('generate', token.generate_keyword, iToken, lObjects)

            iToken = generate_statement_body.classify(iToken, lObjects)
            

    iLast = 0
    while iToken != iLast:
        iToken = utils.find_next_token(iToken, lObjects)
        iLast = iToken
        if utils.classify_token('else', token.else_keyword, iToken, lObjects):
            iStart, iEnd = utils.get_range(lObjects, iToken, 'generate')
            iToken = iEnd 
            utils.classify_token('generate', token.generate_keyword, iToken, lObjects)

            iToken = utils.find_next_token(iToken, lObjects)
            iToken = generate_statement_body.classify(iToken, lObjects)

    ### Classify the closing keywords
    iStart, iEnd = utils.get_range(lObjects, iToken, ';')
    for iToken in range(iStart, iEnd + 1):
        if not utils.is_item(lObjects, iToken):
            continue
        if utils.classify_token('generate', token.end_generate_keyword, iToken, lObjects):
            continue
        if utils.classify_token('end', token.end_keyword, iToken, lObjects):
            continue
        if utils.classify_token(';', token.semicolon, iToken, lObjects):
            continue
        utils.assign_token(lObjects, iToken, token.end_generate_label)

    return iToken
