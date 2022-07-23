
from vsg import parser


def classify(lObjects, oOptions):

    if len(lObjects) == 0 and not oOptions.inside_delimited_comment():
        lObjects.append(parser.blank_line())
