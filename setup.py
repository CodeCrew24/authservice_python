# coding: utf-8

"""
    Auth Service

    This API provides token-based authentication for user registration, login, and client credential management. It ensures secure communication by utilizing tokens for authentication. Users can register with unique usernames and passwords, authenticate using client credentials, retrieve client IDs and secrets, and regenerate client credentials as needed. The API supports various user roles, including 'user', 'admin', 'moderator', 'guest', and 'superadmin'.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301


# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
with open('README.md', 'r') as f:
    DESCRIPTION = f.read()
NAME = "authservice"
VERSION = "0.0.2"
PYTHON_REQUIRES = ">=3.7"
REQUIRES = [
    "urllib3 >= 1.25.3, < 2.1.0",
    "python-dateutil",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]
CLASSIFIERS = [
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',  # Adjusted for developers interested in trying out the beta version
]


setup(
    name=NAME,
    version=VERSION,
    description="With this SDK, Python developers can easily interact with the Auth API, enabling hassle-free implementation of user registration, login, and client credential management features within their applications.",
    author="Code Crew24",
    author_email="dprakash2101@gmail.com",
    url="https://github.com/CodeCrew24/authservice_python",
    keywords=["token based auth", "Bearer Token", "Auth Service"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description=DESCRIPTION,


  # noqa: E501
    package_data={"authservice": ["py.typed"]},
    license='MIT',
    project_urls={
        'GitHub Repo': 'https://github.com/CodeCrew24/authservice_python',
        'Download': 'https://github.com/CodeCrew24/authservice_python/archive/1.0.0.tar.gz',
        'Release Notes': 'https://github.com/CodeCrew24/authservice_python/releases/',
    },
)
