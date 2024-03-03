# coding: utf-8

"""
    Auth Service

    This API provides token-based authentication for user registration, login, and client credential management. It ensures secure communication by utilizing tokens for authentication. Users can register with unique usernames and passwords, authenticate using client credentials, retrieve client IDs and secrets, and regenerate client credentials as needed. The API supports various user roles, including 'user', 'admin', 'moderator', 'guest', and 'superadmin'.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from authservice.models.register_post400_response import RegisterPost400Response

class TestRegisterPost400Response(unittest.TestCase):
    """RegisterPost400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RegisterPost400Response:
        """Test RegisterPost400Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RegisterPost400Response`
        """
        model = RegisterPost400Response()
        if include_optional:
            return RegisterPost400Response(
                message = 'Username is already taken'
            )
        else:
            return RegisterPost400Response(
        )
        """

    def testRegisterPost400Response(self):
        """Test RegisterPost400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()