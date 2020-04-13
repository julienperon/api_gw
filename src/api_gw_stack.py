from aws_cdk import core
from aws_cdk import aws_apigateway as apigw
from aws_cdk import aws_lambda
from src.api_lambda import api_gw_integration


class ApiGatewayStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # API GW lambdas first:
        dummy_lambda = aws_lambda.Function(self, id,
                                           function_name='dummy_lambda',
                                           handler='lambda_handler.handler',
                                           runtime=aws_lambda.Runtime.PYTHON_3_7,
                                           code=aws_lambda.Code.asset('src/api_lambda/dummy_lambda'),
                                           )

        # API Gateway
        base_api = apigw.RestApi(self, 'ApiGatewayWithCors')

        # Lambda Integration
        dummy_entity = base_api.root.add_resource('dummy')
        dummy_lambda_integration = apigw.LambdaIntegration(dummy_lambda,
                                                           proxy=False,
                                                           integration_responses=api_gw_integration.integration_response())

        dummy_entity.add_method('GET',
                                dummy_lambda_integration,
                                method_responses=api_gw_integration.GET_response()
                                )
