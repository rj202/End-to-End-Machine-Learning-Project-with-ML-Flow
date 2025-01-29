import setuptools #setuptools is a Python library used for packaging Python projects and managing distribution.

with open('README.md','r',encoding='utf-8') as f:
    long_description = f.read()


__version__='0.0.0'

REPO_NAME='End-to-End-Machine-Learning-Project-with-ML-Flow'
AUTHOR_USER_NAME='j'
SRC_REPO = 'mlproject'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description='A small python package for ml app',
    long_description='text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        'Bug Tracker': f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues',
    },
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src')
)
