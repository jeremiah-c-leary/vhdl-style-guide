
from vsg import parser


def classify(lObjects, oLine):

    if len(lObjects) == 0:
        lObjects.append(parser.blank_line())
        oLine.isBlank = True
