
from vsg import parser

from vsg.vhdlFile import utils


def get_tokens_bounded_by(lTokenPairs, oFile):
    lToi = []
    for lTokenPair in lTokenPairs:
        aToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1])
        lToi = utils.combine_two_token_class_lists(lToi, aToi)
    return lToi


def adjust_start_index_based_on_whitespace(oToi, iAdjustment):
    iStart = oToi.get_meta_data('iStart')
    lTokens = oToi.get_tokens()
    if isinstance(lTokens[iStart - 1], parser.whitespace):
        oToi.set_meta_data('iStart', iStart + iAdjustment)
