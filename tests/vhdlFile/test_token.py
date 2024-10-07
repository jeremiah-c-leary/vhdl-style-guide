# -*- coding: utf-8 -*-

import os
import pathlib
import unittest

import vsg.vhdlFile as vhdlFile
from tests import utils

sTestInputFileName = "classification_test_input.vhd"

def get_lrm_unit_names():
    lTestInputPaths = pathlib.Path(__file__).parent.glob("*/" + sTestInputFileName)
    lReturn = [path.parent.name for path in lTestInputPaths]
    return lReturn


class test_classification_meta(type):
    __test__ = False

    def __new__(oClass, sName, oBases, dNamespace):
        def generate_test(sLrmUnit):
            def test_classification(self):
                lFile, eError = vhdlFile.utils.read_vhdlfile(os.path.join(os.path.dirname(__file__), sLrmUnit, sTestInputFileName))
                oFile = vhdlFile.vhdlFile(lFile)

                self.maxDiff = None

                sTestDir = os.path.join(os.path.dirname(__file__), sLrmUnit)

                lExpected = []
                utils.read_file(os.path.join(sTestDir, "classification_results.txt"), lExpected, False)

                lActual = []

                for oObject in utils.extract_objects(oFile, True):
                    lActual.append(str(oObject))

                self.assertEqual(lExpected, lActual)

            return test_classification

        for sLrmUnit in get_lrm_unit_names():
            test_name = "test_" + sLrmUnit
            dNamespace[test_name] = generate_test(sLrmUnit)
        return type.__new__(oClass, sName, oBases, dNamespace)


class test_classification(unittest.TestCase, metaclass=test_classification_meta):
    __metaclass__ = test_classification_meta
    __test__ = True
