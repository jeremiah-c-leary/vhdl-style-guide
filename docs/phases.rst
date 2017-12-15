
Phases
------

The rules are grouped together and ran in phases.
If issues are found during a phase, then successive phases will not execute.

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

This phase checks all vertical spacing requirements are met.

Phase 4 - Indentation
#####################

This phase checks all indentation rules

Phase 5 - Alignment
###################

This phase checks all alignment rules

Phase 6 - Capitalization
########################

This phase checks capitalization rules

Phase 7 - Naming conventions
############################

This phase checks naming restrictions for signals, constants, ports, etc...

