
from vsg import violation


def is_exception_enabled(lList):
    if len(lList) == 0:
        return False
    return True 


def check_for_case_violation(oToi, self, check_prefix=False, check_suffix=False, iIndex=0, iLine=None):
    sObjectValue = oToi.get_tokens()[iIndex].get_value()
    iMyLine = get_violation_line(oToi, iLine)

    if self.case == 'lower' and not check_prefix and not check_suffix:
        if not sObjectValue.islower():
            return create_case_violation(sObjectValue, sObjectValue.lower(), oToi, iIndex, iMyLine)

    if self.case == 'lower' and check_prefix and not check_suffix:
        if prefix_detected(sObjectValue, self.prefix_exceptions):
            sDesiredPrefix = get_matched_prefix(sObjectValue, self.prefix_exceptions)
            sActualPrefix = extract_prefix(sObjectValue, sDesiredPrefix)
            sConstant = remove_prefix(sObjectValue, sActualPrefix)
            sExpected = sDesiredPrefix + sConstant.lower()
            if sObjectValue != sExpected:
                return create_case_violation(sObjectValue, sExpected, oToi, iIndex, iMyLine)
        elif not sObjectValue.islower():
            return create_case_violation(sObjectValue, sObjectValue.lower(), oToi, iIndex, iMyLine)

    if self.case == 'lower' and not check_prefix and check_suffix:
        if suffix_detected(sObjectValue, self.suffix_exceptions):
            sDesiredSuffix = get_matched_suffix(sObjectValue, self.suffix_exceptions)
            sActualSuffix = extract_suffix(sObjectValue, sDesiredSuffix)
            sConstant = remove_suffix(sObjectValue, sActualSuffix)
            sExpected = sConstant.lower() + sDesiredSuffix
            if sObjectValue != sExpected:
                return create_case_violation(sObjectValue, sExpected, oToi, iIndex, iMyLine)
        elif not sObjectValue.islower():
            return create_case_violation(sObjectValue, sObjectValue.lower(), oToi, iIndex, iMyLine)

    if self.case == 'lower' and check_prefix and check_suffix:
        if prefix_detected(sObjectValue, self.prefix_exceptions) and suffix_detected(sObjectValue, self.suffix_exceptions):
            sDesiredPrefix = get_matched_prefix(sObjectValue, self.prefix_exceptions)
            sActualPrefix = extract_prefix(sObjectValue, sDesiredPrefix)
            sConstant = remove_prefix(sObjectValue, sActualPrefix)
            sDesiredSuffix = get_matched_suffix(sConstant, self.suffix_exceptions)
            sActualSuffix = extract_suffix(sConstant, sDesiredSuffix)
            sConstant = remove_suffix(sConstant, sActualSuffix)
            sExpected = sDesiredPrefix + sConstant.lower() + sDesiredSuffix
            if sObjectValue != sExpected:
                return create_case_violation(sObjectValue, sExpected, oToi, iIndex, iMyLine)
        elif not sObjectValue.islower():
            return create_case_violation(sObjectValue, sObjectValue.lower(), oToi, iIndex, iMyLine)

    if self.case == 'upper' and not check_prefix and not check_suffix:
        if not sObjectValue.isupper():
            return create_case_violation(sObjectValue, sObjectValue.upper(), oToi, iIndex, iMyLine)

    if self.case == 'upper' and check_prefix and not check_suffix:
        if prefix_detected(sObjectValue, self.prefix_exceptions):
            sDesiredPrefix = get_matched_prefix(sObjectValue, self.prefix_exceptions)
            sActualPrefix = extract_prefix(sObjectValue, sDesiredPrefix)
            sConstant = remove_prefix(sObjectValue, sActualPrefix)
            sExpected = sDesiredPrefix + sConstant.upper()
            if sObjectValue != sExpected:
                return create_case_violation(sObjectValue, sExpected, oToi, iIndex, iMyLine)
        elif not sObjectValue.isupper():
            return create_case_violation(sObjectValue, sObjectValue.upper(), oToi, iIndex, iMyLine)

    if self.case == 'upper' and not check_prefix and check_suffix:
        if suffix_detected(sObjectValue, self.suffix_exceptions):
            sDesiredSuffix = get_matched_suffix(sObjectValue, self.suffix_exceptions)
            sActualSuffix = extract_suffix(sObjectValue, sDesiredSuffix)
            sConstant = remove_suffix(sObjectValue, sActualSuffix)
            sExpected = sConstant.upper() + sDesiredSuffix
            if sObjectValue != sExpected:
                return create_case_violation(sObjectValue, sExpected, oToi, iIndex, iMyLine)
        elif not sObjectValue.isupper():
            return create_case_violation(sObjectValue, sObjectValue.upper(), oToi, iIndex, iMyLine)

    if self.case == 'upper' and check_prefix and check_suffix:
        if prefix_detected(sObjectValue, self.prefix_exceptions) and suffix_detected(sObjectValue, self.suffix_exceptions):
            sDesiredPrefix = get_matched_prefix(sObjectValue, self.prefix_exceptions)
            sActualPrefix = extract_prefix(sObjectValue, sDesiredPrefix)
            sConstant = remove_prefix(sObjectValue, sActualPrefix)
            sDesiredSuffix = get_matched_suffix(sConstant, self.suffix_exceptions)
            sActualSuffix = extract_suffix(sConstant, sDesiredSuffix)
            sConstant = remove_suffix(sConstant, sActualSuffix)
            sExpected = sDesiredPrefix + sConstant.upper() + sDesiredSuffix
            if sObjectValue != sExpected:
                return create_case_violation(sObjectValue, sExpected, oToi, iIndex, iMyLine)
        elif not sObjectValue.isupper():
            return create_case_violation(sObjectValue, sObjectValue.upper(), oToi, iIndex, iMyLine)


def prefix_detected(sString, lPrefixes):
    sLowerString = sString.lower()
    for sPrefix in lPrefixes:
       if sLowerString.startswith(sPrefix.lower()):
           return True
    else:
        return False 


def get_matched_prefix(sString, lPrefixes):
    sLowerString = sString.lower()
    for sPrefix in lPrefixes:
       if sLowerString.startswith(sPrefix.lower()):
           return sPrefix


def extract_prefix(sString, sPrefix):
    return sString[0:len(sPrefix)]


def remove_prefix(sString, sPrefix):
    return sString[len(sPrefix):]


def suffix_detected(sString, lSuffixes):
    sLowerString = sString.lower()
    for sSuffix in lSuffixes:
       if sLowerString.endswith(sSuffix.lower()):
           return True
    else:
        return False 


def get_matched_suffix(sString, lSuffixes):
    sLowerString = sString.lower()
    for sSuffix in lSuffixes:
       if sLowerString.endswith(sSuffix.lower()):
           return sSuffix


def extract_suffix(sString, sSuffix):
    return sString[len(sString) - len(sSuffix):]


def remove_suffix(sString, sSuffix):
    return sString[0:len(sString) - len(sSuffix)]


def create_case_violation(sActual, sExpected, oToi, iIndex, iLine):
    sSolution = 'Change "' + sActual + '" to "' + sExpected + '"'
    oViolation = violation.New(iLine, oToi, sSolution)
    dAction = {}
    dAction['value'] = sExpected
    dAction['index'] = iIndex
    oViolation.set_action(dAction)
    return oViolation


def get_violation_line(oToi, iLine):
    if iLine is None:
        return oToi.get_line_number()
    else:
        return iLine
    

