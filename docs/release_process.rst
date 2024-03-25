
Current Method
==============

Follow these steps:


1)  Update release_notes.txt

2)  Tag with the following command

       git tag <release_number> -F release_notes.txt

3)  Push tag to origin

       git push --tags origin master

4)  Download wheel from CI action

5)  Submit to PyPI

       twine upload dist/*
