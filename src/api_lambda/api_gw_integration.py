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
