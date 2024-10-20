# -*- coding: utf-8 -*-

import re

from vsg import violation

camelCase = re.compile("(?:[a-z])+(?:[a-z0-9])*((?:[A-Z])+(?:[a-z0-9])+)*([A-Z])?")
PascalCase = re.compile("((?:[A-Z])+(?:[a-z0-9])+)+([A-Z])?")


def check_for_case_violation(oToi, self, check_prefix=False, check_suffix=False, check_whole=False, iIndex=0, iLine=None):
    sObjectValue = get_token_value(oToi, iIndex)
    iMyLine = get_violation_line(oToi, iLine)
    oViolation = None

    if self.name != "bit_string_literal" and does_not_contain_any_alpha_characters(sObjectValue):
        return None

    elif case_exception_found(sObjectValue, self):
        oViolation = check_for_exception(sObjectValue, self, oToi, iIndex, iMyLine)

    else:
        oViolation = dChecker[check_prefix][check_suffix](sObjectValue, self, oToi, iIndex, iMyLine, dCase[self.case]["check"])

    return oViolation


def get_token_value(oToi, iIndex):
    return oToi.get_tokens()[iIndex].get_value()


def prefix_detected(sString, lPrefixes):
    sLowerString = sString.lower()
    for sPrefix in lPrefixes:
        if sLowerString.startswith(sPrefix.lower()):
            return True
    return False


def get_matched_prefix(sString, lPrefixes):
    sLowerString = sString.lower()
    for sPrefix in lPrefixes:
        if sLowerString.startswith(sPrefix.lower()):
            return sPrefix


def extract_prefix(sString, sPrefix):
    return sString[0 : len(sPrefix)]


def remove_prefix(sString, sPrefix):
    return sString[len(sPrefix) :]


def suffix_detected(sString, lSuffixes):
    sLowerString = sString.lower()
    for sSuffix in lSuffixes:
        if sLowerString.endswith(sSuffix.lower()):
            return True
    return False


def get_matched_suffix(sString, lSuffixes):
    sLowerString = sString.lower()
    for sSuffix in lSuffixes:
        if sLowerString.endswith(sSuffix.lower()):
            return sSuffix


def extract_suffix(sString, sSuffix):
    return sString[len(sString) - len(sSuffix) :]


def remove_suffix(sString, sSuffix):
    return sString[0 : len(sString) - len(sSuffix)]


def create_case_violation(sActual, sExpected, oToi, iIndex, iLine, sSolution=None):
    if sSolution is None:
        sSolution = 'Change "' + sActual + '" to "' + sExpected + '"'
    oViolation = violation.New(iLine, oToi, sSolution)
    dAction = {}
    dAction["value"] = sExpected
    dAction["index"] = iIndex
    oViolation.set_action(dAction)
    return oViolation


def get_violation_line(oToi, iLine):
    if iLine is None:
        return oToi.get_line_number()
    return iLine


def is_exception_enabled(lList):
    if len(lList) == 0:
        return False
    return True


def check_for_lower_case(sActualValue, sPrefix, sWord, sSuffix, oToi, iIndex, iLine, self):
    sExpectedValue = sPrefix + sWord.lower() + sSuffix
    if not sActualValue == sExpectedValue:
        return create_case_violation(sActualValue, sExpectedValue, oToi, iIndex, iLine)


def check_for_upper_case(sActualValue, sPrefix, sWord, sSuffix, oToi, iIndex, iLine, self):
    sExpectedValue = sPrefix + sWord.upper() + sSuffix
    if not sActualValue == sExpectedValue:
        return create_case_violation(sActualValue, sExpectedValue, oToi, iIndex, iLine)


def check_for_upper_or_lower_case(sActualValue, sPrefix, sWord, sSuffix, oToi, iIndex, iLine, self):
    sExpectedUpperValue = sPrefix + sWord.upper() + sSuffix
    sExpectedLowerValue = sPrefix + sWord.lower() + sSuffix
    if not sActualValue == sExpectedUpperValue and not sActualValue == sExpectedLowerValue:
        sSolution = f'Change "{sActualValue}" to "{sExpectedUpperValue}" or "{sExpectedLowerValue}"'
        return create_case_violation(sActualValue, None, oToi, iIndex, iLine, sSolution)


def check_for_camelcase(sActualValue, sPrefix, sWord, sSuffix, oToi, iIndex, iLine, self):
    sExpectedValue = sPrefix + sWord + sSuffix
    if camelCase.fullmatch(sWord) is None:
        sSolution = "Format " + sActualValue + " into camelCase"
        return create_case_violation(sActualValue, sExpectedValue, oToi, iIndex, iLine, sSolution)


def check_for_pascalcase(sActualValue, sPrefix, sWord, sSuffix, oToi, iIndex, iLine, self):
    sExpectedValue = sPrefix + sWord + sSuffix
    if PascalCase.fullmatch(sWord) is None:
        sSolution = "Format " + sActualValue + " into PascalCase"
        return create_case_violation(sActualValue, sExpectedValue, oToi, iIndex, iLine, sSolution)


