
from vsg import parser
from vsg.token import architecture_body
from vsg.vhdlFile.classify import architecture_declarative_part
from vsg.vhdlFile.classify import architecture_statement_part


'''
architecture identifier of entity_name is

    architecture_declarative_part

begin

    architecture_statement_part

end [ architecture ] [ architecture_simple_name ] 
'''

def tokenize(oObject, iObject, lObjects, dVars):
    if not dVars['bArchitectureKeywordFound']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True

    else:
        if not dVars['bArchitectureIdentifierFound']:

            if classify_identifier(oObject, iObject, lObjects, dVars):
                return True

        else:
            if not dVars['bArchitectureEntityNameFound']:

                if classify_of_keyword(oObject, iObject, lObjects, dVars):
                    return True

                if classify_entity_name(oObject, iObject, lObjects, dVars):
                    return True

            else:
                if not dVars['bArchitectureIsKeywordFound']:

                    if classify_is_keyword(oObject, iObject, lObjects, dVars):
                        return True
                else:
                    if not dVars['bArchitectureBeginKeywordFound']:

                        if classify_begin_keyword(oObject, iObject, lObjects, dVars):
                            return True

                        if architecture_declarative_part.tokenize(oObject, iObject, lObjects, dVars):
                            return True
                    else:
                        if not dVars['bArchitectureEndKeywordFound']:

                            if architecture_statement_part.tokenize(oObject, iObject, lObjects, dVars):
                                return True

                            if classify_end(oObject, iObject, lObjects, dVars):
                                return True

                        else:

                            if classify_end_architecture_keyword(oObject, iObject, lObjects, dVars):
                                return True

                            if classify_semicolon(oObject, iObject, lObjects, dVars):
                                return True

                            if classify_simple_name(oObject, iObject, lObjects, dVars):
                                return True

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'architecture':
        lObjects[iObject] = architecture_body.keyword(sValue)
        dVars['bArchitectureKeywordFound'] = True 
        return True
    return False


def classify_identifier(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = architecture_body.identifier(oObject.get_value())
        dVars['bArchitectureIdentifierFound'] = True
        return True
    return False


def classify_of_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'of':
        lObjects[iObject] = architecture_body.of_keyword(sValue)
        return True
    return False


def classify_entity_name(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = architecture_body.entity_name(oObject.get_value())
        dVars['bArchitectureEntityNameFound'] = True
        return True
    return False


def classify_is_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'is':
        lObjects[iObject] = architecture_body.is_keyword(sValue)
        dVars['bArchitectureIsKeywordFound'] = True
        return True
    return False


def classify_begin_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'begin':
        lObjects[iObject] = architecture_body.begin_keyword(sValue)
        dVars['bArchitectureBeginKeywordFound'] = True
        return True
    return False


def classify_end(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'end':
        lObjects[iObject] = architecture_body.end_keyword(sValue)
        dVars['bArchitectureEndKeywordFound'] = True 
        return True
    return False


def classify_end_architecture_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'architecture':
        lObjects[iObject] = architecture_body.end_architecture_keyword(oObject)
        return True
    return False


def classify_simple_name(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = architecture_body.simple_name(oObject.get_value())
        return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = architecture_body.semicolon()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
        dVars['bArchitectureKeywordFound'] = False
        dVars['bArchitectureIdentifierFound'] = False
        dVars['bArchitectureEntityNameFound'] = False
        dVars['bArchitectureIsKeywordFound'] = False
        dVars['bArchitectureBeginKeywordFound'] = False
        dVars['bArchitectureEndKeywordFound'] = False

