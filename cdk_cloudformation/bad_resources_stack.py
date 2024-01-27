from aws_cdk import Stack, aws_ec2 as ec2, aws_s3 as s3
from constructs import Construct


class BadResourcesStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Example EC2 Instance
        default_vpc = ec2.Vpc.from_lookup(self, "VPC", is_default=True)
        a_simple_ec2_instance = ec2.Instance(
            self,
            "MyInstance",
            instance_name="dev-test-instance",
            vpc=default_vpc,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            ),
            machine_image=ec2.GenericLinuxImage({"us-east-1": "ami-0fc61db8544a617ed"}),
        )
