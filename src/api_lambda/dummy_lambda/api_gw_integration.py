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


def dummy_lambda_construct(self, identifier: str, function_name: str):
    if not function_name:
        function_name = identifier
    return aws_lambda.Function(self, identifier,
                               function_name=identifier,
                               handler='lambda_handler.handler',
                               runtime=aws_lambda.Runtime.PYTHON_3_7,
                               code=aws_lambda.Code.asset('src/api_lambda/dummy_lambda'),
                               )
