Tool Integration
----------------

VSG supports integration with other tools via several command line options.

+-------------------------------+-------------------------------------------------+
| --all-phases                  | Executes all phases without stopping if a       |
|                               | violation is found.                             |
+-------------------------------+-------------------------------------------------+

--all-phases
############

VSG has a concept of phases, where violations in one phase should be addressed before moving to the next phase.
The **--all-phases** option will run an analysis over all the phases.
It will not stop if a violation has occured.

This option can be useful when integrating VSG into an editor that supports linters.
It is important to note there are dependencies between some rules.
If violations for a later phase are fixed before violations on an earlier phase, it could lead to reoccurances of violations until the correct order is followed.

