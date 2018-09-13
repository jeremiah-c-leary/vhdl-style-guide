
def update_entity_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideEntity and not oPreviousLine.isEndEntityDeclaration:
        oCurrentLine.insideEntity = True


def update_port_map_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insidePortMap and not oPreviousLine.isEndPortMap:
        oCurrentLine.insidePortMap = True


def update_generic_map_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideGenericMap and not oPreviousLine.isEndGenericMap:
        oCurrentLine.insideGenericMap = True


def update_architecture_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideArchitecture and not oPreviousLine.isEndArchitecture:
        oCurrentLine.insideArchitecture = True


def update_assert_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideAssert and not oPreviousLine.isAssertEnd:
        oCurrentLine.insideAssert = True


def update_process_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideProcess and not oPreviousLine.isEndProcess:
        oCurrentLine.insideProcess = True


def update_concurrent_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideConcurrent and not oPreviousLine.isEndConcurrent:
        oCurrentLine.insideConcurrent = True


def update_sensitivity_list_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideSensitivityList and not oPreviousLine.isSensitivityListEnd:
        oCurrentLine.insideSensitivityList = True


def update_if_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideIf and not (oPreviousLine.isEndIfKeyword or oPreviousLine.isThenKeyword):
        oCurrentLine.insideIf = True


def update_type_enumerated_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideTypeEnumerated and not oPreviousLine.isTypeEnumeratedEnd:
        oCurrentLine.insideTypeEnumerated = True


def update_subtype_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideSubtype and not oPreviousLine.isSubtypeEnd:
        oCurrentLine.insideSubtype = True


def update_type_array_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideTypeArray and not oPreviousLine.isTypeArrayEnd:
        oCurrentLine.insideTypeArray = True


def update_type_record_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideTypeRecord and not oPreviousLine.isTypeRecordEnd:
        oCurrentLine.insideTypeRecord = True


def update_case_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideCase and not oPreviousLine.isCaseIsKeyword:
        oCurrentLine.insideCase = True


def update_case_when_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideCaseWhen and not oPreviousLine.isCaseWhenEnd:
        oCurrentLine.insideCaseWhen = True


def update_sequential_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideSequential and not oPreviousLine.isSequentialEnd:
        oCurrentLine.insideSequential = True


def update_variable_assignment_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideVariableAssignment and not oPreviousLine.isVariableAssignmentEnd:
        oCurrentLine.insideVariableAssignment = True


def update_component_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideComponent and not oPreviousLine.isComponentEnd:
        oCurrentLine.insideComponent = True


def update_instantiation_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideInstantiation and not oPreviousLine.isInstantiationPortEnd:
        oCurrentLine.insideInstantiation = True


def update_instantiation_port_map_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideInstantiationPortMap and not oPreviousLine.isInstantiationPortEnd:
        oCurrentLine.insideInstantiationPortMap = True


def update_instantiation_generic_map_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideInstantiationGenericMap and not oPreviousLine.isInstantiationGenericEnd:
        oCurrentLine.insideInstantiationGenericMap = True


def update_package_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insidePackage and not oPreviousLine.isPackageEnd:
        oCurrentLine.insidePackage = True


def update_package_body_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insidePackageBody and not oPreviousLine.isPackageBodyEnd:
        oCurrentLine.insidePackageBody = True


def update_function_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideFunction and not oPreviousLine.isFunctionEnd:
        oCurrentLine.insideFunction = True


def update_procedure_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideProcedure and not oPreviousLine.isProcedureEnd:
        oCurrentLine.insideProcedure = True


def update_generate_attributes(dVars, oPreviousLine, oCurrentLine):

    if oPreviousLine.insideGenerate and oPreviousLine.isGenerateEnd:
        if dVars['iGenerateLevel'] > 0:
            oCurrentLine.insideGenerate = True
    elif oPreviousLine.insideGenerate and not oPreviousLine.isGenerateEnd:
        oCurrentLine.insideGenerate = True


def update_for_loop_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideForLoop and not oPreviousLine.isForLoopEnd:
        oCurrentLine.insideForLoop = True


def update_while_loop_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideWhileLoop and not oPreviousLine.isWhileLoopEnd:
        oCurrentLine.insideWhileLoop = True


def update_attribute_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideAttribute and not oPreviousLine.isAttributeEnd:
        oCurrentLine.insideAttribute = True


def update_file_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideFile and not oPreviousLine.isFileEnd:
        oCurrentLine.insideFile = True


def update_constant_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideConstant and not oPreviousLine.isConstantEnd:
        oCurrentLine.insideConstant = True

def update_block_attributes(oPreviousLine, oCurrentLine):

    if oPreviousLine.insideBlock and not oPreviousLine.isEndBlock:
        oCurrentLine.insideBlock = True


def inside_attributes(dVars, oPreviousLine, oCurrentLine):

    update_entity_attributes(oPreviousLine, oCurrentLine)
    update_port_map_attributes(oPreviousLine, oCurrentLine)
    update_generic_map_attributes(oPreviousLine, oCurrentLine)
    update_architecture_attributes(oPreviousLine, oCurrentLine)
    update_assert_attributes(oPreviousLine, oCurrentLine)
    update_process_attributes(oPreviousLine, oCurrentLine)
    update_concurrent_attributes(oPreviousLine, oCurrentLine)
    update_sensitivity_list_attributes(oPreviousLine, oCurrentLine)
    update_if_attributes(oPreviousLine, oCurrentLine)
    update_type_enumerated_attributes(oPreviousLine, oCurrentLine)
    update_type_array_attributes(oPreviousLine, oCurrentLine)
    update_type_record_attributes(oPreviousLine, oCurrentLine)
    update_subtype_attributes(oPreviousLine, oCurrentLine)
    update_case_attributes(oPreviousLine, oCurrentLine)
    update_case_when_attributes(oPreviousLine, oCurrentLine)
    update_sequential_attributes(oPreviousLine, oCurrentLine)
    update_variable_assignment_attributes(oPreviousLine, oCurrentLine)
    update_component_attributes(oPreviousLine, oCurrentLine)
    update_instantiation_attributes(oPreviousLine, oCurrentLine)
    update_instantiation_port_map_attributes(oPreviousLine, oCurrentLine)
    update_instantiation_generic_map_attributes(oPreviousLine, oCurrentLine)
    update_package_attributes(oPreviousLine, oCurrentLine)
    update_package_body_attributes(oPreviousLine, oCurrentLine)
    update_procedure_attributes(oPreviousLine, oCurrentLine)
    update_function_attributes(oPreviousLine, oCurrentLine)
    update_generate_attributes(dVars, oPreviousLine, oCurrentLine)
    update_for_loop_attributes(oPreviousLine, oCurrentLine)
    update_while_loop_attributes(oPreviousLine, oCurrentLine)
    update_attribute_attributes(oPreviousLine, oCurrentLine)
    update_file_attributes(oPreviousLine, oCurrentLine)
    update_constant_attributes(oPreviousLine, oCurrentLine)
    update_block_attributes(oPreviousLine, oCurrentLine)
