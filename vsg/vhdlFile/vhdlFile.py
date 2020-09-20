
from vsg import line
from vsg.vhdlFile import update
from vsg.vhdlFile import classify
from vsg.vhdlFile.classify import entity

from vsg import parser
from vsg import token

from vsg.vhdlFile.classify_new import blank
from vsg.vhdlFile.classify_new import comment
from vsg.vhdlFile.classify_new import design_file
from vsg.vhdlFile.classify_new import whitespace


class vhdlFile():
    '''
    Holds contents of a VHDL file.
    When a vhdlFile object is created, the contents of the file must be passed to it.
    A line object is created for each line read in.
    Then the line object attributes are updated.

    Parameters:

       filecontent: (list)

    Returns:

       fileobject
    '''
    def __init__(self, filecontent):
        self.filecontent = filecontent
        self.lines = [line.line('')]
        self.hasArchitecture = False
        self.hasEntity = False
        self.lAllObjects = []
        self._processFile()
        self.filename = None

    def _processFile(self):

        self.lAllObjects = []

        dVars = {}
        dVars['fFoundProcessBegin'] = False
        dVars['SensitivityListFound'] = False
        dVars['fProcedureParameterEndDetected'] = False
        dVars['fProcedureIsDetected'] = False
        dVars['fProcedureBeginDetected'] = False
        dVars['fFunctionParameterEndDetected'] = False
        dVars['fFunctionIsDetected'] = False
        dVars['fFunctionBeginDetected'] = False
        dVars['fFunctionReturnTypeDetected'] = False
        dVars['iOpenParenthesis'] = 0
        dVars['iCloseParenthesis'] = 0
        dVars['iCurrentIndentLevel'] = 0
        dVars['iGenerateLevel'] = 0
        dVars['iIfLevel'] = 0
        dVars['fConstantArray'] = False
        dVars['iForLoopLevel'] = 0
        dVars['bFirstWhenSeen'] = False

        oLinePrevious = line.blank_line()

        for sLine in self.filecontent:
            oLine = line.line(sLine.replace('\t', '  ').rstrip())
            lTokens = oLine.get_zipped_tokens()
            lObjects = []
            for sToken in lTokens:
                lObjects.append(parser.item(sToken))

            blank.classify(lObjects, oLine)
            whitespace.classify(lTokens, lObjects)
            comment.classify(lTokens, lObjects)
            
            update.inside_attributes(dVars, self.lines[-1], oLine)

            classify.blank(oLine) # lTokens
#            classify.whitespace(lTokens, lObjects)
            classify.comment(dVars, lTokens, lObjects, oLine)


            classify.use(dVars, lTokens, lObjects, oLine)

            classify.entity.legacy(self, dVars, oLine)
            classify.assert_statement(self, dVars, lTokens, lObjects, oLine)

            classify.code_tags(dVars, oLine, oLinePrevious)

            classify.port(dVars, oLine)
            classify.generic(dVars, oLine) #lTokens

            classify.concurrent(dVars, oLine)
            classify.architecture(self, dVars, lTokens, lObjects, oLine)
            classify.package_body_old(dVars, oLine) # lTokens
            classify.block(self, dVars, oLine)
            classify.package(self, dVars, lTokens, lObjects, oLine)
            classify.component(dVars, lTokens, lObjects, oLine)
            classify.signal(self, dVars, oLine)
            classify.constant(self, dVars, lTokens, lObjects, oLine, oLinePrevious)
            classify.variable(self, dVars, lTokens, lObjects, oLine)
            classify.procedure(dVars, oLine, oLinePrevious)
            classify.process(dVars, oLine, self.lines)
            classify.generate(dVars, oLine, oLinePrevious)
            classify.attribute(dVars, lTokens, lObjects, oLine)
            classify.file_statement(dVars, lTokens, lObjects, oLine)

            classify.when(dVars, oLine, oLinePrevious)

            classify.with_statement(dVars, oLine)
            classify.for_loop(dVars, oLine)
            classify.while_loop(dVars, oLine)

            classify.if_statement(dVars, oLine)

            classify.case(self, dVars, oLine)
            classify.function(dVars, oLine)
            classify.type_definition_old(dVars, oLine)
            classify.subtype(dVars, oLine)

            classify.sequential(dVars, oLine)
            classify.variable_assignment(dVars, oLine)
            classify.wait(dVars, oLine)
            classify.after(dVars, oLine)

            # Check instantiation statements
            if oLine.insideArchitecture and not oLine.insideProcess and \
               not oLine.isConcurrentBegin and \
               not oLine.insideComponent and \
               not oLine.isGenerateKeyword and \
               not oLine.insideFunction and \
               not oLine.insideProcedure:
                classify.instantiation(dVars, oLine)

            # Add line to file
            self.lines.append(oLine)

            self.lAllObjects.extend(lObjects)
            self.lAllObjects.append(parser.carriage_return())

            oLinePrevious = oLine
            oLine.objects = lObjects

        design_file.tokenize(self.lAllObjects)

        for iLine, lLine in enumerate(split_on_carriage_return(self.lAllObjects)):
            self.lines[iLine + 1].objects = lLine
        self.set_indent_levels()

    def update(self, lUpdates):
        if len(lUpdates) == 0:
            return
        for oUpdate in lUpdates[::-1]:
