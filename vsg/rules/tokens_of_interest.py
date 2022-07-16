
from vsg.vhdlFile import utils


def get_tokens_bounded_by(lTokenPairs, oFile):
    lToi = []
    for lTokenPair in lTokenPairs:
        aToi = oFile.get_tokens_bounded_by(lTokenPair[0], lTokenPair[1])
        lToi = utils.combine_two_token_class_lists(lToi, aToi)
    return lToi
