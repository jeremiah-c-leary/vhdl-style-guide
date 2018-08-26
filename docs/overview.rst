Overview
--------

VHDL Style Guide (VSG) provides coding style guide enforcement for VHDL code.

VSG was created after participating in a code review.
A real issue in the code was masked by a coding style issue.
A finding was created for the style issue, while the real issue was missed.
When the code was re-reviewed, the real issue was discovered.

Depending on your process, style issues can take a lot of time to resolve.

1. Create finding/ticket/issue
2. Disposition finding/ticket/issue
3. Fix
4. Verify fix

Spending less time on style issues leaves more time to analyze the substance of the code.
This ultimately reduces the amount of time performing code reviews.
It also allows reviewers to focus on the substance of the code.
This will result in a higher quality code base.

Key Benefits
############

* Define VHDL coding standards
* Makes coding standards visible to everyone
* Improve code reviews
* Quickly bring code up to current standards

VSG allows the style of the code to be defined and enforced over the entire code base.
When this is not desireable, configurations allow for coding standards over different parts of the code base.

Key Features
############

* Command line tool

  * Integrates into continuous integration flow tools

* Reports and fixes issues found

  * Horizontal whitespace
  * Vertical whitespace
  * Upper and lower case
  * Keyword alignments
  * etc...

* Fully configurable rules via JSON configuration file

  * Disable rules
  * Alter behavior of existing rules
  * Change phase of execution

* Localize rule sets

  * Create your own rules using python
  * Use existing rules as a template
  * Fully integrates into base rule set
