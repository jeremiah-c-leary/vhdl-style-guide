
from vsg import parser
from vsg.vhdlFile import utils

from vsg.token import block_header as token

#from vsg.vhdlFile.classify_new import generic_clause 
#from vsg.vhdlFile.classify_new import generic_map_aspect
#from vsg.vhdlFile.classify_new import port_clause 
#from vsg.vhdlFile.classify_new import port_map_aspect

'''
    block_header ::=
        [ generic_clause
        [ generic_map_aspect ; ] ]
        [ port_clause
        [ port_map_aspect ; ] ]
'''


def detect(iCurrent, lObjects):
    return iCurrent
