
import re

from vsg import line
from vsg.vhdlFile import update
from vsg.vhdlFile import classify
from vsg.vhdlFile.classify import design_file
from vsg.vhdlFile.classify import entity

from vsg.token import use_clause as use_clause_token
from vsg.token import package_declaration
from vsg.token import package_body
from vsg.token import architecture_body
from vsg.token import constant_declaration

from vsg import parser


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
        self._processFile()
        self.filename = None

    def _processFile(self):

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

        dVars['bInsideContext'] = False
        dVars['bContextIsFound'] = False
        dVars['bContextEndFound'] = False

        dVars['bInsideContextReference'] = False

        dVars['bInsideLibrary'] = False

        dVars['bInsideUse'] = False
        dVars['bUseClauseKeywordFound'] = False

        dVars['bArchitectureKeywordFound'] = False
        dVars['bArchitectureIdentifierFound'] = False
        dVars['bArchitectureEntityNameFound'] = False
        dVars['bArchitectureIsKeywordFound'] = False
        dVars['bArchitectureBeginKeywordFound'] = False
        dVars['bArchitectureEndKeywordFound'] = False

        dVars['bEntityKeywordFound'] = False
        dVars['bEntityIdentifierFound'] = False
        dVars['bEntityIsKeywordFound'] = False
        dVars['bEntityBeginKeywordFound'] = False
        dVars['bEntityEndKeywordFound'] = False

        dVars['bPackageKeywordFound'] = False
        dVars['bPackageIdentifierFound'] = False
        dVars['bPackageIsKeywordFound'] = False
        dVars['bPackageEndKeywordFound'] = False
        dVars['bPackageBodyKeywordFound'] = False

        dVars['bPackageBodyPackageKeywordFound'] = False
        dVars['bPackageBodyIdentifierFound'] = False
        dVars['bPackageBodyIsKeywordFound'] = False
        dVars['bPackageBodyEndKeywordFound'] = False
        dVars['bPackageBodyBodyKeywordFound'] = False

        dVars['bSignalKeywordFound'] = False
        dVars['bSignalColonFound'] = False
        dVars['bSignalAssignmentOperatorFound'] = False

        dVars['bConstantKeywordFound'] = False
        dVars['bConstantColonFound'] = False
        dVars['bConstantAssignmentOperatorFound'] = False

        dVars['bVariableKeywordFound'] = False
        dVars['bVariableColonFound'] = False
        dVars['bVariableAssignmentOperatorFound'] = False

        dVars['bSharedVariableKeywordFound'] = False
        dVars['bSharedVariableColonFound'] = False
        dVars['bSharedVariableAssignmentOperatorFound'] = False

        dVars['bAssertKeywordFound'] = False
        dVars['bAssertReportKeywordFound'] = False
        dVars['bAssertSeverityKeywordFound'] = False

        dVars['bFileKeywordFound'] = False
        dVars['bFileColonFound'] = False
        dVars['bFileOpenKeywordFound'] = False
        dVars['bFileIsKeywordFound'] = False

        dVars['bAttributeKeywordFound'] = False
        dVars['bAttributeColonFound'] = False

        dVars['bComponentKeywordFound'] = False
        dVars['bComponentIdentifierFound'] = False
        dVars['bComponentIsKeywordFound'] = False
        dVars['bComponentEndKeywordFound'] = False

        dVars['bGenericClauseKeywordFound'] = False
        dVars['bGenericClauseOpenParenthesisFound'] = False
        dVars['bGenericClauseCloseParenthesisFound'] = False

        dVars['bPortClauseKeywordFound'] = False
        dVars['bPortClauseOpenParenthesisFound'] = False
        dVars['bPortClauseCloseParenthesisFound'] = False

        dVars['bInterfaceSignalDeclarationAssignmentOperatorFound'] = False
        dVars['bInterfaceSignalDeclarationColonFound'] = False

        dVars['objectQueue'] = []

        oLinePrevious = line.blank_line()

        for sLine in self.filecontent:
            oLine = line.line(sLine.replace('\t', '  ').rstrip())
            lTokens = oLine.get_zipped_tokens()
            lObjects = [] 
            for sToken in lTokens:
                lObjects.append(parser.item(sToken))
            
#            preIndent = str(dVars['iCurrentIndentLevel'])
            update.inside_attributes(dVars, self.lines[-1], oLine)

            classify.blank(oLine) # lTokens
            classify.whitespace(lTokens, lObjects)
            classify.comment(dVars, lTokens, lObjects, oLine)

            for iObject, oObject in enumerate(lObjects):
                design_file.tokenize(oObject, iObject, lObjects, dVars)
