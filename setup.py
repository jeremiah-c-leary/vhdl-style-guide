from setuptools import setup
from setuptools import find_packages

### Implement Version information
import os

from vsg import version

sVersionInfoFileName = os.path.join('vsg', 'version_info.py')

if not os.path.exists(sVersionInfoFileName):

    sVersion, sShaNum = version.get_version_info(version.sVersion, None)

    lVersionInfo = []
    lVersionInfo.append('sVersion = \'' + str(sVersion) + "'")
    lVersionInfo.append('sShaNum = \'' + str(sShaNum) + "'")

    with open(sVersionInfoFileName, 'w') as oFile:
        for sLine in lVersionInfo:
            oFile.write(sLine + '\n')
    oFile.close()

    sInstallVersion = sVersion
    bRemoveVersionFile = True

else:

    from vsg import version_info

    try:
        sInstallVersion = version_info.sVersion
    except AttributeError:
        sInstallVersion = version.sVersion

    bRemoveVersionFile = False

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
  name='vsg',
  version=str(sInstallVersion),
  description='VHDL Style Guide',
  long_description=readme(),
  classifiers=[
      'Development Status :: 4 - Beta',
      'Environment :: Console',
      'Programming Language :: Python :: 3',
      'Intended Audience :: End Users/Desktop',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Natural Language :: English',
      'Operating System :: POSIX :: Linux',
      'Topic :: Software Development :: Quality Assurance',
      'Topic :: Text Processing :: General',
  ],
  url='https://github.com/jeremiah-c-leary/vhdl-style-guide',
  download_url='https://github.com/jeremiah-c-leary/vhdl-style-guide',
  author='Jeremiah C Leary',
  author_email='jeremiah.c.leary@gmail.com',
  license='GNU General Public License',
  packages=find_packages(),
  zip_safe=False,
  include_package_data=True,
  test_suite='nose.collector',
  tests_require=['nose'],
  keywords=['vhdl', 'style', 'beautify', 'guide', 'lint'],
  install_requires=[
    'PyYAML>=5.1'
  ],
  python_requires='>=3.5',
  entry_points={
    'console_scripts': [
      'vsg = vsg.__main__:main'
    ]
  }
)

### Cleanup version information
if bRemoveVersionFile:
    os.remove(sVersionInfoFileName)
