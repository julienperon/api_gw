#!/usr/bin/env python3

from aws_cdk import core

from src.api_gw_stack import ApiGatewayStack


app = core.App()
ApiGatewayStack(app, "ApiGatewayStack", env=core.Environment(region="eu-west-1"))

app.synth()
