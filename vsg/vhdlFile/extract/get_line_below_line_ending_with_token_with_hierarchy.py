
from vsg import parser

from vsg.vhdlFile import utils
from vsg.vhdlFile import vhdlFile


def get_line_below_line_ending_with_token_with_hierarchy(lTokens, lAllTokens, lHierarchy):
    lReturn = []
    iLine = 1
    lCurrentLine = []
    lTemp = []
    bTokenFound = False
    bCrFound = False
    for iIndex in range(0, len(lAllTokens)):

        if not bTokenFound:
            for oToken in lTokens:
                if isinstance(lAllTokens[iIndex], oToken):
                    if lAllTokens[iIndex].get_hierarchy() in lHierarchy:
                        if utils.are_next_consecutive_token_types([parser.carriage_return], iIndex + 1, lAllTokens):
                            bTokenFound = True
                            break
                        if utils.are_next_consecutive_token_types([parser.whitespace, parser.carriage_return], iIndex + 1, lAllTokens):
                            bTokenFound = True
                            break
                        if utils.are_next_consecutive_token_types([parser.whitespace, parser.comment, parser.carriage_return], iIndex + 1, lAllTokens):
                            bTokenFound = True
                            break
                        if utils.are_next_consecutive_token_types([parser.comment, parser.carriage_return], iIndex + 1, lAllTokens):
                            bTokenFound = True
                            break


        if bCrFound:
            lTemp.append(lAllTokens[iIndex])

        if isinstance(lAllTokens[iIndex], parser.carriage_return):
            if bCrFound:
                lTemp.pop()
                lReturn.append(vhdlFile.Tokens(iStart, iLine, lTemp))
                lTemp = []
                bCrFound = False
                bTokenFound = False
            elif bTokenFound:
                bCrFound = True
                iStart = iIndex + 1

            iLine +=1

    return lReturn
