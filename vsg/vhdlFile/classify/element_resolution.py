
from vsg.vhdlFile import utils


def classify_until(lUntils, iToken, lObjects):

    iCurrent = iToken
    iLast = 0
    while iLast != iCurrent:
        iLast = iCurrent
        if lObjects[utils.find_next_token(iCurrent, lObjects)].get_value().lower() in lUntils:
            return iCurrent
        iCurrent = utils.assign_next_token(parser.todo, iCurrent, lObjects)
