
from vsg import parser


def classify(lObjects, oOptions):

    if is_blank_line(lObjects, oOptions):
        lObjects.append(parser.blank_line())


def is_blank_line(lObjects, oOptions):
    if len(lObjects) == 0 and not oOptions.inside_delimited_comment():
        return True
    return False
