=========================
ploneintranet.attachments
=========================

Attachment storage for the Plone intranet suite

* `Source code @ GitHub <https://github.com/ploneintranet/ploneintranet.attachments>`_
* `Releases @ PyPI <http://pypi.python.org/pypi/ploneintranet.attachments>`_
* `Documentation @ ReadTheDocs <http://ploneintranetattachments.readthedocs.org>`_

Build status
------------

Notification tests
~~~~~~~~~~~~~~~~~~

.. image:: http://jenkins.ploneintranet.net/buildStatus/icon?job=Plone%20Intranet%20Attachments
    :target: http://jenkins.ploneintranet.net/job/Plone%20Intranet%20Attachments/

Robot tests for Plone Intranet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: http://jenkins.ploneintranet.net/buildStatus/icon?job=Plone%20Intranet%20Suite%20Master
    :target: http://jenkins.ploneintranet.net/job/Plone%20Intranet%20Suite%20Master/badge/



How it works
============

Make a content type support attachments by having it implement
IAttachmentStoragable. The provided adapter is used to add and retrieve values:

>>> storage = IAttachmentStorage(obj)
>>> storage.add('test.doc', attachment_obj)
>>> retrieved = storage.get('test.doc')

To list the ids of available attachments:

>>> storage.keys()

To delete an attachment:

>>> storage.remove('test.doc')

Attachments can be accessed ttw using the ++attachments++ namespace
(/path/to/object/++attachments++default/test.doc).


Installation
============

To install `ploneintranet.attachments` you simply add ``ploneintranet.attachments``
to the list of eggs in your buildout, run buildout and restart Plone.
Then, install `ploneintranet.attachments` using the Add-ons control panel.


Copyright (c) Plone Foundation
------------------------------

This package is Copyright (c) Plone Foundation.

Any contribution to this package implies consent and intent to irrevocably transfer all 
copyrights on the code you contribute, to the `Plone Foundation`_, 
under the condition that the code remains under a `OSI-approved license`_.

To contribute, you need to have signed a Plone Foundation `contributor agreement`_.
If you're `listed on Github`_ as a member of the Plone organization, you already signed.

.. _Plone Foundation: https://plone.org/foundation
.. _OSI-approved license: http://opensource.org/licenses
.. _contributor agreement: https://plone.org/foundation/contributors-agreement
.. _listed on Github: https://github.com/orgs/plone/people