def check_for_regex(sActualValue, sPrefix, sWord, sSuffix, oToi, iIndex, iLine, self):
    sExpectedValue = sPrefix + sWord + sSuffix
    if self.oRegex.fullmatch(sWord) is None:
        sSolution = "Format " + sActualValue + " to match defined regex"
        return create_case_violation(sActualValue, sExpectedValue, oToi, iIndex, iLine, sSolution)


def check_for_case(sObjectValue, self, oToi, iIndex, iLine, fCheck):
    return fCheck(sObjectValue, "", sObjectValue, "", oToi, iIndex, iLine, self)


def check_for_prefix_exception(sObjectValue, self, oToi, iIndex, iLine, fCheck):
    sDesiredPrefix = ""
    sConstant = sObjectValue
    sDesiredSuffix = ""
    if prefix_detected(sObjectValue, self.prefix_exceptions):
        sDesiredPrefix = get_matched_prefix(sObjectValue, self.prefix_exceptions)
        sActualPrefix = extract_prefix(sObjectValue, sDesiredPrefix)
        sConstant = remove_prefix(sObjectValue, sActualPrefix)

    return fCheck(sObjectValue, sDesiredPrefix, sConstant, "", oToi, iIndex, iLine, self)


#    else:
#        return fCheck(sObjectValue, '', sObjectValue, '', oToi, iIndex, iLine)


def check_for_suffix_exception(sObjectValue, self, oToi, iIndex, iLine, fCheck):
    sDesiredPrefix = ""
    sConstant = sObjectValue
    sDesiredSuffix = ""
    if suffix_detected(sObjectValue, self.suffix_exceptions):
        sDesiredSuffix = get_matched_suffix(sObjectValue, self.suffix_exceptions)
        sActualSuffix = extract_suffix(sObjectValue, sDesiredSuffix)
        sConstant = remove_suffix(sObjectValue, sActualSuffix)

    return fCheck(sObjectValue, "", sConstant, sDesiredSuffix, oToi, iIndex, iLine, self)


#    else:
#        return fCheck(sObjectValue, '', sObjectValue, '', oToi, iIndex, iLine)


def check_for_prefix_and_suffix_exceptions(sObjectValue, self, oToi, iIndex, iLine, fCheck):
    sDesiredPrefix = ""
    sConstant = sObjectValue
    sDesiredSuffix = ""
    if prefix_detected(sObjectValue, self.prefix_exceptions) and suffix_detected(sObjectValue, self.suffix_exceptions):
        sDesiredPrefix = get_matched_prefix(sObjectValue, self.prefix_exceptions)
        sActualPrefix = extract_prefix(sObjectValue, sDesiredPrefix)
        sConstant = remove_prefix(sObjectValue, sActualPrefix)
        sDesiredSuffix = get_matched_suffix(sConstant, self.suffix_exceptions)
        sActualSuffix = extract_suffix(sConstant, sDesiredSuffix)
        sConstant = remove_suffix(sConstant, sActualSuffix)
        sExpected = sDesiredPrefix + sConstant.lower() + sDesiredSuffix
    elif prefix_detected(sObjectValue, self.prefix_exceptions):
        sDesiredPrefix = get_matched_prefix(sObjectValue, self.prefix_exceptions)
        sActualPrefix = extract_prefix(sObjectValue, sDesiredPrefix)
        sConstant = remove_prefix(sObjectValue, sActualPrefix)
    elif suffix_detected(sObjectValue, self.suffix_exceptions):
        sDesiredSuffix = get_matched_suffix(sObjectValue, self.suffix_exceptions)
        sActualSuffix = extract_suffix(sObjectValue, sDesiredSuffix)
        sConstant = remove_suffix(sObjectValue, sActualSuffix)

    return fCheck(sObjectValue, sDesiredPrefix, sConstant, sDesiredSuffix, oToi, iIndex, iLine, self)


def case_exception_found(sObjectValue, self):
    if sObjectValue.lower() in self.case_exceptions_lower:
        return True
    return False


def check_for_exception(sObjectValue, self, oToi, iIndex, iLine):
    iIndex = self.case_exceptions_lower.index(sObjectValue.lower())
    if sObjectValue != self.case_exceptions[iIndex]:
        return create_case_violation(sObjectValue, self.case_exceptions[iIndex], oToi, iIndex, iLine)


def does_not_contain_any_alpha_characters(sObjectValue):
    if sObjectValue.startswith('"'):
        return True
    return False


# Define mapping of case to checkers and comparators
dCase = {}
dCase["camelCase"] = {}
dCase["camelCase"]["check"] = check_for_camelcase
dCase["PascalCase"] = {}
dCase["PascalCase"]["check"] = check_for_pascalcase
dCase["regex"] = {}
dCase["regex"]["check"] = check_for_regex
dCase["lower"] = {}
dCase["lower"]["check"] = check_for_lower_case
dCase["upper"] = {}
dCase["upper"]["check"] = check_for_upper_case
dCase["upper_or_lower"] = {}
dCase["upper_or_lower"]["check"] = check_for_upper_or_lower_case

# Define mapping of exceptions to functions
dChecker = {}
dChecker[True] = {}
dChecker[False] = {}
dChecker[False][False] = check_for_case
dChecker[False][True] = check_for_suffix_exception
dChecker[True][False] = check_for_prefix_exception
dChecker[True][True] = check_for_prefix_and_suffix_exceptions
