#!/usr/bin/env python
# Program that creates and sets up an instance automatically using Pexpect module.

import boto3
from pexpect import pxssh

ec2 = boto3.resource('ec2')
all_instances = {}
run = {}
created_instances_id = []
s = pxssh.pxssh()


def create_instance(*args):
    inst = ec2.create_instances(ImageId=args[0], MinCount=int(args[1]), MaxCount=int(args[2]), KeyName=args[3],
                                InstanceType=args[4])
    return inst


def list_instances():
    for instance in ec2.instances.all():
        all_instances[instance.id] = instance.id
        print all_instances[instance.id], instance.state


# Terminates the instances based on the instance ID
def terminate_instance(instance_id):
    instance = ec2.Instance(instance_id)
    response = instance.terminate()
    print response


def instance_info(instance_id):
    instance = ec2.Instance(instance_id)
    all_instances[instance_id] = {
        'state': instance.state,
        'public_ip': instance.public_ip_address
    }

    return all_instances[instance_id]


def check_instance_status(instance_id):
    if ec2.Instance(instance_id).state == 'running':
        run[created_instances_id[i]] = 'True'
        return True
    else:
        run[created_instances_id[i]] = 'False'
        return False


if __name__ == '__main__':
    # Required inputs for creating instances in AWS.
    ami_id = raw_input("Enter the correct ami id: ")
    min_in = raw_input("Enter the minimum number of instances to be created >= 1: ")
    max_in = raw_input("Enter the minimum number of instances to be created: ")
    key_pair = raw_input("Enter the key pair value: ")
    instance_type = raw_input("Enter the type of instance to be created: ")

    # Creating the instances based on the requirements.
    instances = create_instance(ami_id, min_in, max_in, key_pair, instance_type)
    print "\nThe following {0} instances have been created successfully: ".format(max_in)
    for inst in instances:
        created_instances_id.append(inst.id)
    for i in range(len(created_instances_id)):
        print "instance Id {0} = {1}".format(i + 1, created_instances_id[i])

    # Listing all the instances in our region.
    print "\nAll the Instances that are available in your environment..."
    list_instances()
