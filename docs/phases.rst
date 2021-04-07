.. include:: icons.rst

Phases
======

Rules are grouped together and executed in phases.
This simplifies rule generation for rules in later phases.
If issues are found during a phase, then successive phases will not be run.
The phases are constructed to model the proper order of fixing issues.
Each phase prepares the code for the next phase.

Which phase a rule is executed in is indicated by one of these phase labels:

|phase_1| |phase_2| |phase_3| |phase_4| |phase_5| |phase_6| |phase_7|

Phase |phase_1| - Structural
-------------------------------

This ensures the VHDL is structured properly for future phases.

It includes the following operations:

* Addition or removal of optional VHDL elements
* Addition or carriage returns to split lines
* Removal of carriage returns to combine lines

Phase |phase_2| - Whitespace
--------------------------------

This phase checks whitespace rules.

It includes the following operations:

* Addition of whitespace between VHDL elements
* Reduction of whitespace between VHDL elements

Phase |phase_3| - Vertical Spacing
--------------------------------------

This phase checks vertical spacing between lines.

It includes the following operations:

* Addition of carriage returns to emphasize VHDL elements
* Removal of carriage returns to deemphasize VHDL elements

Phase |phase_4| - Indentation
----------------------------------

This phase checks the indent of lines.

Phase |phase_5| - Alignment
-------------------------------

This phase checks VHDL elements are column aligned.

It includes the following operations:

* Alignment of colons
* Alignment of assignment operators
* Alignment of identifiers

Phase |phase_6| - Capitalization
------------------------------------

This phase checks case of VHDL elements.

It includes the following operations:

* Case of VHDL keywords
* Case of identifiers

Phase |phase_7| - Naming conventions
----------------------------------------

This phase checks naming conventions for non VHDL keywords.

It includes the following operations:

* Signal prefixes
* Port prefixes and suffixes
* Architecture identifiers

Subphases
---------

Each phase can have multiple subphases.
There are rules which are executed within the same phase, but one is dependent on another.
Utilizing a subphase allows for the proper execution of the rules.

Subphase 1
##########

Prepare code for rules in subphase 2.

Subphase 2
##########

Execute on code prepared in subphase 1.
