from aws_cdk import core
from aws_cdk import aws_lambda


def integration_response():
    return [
        {
            'statusCode': '200',
            'responseParameters': {
                'method.response.header.Access-Control-Allow-Origin': "'*'",
            }
        }
    ]


def GET_response():
    return [{
        'statusCode': '200',
        'responseParameters': {
            'method.response.header.Access-Control-Allow-Origin': True,
        }
    }
    ]


class LambdaStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.cdk_function = aws_lambda.Function(self, id,
                                                handler='lambda_handler.handler',
                                                runtime=aws_lambda.Runtime.PYTHON_3_7,
                                                code=aws_lambda.Code.asset('src/api_lambda/dummy_lambda'),
                                                )