#            print(oUpdate)
            iStart = oUpdate.oTokens.iStartIndex
            lTokens = oUpdate.get_tokens()
            iEnd = oUpdate.oTokens.iEndIndex
            self.lAllObjects[iStart:iEnd] = lTokens
#        print(self.lAllObjects)
        for iLine, lLine in enumerate(split_on_carriage_return(self.lAllObjects)):
#            print(lLine)
            self.lines[iLine + 1].update_objects(lLine)
             
            

    def update_filecontent(self):
        self.filecontent = []
        for oLine in self.lines[1:]:
            self.filecontent.append(oLine.line)
        self.lines = [line.line('')]

    def get_lines(self):
        return self.lines

    def get_line(self, iLineNumber):
        return self.lines[iLineNumber]

    def insert_line(self, iLineNumber, oLine):
        self.lines.insert(iLineNumber, oLine)

    def remove_line(self, iLineNumber):
        self.lines.pop(iLineNumber)

    def get_lines_starting_with_item_or_whitespace_and_then_item(self, parserType):
        lReturn = []

        for iLine, oLine in enumerate(self.lines):
            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, parserType):
                dEntry = _create_empty_return_dictionary()
                dEntry['metadata']['iStartLineNumber'] = iLine
                dEntry['metadata']['iEndLineNumber'] = iLine
                dEntry['lines'].append(oLine)
                lReturn.append(dEntry)

        return lReturn

    def convert_whitespace_only_lines_to_blank_lines(self):
        print('Entering convert_whitespace_only_lines_to_blank_lines')
        for iLine, oLine in enumerate(self.lines):
            print(f'[{oLine.line}]')
            if oLine.line.isspace() or oLine.line == '':
                print('Got Here')
                self.lines.pop(iLine)
                self.lines.insert(iLine, line.blank_line())
            
    def get_region_bounded_by_items(self, beginItem, endItem):
        lReturn = []
        dRegion = {}
        dRegion['metadata'] = {}
        dRegion['metadata']['iStartLineNumber'] = 0
        dRegion['metadata']['iEndLineNumber'] = 0
        dRegion['lines'] = []
        bRegionBeginFound = False
        bRegionEndFound = False
        for iLine, oLine in enumerate(self.lines):
            for oObject in oLine.objects:
                if isinstance(oObject, beginItem):
                    bRegionBeginFound = True
                    dRegion['metadata']['iStartLineNumber'] = iLine
                if isinstance(oObject, endItem):   
                    bRegionEndFound = True
                    dRegion['metadata']['iEndLineNumber'] = iLine
            if bRegionBeginFound:
                dRegion['lines'].append(oLine)
            if bRegionEndFound:
                lReturn.append(dRegion)
                dRegion = {}
                dRegion['metadata'] = {}
                dRegion['metadata']['iStartLineNumber'] = 0
                dRegion['metadata']['iEndLineNumber'] = 0
                dRegion['lines'] = []
                bRegionBeginFound = False
                bRegionEndFound = False
        return lReturn

    def set_indent_levels(self):
        '''
        Set the appropriate indent level for lines using item objects.
        '''
        dIndent = {}
        dIndent['insideContextDeclaration'] = False
        dIndent['level'] = 0
        for oLine in self.lines:

            if len(oLine.objects) == 0:
                continue

            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, token.context_declaration.context_keyword):
                oLine.indentLevel = 0
                dIndent['insideContextDeclaration'] = True
            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, token.context_declaration.end_keyword):
                oLine.indentLevel = 0
                dIndent['insideContextDeclaration'] = False
            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, token.context_reference.keyword):
                if dIndent['insideContextDeclaration']:
                    oLine.indentLevel = 2
                else:
                    oLine.indentLevel = 1
            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, token.library_clause.keyword):
                if dIndent['insideContextDeclaration']:
                    oLine.indentLevel = 1
                else:
                    oLine.indentLevel = 0
            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, token.use_clause.keyword):
                if dIndent['insideContextDeclaration']:
                    oLine.indentLevel = 2
                else:
                    oLine.indentLevel = 1

            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, token.architecture_body.architecture_keyword):
                dIndent['level'] = 1
                oLine.indentLevel = 0

            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, token.constant_declaration.assignment_operator):
                if type(oLine.objects[0]) == token.constant_declaration.assignment_operator:
                    if oLine.objects[0].get_value() == '(':
                        oLine.indentLevel = dIndent['level']
                        dIndent['level'] += 1
                    elif oLine.objects[0].get_value() == ')':
                        dIndent['level'] -= 1
                        oLine.indentLevel = dIndent['level']
                    else:
                        oLine.indentLevel = dIndent['level']
                else:
                    oObject = oLine.objects[1]
                    sValue = oObject.get_value()
                    if oLine.objects[1].get_value() == '(':
                        oLine.indentLevel = dIndent['level']
                        dIndent['level'] += 1
                    elif oLine.objects[1].get_value() == ')':
                        dIndent['level'] -= 1
                        oLine.indentLevel = dIndent['level']
                    else:
                        oLine.indentLevel = dIndent['level']

    def print_debug(self):
        for oLine in self.lines:
            print(f'{oLine.indentLevel} | {oLine.line}')
        

    def get_sequence_of_tokens_matching(self, lTokens):
        iLine = 1
        lTemp = []
        lReturn = []
        iMatchCount = 0
        iMatchLength = len(lTokens)
        iStart = 0
        for iIndex in range(0, len(self.lAllObjects)):
            if isinstance(self.lAllObjects[iIndex], lTokens[iMatchCount]):
                if iMatchCount == 0:
                    iStart = iIndex
                lTemp.append(self.lAllObjects[iIndex])
                iMatchCount +=1
                if iMatchCount == iMatchLength:
                    lReturn.append(Tokens(iStart, iLine, lTemp))
                    lTemp = []
                    iMatchCount = 0
            elif iMatchCount > 0:
                lTemp = []
                iMatchCount = 0

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1

        return lReturn

    def get_tokens_matching(self, lTokens):
        iLine = 1
        lReturn = []
        for iIndex in range(0, len(self.lAllObjects)):
            for oToken in lTokens:
                if isinstance(self.lAllObjects[iIndex], oToken):
                    lReturn.append(Tokens(iIndex, iLine, [self.lAllObjects[iIndex]]))

            if isinstance(self.lAllObjects[iIndex], parser.carriage_return):
                iLine +=1

        return lReturn


