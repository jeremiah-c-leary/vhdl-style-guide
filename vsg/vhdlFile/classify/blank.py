
from vsg import parser


def classify(lObjects):

    if len(lObjects) == 0:
        lObjects.append(parser.blank_line())
