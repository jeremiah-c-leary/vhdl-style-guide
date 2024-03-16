
Current Method
==============

Follow these steps:

1)  Update vsg/version.py with release version

2)  Commit file with message "Preparing for release <release_number>"

3)  Update release_notes.txt

4)  Tag with the following command

       git tag <release_number> -F release_notes.txt

5)  Push tag to origin

       git push --tags origin master

6)  Update vsg/version_info.py

       Update sVersion with <release_number>
       Update sShaNum with sha number from tag

7)  Submit to PyPI

       python setup.py sdist upload -r pypi

.. Reference Method
.. ================
..
.. The download_url is a link to a hosted file with your repository's code.
.. Github will host this for you, but only if you create a git tag.
.. In your repository, type:
..
..  git tag 0.1 -m "Adds a tag so that we can put this on PyPI.".
..
.. jcl - update the release_notes.txt file
.. jcl - use this instead:  git -tag <revision_number> -F release_notes.txt
..
.. Then, type git tag to show a list of tags — you should see 0.1 in the list. Type
..
..  git push --tags origin master
..
.. jcl - update sVersion in vsg/version_info.py
.. jcl - do not forget to update the version_info.py with the sha number of the tag.
.. jcl - grab the sha number from the tags page
..
.. to update your code on Github with the latest tag information.
..
.. Github creates tarballs for download at https://github.com/{username}/{module_name}/archive/{tag}.tar
..
.. To submit to PyPI:
..
.. python setup.py sdist upload -r pypi
