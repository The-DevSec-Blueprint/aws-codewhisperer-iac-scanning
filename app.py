#!/usr/bin/env python3
import os

import aws_cdk as cdk
from cdk_cloudformation.bad_resources_stack import BadResourcesStack
from cdk_cloudformation.secure_resources_stack import SecureResourcesStack

app = cdk.App()
BadResourcesStack(
    app,
    "BadResourcesStack",
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION")
    ),
)
SecureResourcesStack(
    app,
    "SecureResourcesStack",
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION")
    ),
)
app.synth()
