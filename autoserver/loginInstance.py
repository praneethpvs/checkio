#!/usr/bin/env python

def login_instance(u_name, instance_ip, key_pair_path):
    try:
        username = u_name
        hostname = instance_ip
        ssh_key = key_pair_path
        s.login(hostname, username, ssh_key)
        s.sendline('ls -l')  # run a command
        s.prompt()  # match the prompt
        print(s.before)
    except pxssh.ExceptionPxssh as e:
        print("pxssh failed on login.")
        print(e)


print "\nEnter the username and the kep-pair path of the launched instances."
user_name = raw_input("Enter the username of the instance: ")
kp_path = raw_input("Enter the location of the key-pair folder: ")

# Checking the status of the instances once they are created.
# If they are in running state then we login to the Instance.
for i in range(len(created_instances_id)):
    if not check_instance_status(created_instances_id[i]):
        print "\nThe Instance created is in pending state:"
        sleep(360)
        goto(99)
    else:
        temp_inst = instance_info(created_instances_id[i])
        inst_ip = temp_inst.public_ip_address
        login_instance(user_name, inst_ip, kp_path)
