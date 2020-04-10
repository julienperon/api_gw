#!/usr/bin/env python3

from aws_cdk import core

from src.api_gw_stack import ApiGatewayStack


app = core.App()
ApiGatewayStack(app, "src")

app.synth()
