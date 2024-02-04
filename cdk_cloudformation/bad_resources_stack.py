from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_s3 as s3,
    aws_iam as iam,
    aws_apigatewayv2 as apigateway,
)
from constructs import Construct


class BadResourcesStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        default_vpc = ec2.Vpc.from_lookup(self, "VPC", is_default=True)
        apigateway.CfnStage(
            self,
            "rHttpApiDefaultStage",
            api_id="foo",
            stage_name="$default",
            auto_deploy=True,
        )
        
        # S3 Bucket
        s3.Bucket(self, "TheS3Bucket", bucket_name="test-s3-bucket")

        # IAM Role
        role = iam.Role(
            self,
            "InstanceRole",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AdministratorPolicy")
            ],
        )

        # EC2 Security Group
        security_group = ec2.SecurityGroup(
            self,
            "SecurityGroup",
            vpc=default_vpc,
            allow_all_outbound=True,
            security_group_name="dev-test-sg",
        )
        security_group.add_ingress_rule(
            ec2.Peer.ipv4("0.0.0.0/0"), ec2.Port.all_tcp(), "Allow ALL Inbound Access"
        )

        # Example EC2 Instance
        a_simple_ec2_instance = ec2.Instance(
            self,
            "MyInstance",
            instance_name="dev-test-instance",
            vpc=default_vpc,
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO
            ),
            machine_image=ec2.GenericLinuxImage({"us-east-1": "ami-0fc61db8544a617ed"}),
            security_group=security_group,
            role=role,
        )
