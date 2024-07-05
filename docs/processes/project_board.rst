Project Board
-------------

Issues and pull requests are managed on a `GitHub project board <https://github.com/users/jeremiah-c-leary/projects/3>`_:

Issues can be tracked from when they are created, through development, validation and release.

Issue flow chart
================

Issue progress is tracked using the Status attribute.
The transition from one state to another is governed by the table below.

+-----------------+-----------------+---------------------------------------------------------------------------------------+
| Status          | Next status     | Reason                                                                                |
+=================+=================+=======================================================================================+
| None            | Triaged         | A solution can be developed.                                                          |
|                 +-----------------+---------------------------------------------------------------------------------------+
|                 | User Feedback   | More information is required from the user before development can continue.           |
|                 +-----------------+---------------------------------------------------------------------------------------+
|                 | Deferred        | Issue will not be developed in current major release.                                 |
+-----------------+-----------------+---------------------------------------------------------------------------------------+
| Triaged         | In Progress     | Issue can be developed without user feedback.                                         |
|                 +-----------------+---------------------------------------------------------------------------------------+
|                 | User Feedback   | More information is required from the issue creator before development can continue.  |
+-----------------+-----------------+---------------------------------------------------------------------------------------+
| User Feedback   | Triaged         | Sufficient clarification has been received and the issue can continue development.    |
|                 +-----------------+---------------------------------------------------------------------------------------+
|                 | In Progress     | Sufficient clarification has been received and the issue can continue development.    |
|                 +-----------------+---------------------------------------------------------------------------------------+
|                 | Closed          | Issue can be resolved without any new development.                                    |
|                 +-----------------+---------------------------------------------------------------------------------------+
|                 | Deferred        | Issue will not be developed in current major release.                                 |
+-----------------+-----------------+---------------------------------------------------------------------------------------+
| User Validation | In Progress     | Additional development is required to meet user needs.                                |
|                 +-----------------+---------------------------------------------------------------------------------------+
|                 | Closed          | Issue has been resolved and is ready for release.                                     |
+-----------------+-----------------+---------------------------------------------------------------------------------------+
| In Progress     | User Feedback   | More information is required from the user before development can continue.           |
|                 +-----------------+---------------------------------------------------------------------------------------+
|                 | User Validation | A solution has been developed for the user and requires validation.                   |
+-----------------+-----------------+---------------------------------------------------------------------------------------+

The project board is divided into 7 views: Issue Triage, Development, Bugs, Next Release, Releases, Deferred, and Version 4.0.

Issue Triage
============

There is a GitHub action which will add any newly created issue into the project board.
This view provides an easy way to check for new issues.

Development
===========

This view manages the active issues through the issue flow chart given above.

Bugs
====

This view shows all bugs and where they are in the process.
It provides a quick look into the status of all bugs.

.. jcl - include picture of view

Next Release
============

This view contains issues and pull requests which have been closed and are ready to be published in the next release.
It provides a concise view for creating release notes.

When a release occurs, the Schedule Release column is updated with the release number.
This will move the issue from this view and into the Releases view.

Releases
========

This view shows which issues have been addressed with a particular release.
Each release provides a collapsible view containing each issue in a release.

Deferred
========

This view shows all issues which have been deferred.
Deferred issues will either be developed later or eventually retired and then closed.

Version 4.0
===========

This view provides a list of all issues which would be candidates when a major rewrite occurs.
This could be due to limitations in parsing or the underlying data structure.
