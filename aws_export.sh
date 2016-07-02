#!/bin/bash

# Hastily written by Woodland Hunter in 2015 for his own use.
# AWS credentials sit in plaintext normally, so this
# isn't much different...
#
# 1) move to $HOME/.aws_export.sh
# 2) then in .bash_profile add this:
#
# alias aws_export='. $HOME/.aws_export.sh'
# aws_export dev
#
# 3) then add AWS_ACCOUNT in your prompt, something like
#
# export PS1='\[\033[0;34m\][${AWS_ACCOUNT}] \[\033[0;32m\]\h\[\033[0;33m\] \w\[\033[00m\]: '

case $1 in
  dev)
    export AWS_ACCOUNT="dev"
    export AWS_ACCESS_KEY_ID="youridhere"
    export AWS_SECRET_ACCESS_KEY="yourkeyhere"
  ;;
  prod)
    export AWS_ACCOUNT="prod"
    export AWS_ACCESS_KEY_ID="youridhere"
    export AWS_SECRET_ACCESS_KEY="yourkeyhere"
  ;;
  *)
    echo "usage: $0 valid_account region"
  ;;
esac

if [[ -z $2 ]];then
  region=us-west-2
else
  region=$2
fi

export AWS_REGION=${region}
export AWS_DEFAULT_REGION=${region}

# Hashicorp Terraform
# this allows you to set your aws.tf provider like so:
#
# variable "aws_access_key" {} #env variable
# variable "aws_secret_key" {} # env variable
# variable "aws_region" {} #env variable
# provider "aws" {
#     access_key = "${var.aws_access_key}"
#     secret_key = "${var.aws_secret_key}"
#     region = "${var.aws_region}"
# }

export TF_VAR_aws_access_key=${AWS_ACCESS_KEY_ID}
export TF_VAR_aws_secret_key=${AWS_SECRET_ACCESS_KEY}
export TF_VAR_aws_region=${AWS_REGION}

