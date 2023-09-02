#!/usr/bin/env python3
import aws_cdk as core
from cdk_workshop.cdk_workshop_stack import CdkWorkshopStack

app = core.App()

environment_type = app.node.try_get_context("environmentType")
environment_context = app.node.try_get_context(environment_type)
region = environment_context["region"]
account = app.node.try_get_context("account")
tags = environment_context["tags"]
stack_name = f'{app.node.try_get_context("prefix")}-{environment_type}'

class MyStack(core.Stack):
    def __init__(self, scope, id, **kwargs):
        super().__init__(scope, id, **kwargs)

CdkWorkshopStack(
    app,
    stack_name,
     env=core.Environment(
        account=account,
        region=region
    ),
    tags=tags,
)

app.synth()