#                use_clause.tokenize(oObject, iObject, lObjects, dVars)
#                entity_declaration.tokenize(oObject, iObject, lObjects, dVars)
#                architecture_body.tokenize(oObject, iObject, lObjects, dVars)


            classify.library(dVars, lTokens, lObjects, oLine)
            classify.use(dVars, lTokens, lObjects, oLine)
            classify.context(self, dVars, lTokens, lObjects, oLine)
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
            classify.type_definition(dVars, oLine)
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
            oLinePrevious = oLine
            oLine.objects = lObjects
#            print('-'*80)
#            print(oLine.line)
#            print(lObjects)
#            print('[' + preIndent + '][' + oLine.line + '][' + str(oLine.indentLevel) + ']')
        self.set_indent_levels()
        self.classify_package_keywords()
#        self.print_debug()


    def update_filecontent(self):
        self.filecontent = []
        for oLine in self.lines[1:]:
            self.filecontent.append(oLine.line)
        self.lines = [line.line('')]

    def get_lines(self):
        return self.lines

    def get_line(self, iLineNumber):
        return self.lines[iLineNumber]

    def get_context_declarations(self):
        lReturn = []
        dContext = {}
        dContext['metadata'] = {}
        dContext['metadata']['iStartLineNumber'] = 0
        dContext['metadata']['iEndLineNumber'] = 0
        dContext['lines'] = []
        bContextKeywordFound = False
        bContextColonFound = False
        for iLine, oLine in enumerate(self.lines):
            for oObject in oLine.objects:
                if isinstance(oObject, parser.context_keyword):
                    bContextKeywordFound = True
                    dContext['metadata']['iStartLineNumber'] = iLine
                if isinstance(oObject, parser.context_semicolon):   
                    bContextColonFound = True
                    dContext['metadata']['iEndLineNumber'] = iLine
            if bContextKeywordFound:
                dContext['lines'].append(oLine)
            if bContextColonFound:
                lReturn.append(dContext)
                dContext = {}
                dContext['metadata'] = {}
                dContext['metadata']['iStartLineNumber'] = 0
                dContext['metadata']['iEndLineNumber'] = 0
                dContext['lines'] = []
                bContextKeywordFound = False
                bContextColonFound = False
        return lReturn
  
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
            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, parser.context_keyword):
                oLine.indentLevel = 0
                dIndent['insideContextDeclaration'] = True
            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, parser.context_end_keyword):
                oLine.indentLevel = 0
                dIndent['insideContextDeclaration'] = False
            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, parser.context_reference_keyword):
                if dIndent['insideContextDeclaration']:
                    oLine.indentLevel = 2
                else:
                    oLine.indentLevel = 1
            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, parser.library_keyword):
                if dIndent['insideContextDeclaration']:
                    oLine.indentLevel = 1
                else:
                    oLine.indentLevel = 0
            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, use_clause_token.keyword):
                if dIndent['insideContextDeclaration']:
                    oLine.indentLevel = 2
                else:
                    oLine.indentLevel = 1

            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, architecture_body.keyword):
                dIndent['level'] = 1
                oLine.indentLevel = 0

            if len(oLine.objects) == 0:
                continue

            if _does_line_start_with_item_or_whitespace_and_then_item(oLine, constant_declaration.assignment_expression):
                if type(oLine.objects[0]) == constant_declaration.assignment_expression:
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

    def classify_package_keywords(self):
        '''
        Assigns the correct package object to the package keywords.
        '''
        bPackageIdentifierFound = False
        bPackageBodyBodyKeywordFound = False
        for iLine, oLine in enumerate(self.lines[::-1]):
            for iObject, oObject in enumerate(oLine.objects[::-1]):
                if type(oObject) == parser.item and bPackageIdentifierFound:
                    iIndex = len(oLine.objects) - iObject - 1
                    oLine.objects[iIndex] = package_declaration.keyword(oObject.get_value())
                    bPackageIdentifierFound = False                

                if type(oObject) == package_declaration.identifier and not bPackageIdentifierFound:
                    bPackageIdentifierFound = True

                if type(oObject) == parser.item and bPackageBodyBodyKeywordFound:
                    iIndex = len(oLine.objects) - iObject - 1
                    oLine.objects[iIndex] = package_body.package_keyword(oObject.get_value())
                    bPackageBodyBodyKeywordFound = False                

                if type(oObject) == package_body.body_keyword and not bPackageBodyBodyKeywordFound:
                    bPackageBodyBodyKeywordFound = True

    def print_debug(self):
        for oLine in self.lines:
#            print('-'*80)
            print(f'{oLine.indentLevel} | {oLine.line}')
#            for oObject in oLine.objects:
#                print(oObject)
        

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
