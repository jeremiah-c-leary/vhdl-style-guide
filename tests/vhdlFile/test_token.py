# -*- coding: utf-8 -*-

import pathlib
import unittest

import vsg.vhdlFile as vhdlFile
from tests import utils

sTestInputFileName = "classification_test_input.vhd"
sTestResultFileName = "classification_results.txt"


def get_lrm_unit_paths():
    lTestInputPaths = pathlib.Path(__file__).parent.glob("*/" + sTestInputFileName)
    lReturn = [path.parent for path in lTestInputPaths]
    return lReturn


class test_classification_meta(type):
    __test__ = False

    def __new__(oClass, sName, oBases, dNamespace):
        def generate_test(oLrmUnitPath):
            def test_classification(self):

                lFile, eError = vhdlFile.utils.read_vhdlfile(str(oLrmUnitPath.joinpath(sTestInputFileName)))
                oFile = vhdlFile.vhdlFile(lFile)

                self.maxDiff = None

                lExpected = []
                utils.read_file(str(oLrmUnitPath.joinpath(sTestResultFileName)), lExpected, False)

                lActual = []

                for oObject in utils.extract_objects(oFile, True):
                    lActual.append(str(oObject))

                self.assertEqual(lExpected, lActual)

            return test_classification

        for oLrmUnitPath in get_lrm_unit_paths():
            test_name = "test_" + oLrmUnitPath.name
            dNamespace[test_name] = generate_test(oLrmUnitPath)
        return type.__new__(oClass, sName, oBases, dNamespace)


class test_classification(unittest.TestCase, metaclass=test_classification_meta):
    __metaclass__ = test_classification_meta
    __test__ = True
