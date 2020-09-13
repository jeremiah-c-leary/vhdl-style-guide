
from vsg.vhdlFile.classify_new import architecture_body
from vsg.vhdlFile.classify_new import package_body


def detect(iToken, lObjects):
    '''
    secondary_unit ::=
        architecture_body
      | package_body
    '''
    iReturned = architecture_body.detect(iToken, lObjects)
    if iReturned != iToken:
        return iReturned

    iReturned = package_body.detect(iToken, lObjects)
    if iReturned != iToken:
        return iReturned

    return iToken
