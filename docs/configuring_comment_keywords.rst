
.. _configuring-comment-keywords:

Configuring Comment Keywords
----------------------------

Comments serve as a mode of communication between designers.
They can be used to clarify code and communicate tasks.

Common task based comments include instructions for missing features or issues which must be addressed.
The keywords TODO and FIXME are typically used to communicate these to other designers.

The list of keywords searched for can be configured using the code:`keyword` option.

.. code-block:: yaml

    rule :
        comment_012:
            disable: false
            keywords: ['TODO', 'FIXME', 'ATTENTION']

Rules Enforcing Comment Keywords
################################

* `comment_012 <comment_rules.html#comment-012>`_
