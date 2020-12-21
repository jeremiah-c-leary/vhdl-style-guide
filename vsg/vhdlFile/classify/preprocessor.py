

from vsg import parser


def classify(lTokens, lObjects):
    '''
    Classifies preprocessor commands

    '''
    # Check for entity
    try:
        if lTokens[0].startswith('#') or (lTokens[0].startswith(' ') and lTokens[1].startswith('#')):
            lObjects.clear()
            lObjects.append(parser.preprocessor(''.join(lTokens)))
    except IndexError:
        return
