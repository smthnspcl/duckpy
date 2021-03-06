from setuptools import setup, find_packages

setup(
    long_description_content_type="text/markdown",
    long_description=open("readme.md", "r").read(),
    name="duckpy",
    version="0.42",
    description="query the duckduckgo lite engine",
    author="Pascal Eberlein",
    author_email="pascal@eberlein.io",
    url="https://github.com/smthnspcl/duckpy",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    keywords="duckduckgo python search query",
    packages=find_packages(),
    install_requires=open("requirements.txt").readlines(),
    entry_points={'console_scripts': ['duckpy = duckpy.__main__:main']}
)
