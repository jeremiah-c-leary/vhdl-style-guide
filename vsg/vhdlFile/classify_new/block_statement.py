
from vsg import parser
from vsg.vhdlFile import utils

from vsg.token import block_statement as token

from vsg.vhdlFile.classify_new import block_header
from vsg.vhdlFile.classify_new import block_declarative_part
from vsg.vhdlFile.classify_new import block_statement_part

'''
    block_statement ::=
    block_label :
        block [ ( guard_condition ) ] [ is ]
            block_header
            block_declarative_part
        begin
            block_statement_part
        end block [ block_label ] ;
'''


def detect(iCurrent, lObjects):
#    print('---> detecting block_statement')
    iItemCount = 0
    iIndex = iCurrent
    try:
        while iItemCount < 3:
#            print(lObjects[iIndex].get_value())
            if utils.is_item(lObjects, iIndex):
                iItemCount += 1
            iIndex += 1
        else:
            if utils.object_value_is(lObjects, iIndex-1, 'block'):  # jcl - why is this iIndex - 1?
                return classify(iCurrent, lObjects)
    except IndexError:
        return iCurrent
    return iCurrent


def classify(iCurrent, lObjects):
#    print('---> Classifying opening block_statement')

    ### Classify opening keywords
    iStart, iEnd = utils.get_range(lObjects, iCurrent, 'block')
    for iToken in range(iStart, iEnd + 1):
#        print(lObjects[iToken].get_value())
        if not utils.is_item(lObjects, iToken):
            continue
        if utils.classify_token('block', token.keyword, iToken, lObjects):
            continue
        if utils.classify_token(':', token.label_colon, iToken, lObjects):
            continue
        utils.assign_token(lObjects, iToken, token.block_label)

    ### Check for guard condition
    if utils.have_guard_condition(iToken, lObjects):
        iStart, iEnd = utils.get_range(lObjects, iToken, ')')
        for iToken in range(iStart, iEnd + 1):
#            print(lObjects[iToken].get_value())
            if not utils.is_item(lObjects, iToken):
                continue
            utils.assign_token(lObjects, iToken, token.guard_condition)

    ### Find next item
    while not utils.is_item(lObjects, iToken):
#        print(lObjects[iToken].get_value())
        iToken += 1

    ### Classify the is keyword if it exists
    if utils.classify_token('is', token.is_keyword, iToken, lObjects):
#        print(lObjects[iToken].get_value())
        iToken += 1

    ### Check for block_header
    iLast = 0           
    while iLast != iToken:
        while not utils.is_item(lObjects, iToken):
#            print(lObjects[iToken].get_value())
            iToken += 1
        iLast = iToken
        iToken = block_header.detect(iToken, lObjects)
        
    ### Check for block_declarative_part
    iLast = 0           
    while iLast != iToken:
        while not utils.is_item(lObjects, iToken):
#            print(lObjects[iToken].get_value())
            iToken += 1
        iLast = iToken
        iToken = block_declarative_part.detect(iToken, lObjects)

    ### Classify Begin keyword        
    utils.classify_token('begin', token.begin_keyword, iToken, lObjects)
#    print(lObjects[iToken].get_value())
    iToken += 1

    ### Check for block_statement_part
    iLast = 0           
    while iLast != iToken:
        while not utils.is_item(lObjects, iToken):
            iToken += 1
        iLast = iToken
        iToken = block_statement_part.detect(iToken, lObjects)

#    print('---> Classifying closing block_statement')
    ### Classify the closing keywords
    iStart, iEnd = utils.get_range(lObjects, iToken, ';')
    for iToken in range(iStart, iEnd + 1):
#        print(lObjects[iToken].get_value())
        if not utils.is_item(lObjects, iToken):
            continue
        if utils.classify_token('block', token.end_block_keyword, iToken, lObjects):
            continue
        if utils.classify_token('end', token.end_keyword, iToken, lObjects):
            continue
        if utils.classify_token(';', token.semicolon, iToken, lObjects):
            continue
        utils.assign_token(lObjects, iToken, token.end_block_label)

    return iToken


#*******************************************************************************
#*******************************************************************************
#*******************************************************************************


#def tokenize(iObject, oObject, lAllObjects, lNewObjects, dVars):
#
#    iToken = iObject
#
#    while not utils.object_value_is(lAllObjects iToken, 'block'):
#        if utils.is_item(lAllObjects, iToken):
#            if utils.object_value_is(lAllObjects, iToken, ':'):
#                utils.assign_token(lAllObjects, iToken, token.label_colon)
#            else:
#                utils.assign_token(lAllObjects, iToken, token.label_name)
#        iToken += 1
#    else:
#        utils.assign_token(lAllObjects, iToken, token.keyword)
#        iToken += 1
#
#    while not 
#
#    for iToken in range(iObject, len(lAllObjects):
#        kk
#        if utils.is_item(lAllObjects, iToken):
#            if utils.object_value_is(lAllObjects, iToken, ':'):
#                utils.assign_token(lAllObjects, iToken, token.label_colon)
#            elif utils.object_value_is(lAllObjects, iToken, 'block'):
#                utils.assign_token(lAllObjects, iToken, token.label_colon)
#
#def tokenize_begin_declaration(iObject, oObject, lAllObjects, lNewObjects, dVars):
#
#    if oObject.get_value().lower() == ':':
#        lNewObjects.append(token.label_colon())
#        return True
#    elif oObject.get_value().lower() == 'block':
#       lNewObjects.append(token.keyword(oObject.get_value()))
#       return True
#    elif utils.have_guard_condition(iObject, lAllObjects):
#       print("need to process guard condition first")
#       return True
#    elif utils.have_is_keyword(iObject, lAllObjects):
#       lNewObjects.append(token.is_keyword(oObject.get_value()))
#       return True
#    elif oObject.get_value().lower() == 'begin':
#       lNewObjects.append(token.begin_keyword(oObject.get_value()))
#       utils.pop_level(dVars)
#       utils.push_level(dVars, 'block_statement_part')
#       return True
#
#    return False
#
#def tokenize_end_declaration(iObject, oObject, lAllObjects, lNewObjects, dVars):
#    if oObject.get_value().lower() == 'block':
#        lNewObjects.append(token.end_block_keyword(oObject.get_value()))
#        return True
#    elif oObject.get_value().lower() == ';':
#        lNewObjects.append(token.semicolon())
#        utils.pop_level(dVars)
#        return True
#    else:
#        lNewObjects.append(token.end_block_label(oObject.get_value()))
#        return True
#
#    return False
#
