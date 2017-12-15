Overview
--------

After recently performing code reviews, most of the issues found were related to style.
Time spent in code reviews addressing style issues is a waste.
Depending on your process, style issues can take a lot of time to resolve.

1. Create finding/ticket/issue
2. Disposition
3. Fix
4. Verify fix

Spending less time on style issues leaves more time to analyze the substance of the code.
Ultimately, this will reduce the amount of time performing code reviews.
Spending more time on substance than style will result in higher quality code that costs less.

Key Benefits
############

* Define VHDL coding standards
* Makes coding standards visible to everyone
* Improve code reviews
* Quickly bring code up to current standards

VSG allows the style of the code to be defined and enforced over part or the entire code base.
Configurations allow for multiple coding standards.

Key Features
############

* Command line tool

  * integrate into continuous integration flow

* Fixes and/or reports issues found

  * horizontal whitespace
  * vertical whitespace
  * upper and lower case
  * keyword alignments
  * etc...

* Fully configurable rules via JSON configuration file

  * Disable rules
  * Alter behavior of existing rules
  * Change phase of execution

* Localize rule sets

  * Create your own rules using python
  * Use existing rules as a template
  * Fully integrates into base rule set

