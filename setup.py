from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="turbostich",
    version="0.0.1",
    author="TurBoss",
    author_email="<j.l.toledano.l@gmail.com>",
    description="turbostich - Embroider Virtual Control Panel for LinuxCNC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TurBoss/TurBoStich",
    download_url="https://github.com/TurBoss/TurBoStich/tarball/master",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'gui_scripts': [
            'turbostich=turbostich:main',
        ],
        'qtpyvcp.vcp': [
            'turbostich=turbostich',
        ],
    },
)
