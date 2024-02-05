# Shifting Left with AI: Catching Vulnerabilities Early using AWS CodeWhisperer and VSCode

[![Thumbnail](./docs/images/thumbnail_shiftleft.svg)](https://youtu.be/riFlzaq8PKcA)

## Getting Started (Prerequsities)

1. Make sure you have NPM/Node.js installed! You can install it by going to clicking [here](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).
1. Make sure you have Python installed! You can install it by going to clicking [here](https://www.python.org/downloads/).
1. Create a Virtual Environment in Python!
```sh
$ python -m venv .env
```
1. Source your Virtual Environment & Install Packages!
```sh
$ source .env/bin/activate
$ pip install -r requirements.txt
```

## Generating Stacks For Scanning

Luckily, I've taken the liberty of installing invoke for our `little` project. The invoke commands are basically wrappers around the AWS CDK CLI commands to either synthesize or deploy our stacks. If you're looking to create the cdk stacks for scanning with CodeWhisperer, you'll want to enter the following commands below:

```sh
inv synth
```
>**NOTE**: Pass in --stack-name to specify the stack that you want.
