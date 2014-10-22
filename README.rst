=========================
ploneintranet.attachments
=========================

Attachment storage for the Plone intranet suite

* `Source code @ GitHub <https://github.com/ploneintranet/ploneintranet.attachments>`_
* `Releases @ PyPI <http://pypi.python.org/pypi/ploneintranet.attachments>`_
* `Documentation @ ReadTheDocs <http://ploneintranetattachments.readthedocs.org>`_
* `Continuous Integration @ Travis-CI <http://travis-ci.org/ploneintranet/ploneintranet.attachments>`_

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

