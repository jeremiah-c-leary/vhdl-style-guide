
Phases
------

Rules are grouped together and executed in phases.
If issues are found during a phase, then successive phases will not run.
The phases are constructed to model the proper order of fixing issues.
Each phase prepares the code for the next phase.

Phase 1 - Structural
####################

This phase checks the structure of VHDL statements.
This ensures the VHDL is structured properly for future phases.

Phase 2 - Whitespace
####################

This phase checks whitespace rules.
However, this does not include indentation.

Phase 3 - Vertical Spacing
##########################

This phase checks all vertical spacing requirements.

Phase 4 - Indentation
#####################

This phase checks all indentation rules.

Phase 5 - Alignment
###################

This phase checks all alignment rules.

Phase 6 - Capitalization
########################

This phase checks capitalization rules.

Phase 7 - Naming conventions
############################

This phase checks naming conventions for signals, constants, ports, etc...

