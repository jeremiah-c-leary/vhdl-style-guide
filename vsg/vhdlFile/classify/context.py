
from vsg import parser


def context(self, dVars, lTokens, lObjects, oLine):
    '''
    Classifies context declarations:

        context identifier is
            [ library ;]
        end [context] [identifier] ;

    and context references:

        context selected_name { , selected_name } ;

    Sets the following line attributes:

      * insideContext

    Modifies the following variables:

      * bInsideContext
      * bContextEndFound
      * bContextIsFound
      * iCurrentIndentLevel
    '''
    bContextDeclarationFound = False
#    print(oLine.line)
    for iToken, sToken in enumerate(lTokens):
        if dVars['bInsideContext']:

            classify_context_identifier(sToken, iToken, lObjects, dVars)

            if classify_context_is_keyword(sToken, iToken, lObjects, dVars):

                reclassify_context_keyword_and_identifier(self, lObjects)
           
            classify_context_reference_comma(sToken, iToken, lObjects, dVars)

            if classify_context_reference_semicolon(sToken, iToken, lObjects, dVars):

                if not dVars['bContextIsFound']:
                    reclassify_context_reference_keyword_and_identifier_outside_of_context_declaration(self, lObjects, dVars)

            if dVars['bContextEndFound']:

               classify_context_end_context_keyword(sToken, iToken, lObjects)

               classify_context_end_identifier(sToken, iToken, lObjects)

               if classify_semicolon(sToken, iToken, lObjects, dVars):

                   reclassify_context_reference_keyword_and_identifier(self, lObjects)

            classify_context_end_keyword(sToken, iToken, lObjects, dVars, oLine)

            classify_unknown_item(sToken, iToken, lObjects)
 
        else:
            classify_context_keyword(sToken, iToken, lObjects, dVars, oLine)


def classify_unknown_item(sToken, iToken, lObjects):
    if type(lObjects[iToken]) == parser.item:
        lObjects[iToken] = parser.item(sToken)


def classify_semicolon(sToken, iToken, lObjects, dVars):
    if sToken == ';':
        lObjects[iToken] = parser.context_semicolon()
        dVars['bInsideContext'] = False
        dVars['bContextIsFound'] = False
        dVars['bContextEndFound'] = False
        return True
    return False


def classify_context_end_identifier(sToken, iToken, lObjects):
    if sToken.lower() != 'context' and sToken != ';' and not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment):
        lObjects[iToken] = parser.context_end_identifier(sToken)


def classify_context_end_context_keyword(sToken, iToken, lObjects):
    if sToken.lower() == 'context':  
        lObjects[iToken] = parser.context_end_context_keyword(sToken)


def classify_context_end_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'end':
        lObjects[iToken] = parser.context_end_keyword(sToken)
        dVars['bContextEndFound'] = True
        if iToken < 2:
            oLine.indentLevel = 0
            dVars['iCurrentIndentLevel'] = 0


def classify_context_is_keyword(sToken, iToken, lObjects, dVars):
    if sToken.lower() == 'is':
        lObjects[iToken] = parser.context_is_keyword(sToken)
        dVars['bContextIsFound'] = True
        return True
    return False


def classify_context_identifier(sToken, iToken, lObjects, dVars):
    if not dVars['bContextIsFound'] and not isinstance(lObjects[iToken], parser.whitespace) and not isinstance(lObjects[iToken], parser.comment):
        lObjects[iToken] = parser.identifier(sToken)


def classify_context_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'context':
        lObjects[iToken] = parser.keyword(sToken)
        dVars['bInsideContext'] = True
        dVars['iCurrentIndentLevel'] += 1
        if iToken < 2:
            oLine.indentLevel = 0

def classify_context_reference_keyword(sToken, iToken, lObjects, dVars, oLine):
    if sToken.lower() == 'context':
        print('Got Here')
        lObjects[iToken] = parser.context_reference_keyword(sToken)
        dVars['bInsideContextReference'] = True
        oLine.indentLevel = dVars['iCurrentIndentLevel']


