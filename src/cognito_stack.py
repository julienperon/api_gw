from aws_cdk import core
from aws_cdk import aws_cognito


class CognitoStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        user_pool = aws_cognito.UserPool(self, "UserPool",
                                         user_pool_name="Myawesomeapp-userpool",
                                         self_sign_up_enabled=False)
        # pool_id = user_pool.user_pool_id

        api_client = user_pool.add_client("customer-app-client")
        client_id = api_client.user_pool_client_id

        cognito_idp = aws_cognito.CfnIdentityPool(self, "IdentityPool",
                                                  identity_pool_name="Myawesomeapp-idp",
                                                  allow_unauthenticated_identities=False)
        cognito_idp.CognitoIdentityProviderProperty(client_id=client_id)
