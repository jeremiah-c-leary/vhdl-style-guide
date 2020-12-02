
from vsg import parser

from vsg.vhdlFile.extract import tokens


def get_tokens_matching_in_range_bounded_by_tokens(lTokens, oStart, oEnd, lAllTokens, oTokenMap):
        iLine = 1
        lReturn = []
        bSearch = False
        for iIndex in range(0, len(lAllTokens)):
            if isinstance(lAllTokens[iIndex], oStart):
                bSearch = True
            if isinstance(lAllTokens[iIndex], oEnd):
                bSearch = False
            if bSearch:
                for oToken in lTokens:
                    if isinstance(lAllTokens[iIndex], oToken):
                        lReturn.append(tokens.New(iIndex, iLine, [lAllTokens[iIndex]]))

            if isinstance(lAllTokens[iIndex], parser.carriage_return):
                iLine +=1

        return lReturn
