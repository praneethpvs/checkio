#!/usr/bin/env python
# Program that creates and sets up an instance automatically using Pexpect module.

import boto3

ec2 = boto3.resource('ec2')
all_instances = []


def create_instance(*args):
    inst = ec2.create_instances(ImageId=args[0], MinCount=int(args[1]), MaxCount=int(args[2]), KeyName=args[3],
                                InstanceType=args[4])
    return inst


def list_instances():
    for instance in ec2.instances.all():
        all_instances.append(instance.id)
        print instance.id, instance.state


# Terminates the instances based on the instance ID's
def terminate_instance(instance_id):
    instance = ec2.Instance(instance_id)
    response = instance.terminate()
    print response


if __name__ == '__main__':
    # Required inputs for creating instances in AWS.
    ami_id = raw_input("Enter the correct ami id: ")
    min_in = raw_input("Enter the minimum number of instances to be created >= 1: ")
    max_in = raw_input("Enter the minimum number of instances to be created: ")
    key_pair = raw_input("Enter the key pair value: ")
    instance_type = raw_input("Enter the type of instance to be created: ")

    # Creating the instances based on the requirements.
    instances = create_instance(ami_id, min_in, max_in, key_pair, instance_type)
    print "{0} Instance created successfully".format(max_in)

    # Listing all the instances in our region.
    print "All the Instances that are available in your environment..."
    list_instances()
