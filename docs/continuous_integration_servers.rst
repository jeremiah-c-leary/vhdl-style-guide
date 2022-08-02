Continuous Integration Servers
------------------------------

VSG supports options to facilitate integration with continuous integration severs such as Bamboo and GitLab.
The following command line options are available.

+-------------------------------+--------------------------------------------------------------------------------------------+
| Command Line Option           | Comment                                                                                    |
+===============================+============================================================================================+
| :code:`--junit`               | Generate `JUnit report <continuous_integration_servers.html#JUnit-report>`_                |
+-------------------------------+--------------------------------------------------------------------------------------------+
| :code:`--quality_report`      | Generate `code quality report <continuous_integration_servers.html#Code-Quality-Report>`_  |
+-------------------------------+--------------------------------------------------------------------------------------------+

JUnit Report
############

VSG can generate a report of an analysis in JUnit XML format.
This report will include the filename along with any errors detected.
The rule which was violated, the line number where the violation occured, and the proposed solution are provided.

This report can be used in most CI server applications to create a test report.
Refer to the documentation of your CI server application for how to integrate the JUnit report.

An example JUnit XML file is shown below:

.. code-block:: xml

   <?xml version="1.0" ?>
   <testsuite errors="0" hostname="DESKTOP-HV9NHA3" failures="1" timestamp="2022-07-23T04:25:51" tests="1" time="0" name="vhdl-style-guide">
     <properties>
     </properties>
     <testcase name="original.vhd" time="0" classname="failure">
       <failure type="Failure">
         architecture_010: 847 : Add *architecture* keyword.
         concurrent_007: 298 : move code after else to next line.
       </failure>
     </testcase>
     <system-out>
     </system-out>
     <system-err>
     </system-err>
   </testsuite>

Code Quality Report
###################

VSG can generate a quality report of an analysis in JSON format.
The JSON file generated follows a subset of the `Code Climate specification <https://github.com/codeclimate/platform/blob/master/spec/analyzers/SPEC.md#data-types>`_.
The following items in the spec are populated.

.. |description| replace::
   Includes the rule which failed and the proposed solution

.. |fingerprint| replace::
   An MD5 hash to uniquify the error.

.. |severity| replace::
   The severity of the error.  Errors will be reported as :code:`critical`.  Warnings will be reported as :code:`minor`.

.. |location_path| replace::
   A relative path to the file with code quality issues.

.. |location_lines_begin| replace::
   The line number where the code quality issue occured.

+----------------------+------------------------+
| Code Climate Spec    | Description            |
+======================+========================+
| description          | |description|          |
+----------------------+------------------------+
| fingerprint          | |fingerprint|          |
+----------------------+------------------------+
| severity             | |severity|             |
+----------------------+------------------------+
| location.path        | |location_path|        |
+----------------------+------------------------+
| location.lines.begin | |location_lines_begin| |
+----------------------+------------------------+

This report can be used in most CI server applications to create a test report.
Refer to the documentation of your CI server application for how to integrate the Code Quality Report.

An example of a code quality report is shown below:

.. code-block:: json

   [
     {
       "description": "architecture_010 :: Add *architecture* keyword.",
       "fingerprint": "323039ccd1801791163d7a302cfd5b25",
       "severity": "critical",
       "location": {
         "path": "vsg/tests/tool_integration/quality_report/example.vhd",
         "lines": {
           "begin": 8
         }
       }
     }
   ]
