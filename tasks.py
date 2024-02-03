from invoke import task
from subprocess import run, PIPE

# This Version aligns with aws-cdk-lib in the requirements.txt.
CDK_VERSION = "npx --yes cdk@2.55.1"


@task
def synth(c, stack_name: str = None):
    """
    Synthesize the CDK stacks and dumps
    the resources into their respective files.

    :param c: The Invoke context.
    :param stack_name: The name of the stack to synthesize.
    :return: None.
    """
    if stack_name is None:
        for stack_name in _obtain_list_of_stacks():
            c.run(f"{CDK_VERSION} synth {stack_name} > ./synth_stacks/{stack_name}.yml")
    else:
        c.run(f"{CDK_VERSION} synth {stack_name} > ./synth_stacks/{stack_name}.yml")


def _obtain_list_of_stacks():
    """
    Obtain a list of all CDK stacks.

    :return: A list of all CDK stacks.
    """
    command = CDK_VERSION.split(" ")
    command.append("list")
    result = run(command, capture_output=True, text=True, check=True)

    stacks = result.stdout.split("\n")
    stacks.remove("")

    return stacks