def reclassify_context_keyword_and_identifier(self, lObjects):
    lObjects.reverse()
    bKeywordFound = False
    for iObject, oObject in enumerate(lObjects):
        if isinstance(oObject, parser.context_is_keyword):
            continue
        if type(oObject) ==  parser.identifier:
            lObjects[iObject] = parser.context_identifier(oObject.get_value()) 
        if type(oObject) == parser.keyword:
            lObjects[iObject] = parser.context_keyword(oObject.get_value()) 
            bKeywordFound = True
            break
    lObjects.reverse()

    if not bKeywordFound:
        bBreak = False
        for oLine in self.lines[::-1]:
            myObjects = oLine.get_objects()
            myObjects.reverse()
            for iObject, oObject in enumerate(myObjects):
                if type(oObject) == parser.identifier:
                    myObjects[iObject] = parser.context_identifier(oObject.get_value()) 
                if type(oObject) ==  parser.keyword:
                    myObjects[iObject] = parser.context_keyword(oObject.get_value()) 
                    bBreak = True
                    break
            myObjects.reverse()
            if bBreak:
                break


def classify_context_reference_comma(sToken, iToken, lObjects, dVars):
    if sToken == ',' and not isinstance(lObjects[iToken], parser.library_comma):
        lObjects[iToken] = parser.context_reference_comma()


def classify_context_reference_semicolon(sToken, iToken, lObjects, dVars):
    if sToken == ';' and not isinstance(lObjects[iToken], parser.library_semicolon) and not isinstance(lObjects[iToken], parser.use_semicolon) and not dVars['bContextEndFound']:
        lObjects[iToken] = parser.context_reference_semicolon()
        return True
    return False


def reclassify_context_reference_keyword_and_identifier(self, lObjects):
    lObjects.reverse()
    bKeywordFound = False
    for iObject, oObject in enumerate(lObjects):
        if (type(oObject) == parser.item or type(oObject) == parser.identifier) and not oObject.get_value().lower() == 'context':
            lObjects[iObject] = parser.context_reference_identifier(oObject.get_value()) 
        if (type(oObject) == parser.item or type(oObject) == parser.identifier) and oObject.get_value().lower() == 'context':
            lObjects[iObject] = parser.context_reference_keyword(oObject.get_value()) 
        if type(oObject) == parser.context_keyword:
            bKeywordFound = True
            break
    lObjects.reverse()

    if not bKeywordFound:
        bBreak = False
        for oLine in self.lines[::-1]:
            myObjects = oLine.get_objects()
            myObjects.reverse()
            for iObject, oObject in enumerate(myObjects):
                if (type(oObject) == parser.item or type(oObject) == parser.identifier) and not oObject.get_value().lower() == 'context':
                    myObjects[iObject] = parser.context_reference_identifier(oObject.get_value()) 
                if (type(oObject) == parser.item or type(oObject) == parser.identifier) and oObject.get_value().lower() == 'context':
                    myObjects[iObject] = parser.context_reference_keyword(oObject.get_value()) 
                if type(oObject) == parser.context_keyword:
                    bBreak = True
                    break
            myObjects.reverse()
            if bBreak:
                break


def reclassify_context_reference_keyword_and_identifier_outside_of_context_declaration(self, lObjects, dVars):
#    print('Entering reclassify_context_reference...')
#    print(lObjects)
    lObjects.reverse()
    bKeywordFound = False
    for iObject, oObject in enumerate(lObjects):
#        print(oObject)
#        print(oObject.get_value())
        if type(oObject) == parser.identifier:
            lObjects[iObject] = parser.context_reference_identifier(oObject.get_value()) 
        if type(oObject) == parser.keyword:
            lObjects[iObject] = parser.context_reference_keyword(oObject.get_value()) 
#            print('  Context keyword found')
        if type(oObject) == parser.context_keyword:
            bKeywordFound = True
            break
    lObjects.reverse()

    if not bKeywordFound:
#        print('Reading previous lines')
        bBreak = False
        for oLine in self.lines[::-1]:
            myObjects = oLine.get_objects()
#            print(oLine.line)
#            print(myObjects)
            myObjects.reverse()
            for iObject, oObject in enumerate(myObjects):
#                print(oObject)
                if type(oObject) == parser.identifier:
                    myObjects[iObject] = parser.context_reference_identifier(oObject.get_value()) 
                if type(oObject) == parser.keyword:
                    myObjects[iObject] = parser.context_reference_keyword(oObject.get_value()) 
                if type(oObject) == parser.context_keyword:
                    bBreak = True
                    break
            myObjects.reverse()
            if bBreak:
                break
#    print('-'*80)
    dVars['bInsideContext'] = False
    dVars['bContextIsFound'] = False
    dVars['bContextEndFound'] = False
