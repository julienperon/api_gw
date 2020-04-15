#!/usr/bin/env python3

from aws_cdk import core

from src.cognito_stack import CognitoStack
from src.api_gw_stack import ApiGatewayStack


app = core.App()
CognitoStack(app, "CognitoStack", env=core.Environment(region="eu-west-1"))
ApiGatewayStack(app, "ApiGatewayStack", env=core.Environment(region="eu-west-1"))

app.synth()
