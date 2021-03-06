.. _docid.steps.veripy.steps.forms.actions.enter_text_into_field:
.. index:: veripy.steps.forms.actions.enter_text_into_field

======================================================================
veripy.steps.forms.actions.enter_text_into_field
======================================================================

:Module:   veripy.steps.forms.actions.enter_text_into_field
:Filename: veripy/steps/forms/actions/enter_text_into_field.py

Step Overview
=============


=================================================== ===== ==== ==== ====
Step Definition                                     Given When Then Step
=================================================== ===== ==== ==== ====
Given "{text}" is entered into the "{element_name}"   x                 
When "{text}" is entered into the "{element_name}"          x           
=================================================== ===== ==== ==== ====

Step Definitions
================

.. index:: 
    single: Given step; Given "{text}" is entered into the "{element_name}"

.. _given "{text}" is entered into the "{element_name}":

**Step:** Given "{text}" is entered into the "{element_name}"
-------------------------------------------------------------

Tells the browser to enter the given test into an element with
the given identifier.

::

    Given "query text" is entered into the "Search Box"
    # or
    When "query text" is entered into the "Search Box"

.. index:: 
    single: When step; When "{text}" is entered into the "{element_name}"

.. _when "{text}" is entered into the "{element_name}":

**Step:** When "{text}" is entered into the "{element_name}"
------------------------------------------------------------

Tells the browser to enter the given test into an element with
the given identifier.

::

    Given "query text" is entered into the "Search Box"
    # or
    When "query text" is entered into the "Search Box"