def _create_empty_return_dictionary():
    dReturn = {}
    dReturn['metadata'] = {}
    dReturn['metadata']['iStartLineNumber'] = 0
    dReturn['metadata']['iEndLineNumber'] = 0
    dReturn['lines'] = []
    return dReturn


def _does_line_start_with_item_or_whitespace_and_then_item(oLine, parserType):
    if isinstance(oLine.get_object(0), parserType):
        return True
    if isinstance(oLine.get_object(0), parser.whitespace) and isinstance(oLine.get_object(1), parserType):
        return True
    return False


def is_whitespace(oObject):
    if type(oObject) == parser.carriage_return:
        return True
    if type(oObject) == parser.blank_line:
        return True
    if type(oObject) == parser.comment:
        return True
    if type(oObject) == parser.whitespace:
        return True
    return False

def split_on_carriage_return(lObjects):
    lReturn = []
    lMyObjects = []
    iLine = 1
    for oObject in lObjects:
        if type(oObject) == parser.carriage_return:
            lReturn.append(lMyObjects)
            iLine += 1
            lMyObjects = []
        else:
            lMyObjects.append(oObject)
    if len(lMyObjects) > 0:
        lReturn.append(lMyObjects)
    return lReturn


class Tokens():

    def __init__(self, iStartIndex, iLine, lTokens):

        self.iStartIndex = iStartIndex
        self.lTokens = lTokens
        self.iLine = iLine
        self.iEndIndex = iStartIndex + len(lTokens)

    def get_tokens(self):
        return self.lTokens

    def set_tokens(self, lTokens):
        self.lTokens = lTokens

    def get_line_number(self):
        return self.iLine
