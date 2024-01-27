import aws_cdk as core
import aws_cdk.assertions as assertions

from dir.dir_stack import DirStack


# example tests. To run these tests, uncomment this file along with the example
# resource in dir/dir_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = DirStack(app, "dir")
    template = assertions.Template.from_stack(stack)


#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
