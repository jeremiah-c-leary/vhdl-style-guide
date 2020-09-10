

from vsg.token import block_header as token

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify_new import generic_clause 
from vsg.vhdlFile.classify_new import generic_map_aspect
from vsg.vhdlFile.classify_new import port_clause 
from vsg.vhdlFile.classify_new import port_map_aspect

'''
    block_header ::=
        [ generic_clause
        [ generic_map_aspect ; ] ]
        [ port_clause
        [ port_map_aspect ; ] ]
'''


def detect(iToken, lObjects):
    iReturn = iToken
    iReturn = generic_clause.detect(iReturn, lObjects)
    iLast = iReturn
    iReturn = generic_map_aspect.detect(iReturn, lObjects)
    if iLast != iReturn:
        iReturn = utils.assign_next_token_required(';', token.semicolon, iReturn, lObjects)
    iReturn = port_clause.detect(iReturn, lObjects)
    iLast = iReturn
    iReturn = port_map_aspect.detect(iReturn, lObjects)
    if iLast != iReturn:
        iReturn = utils.assign_next_token_required(';', token.semicolon, iReturn, lObjects)
    
    return iReturn
