Continuous Integration Servers
------------------------------

VSG supports integration with continuous integration severs such as Bamboo and GitLab.
Support is provided using one of the following command line arguments.

+----------+-------------------------------+-------------------------------------------------+
| CI Sever | Command Line Option           | Comment                                         |
+----------+-------------------------------+-------------------------------------------------+
| Bamboo   | :code:`--junit`               | Extract JUnit file.                             |
+----------+-------------------------------+-------------------------------------------------+
| GitLab   | :code:`--quality_report`      | Create code quality report for GitLab.          |
+----------+-------------------------------+-------------------------------------------------+

Bamboo
######

Bamboo supports error reporting using a JUnit XML file.
Use the :code:`--junit` command line option when executing VSG from Bamboo.
VSG will generate a JUnit XML file that will contain information about the run.
This will include any failures encountered.

Information on using JUnit files with Bamboo can be found on `Atlassian's website <https://confluence.atlassian.com/bamboo/junit-parser-289277056.html>`_.

GitLab
######

GitLab supports error reporting using a JSON file.
Use the :code:`--junit` command line option when executing VSG from GitLab.
VSG will generate a JSON file that will contain information about the run.
This will include the any failures encountered.

Information on enabling code quality reports can be found on `GitLab's website <https://docs.gitlab.com/ee/ci/testing/code_quality.html>`_.

Other CI Servers
################

Support for other CI servers is dependent on their support for either JUnit XML files or the JSON format file provided by the above options.
Check the documentation of the CI server to determine which option would work.
