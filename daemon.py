import os
import subprocess
import time
from config import db


current_command = False
current_pid = False
commands = []

while True:
    if not current_pid:
        with open(db, 'r') as my_file:
            commands = my_file.readlines()
            if commands:
                command = commands[0].strip('\n')
                current_command = command
                my_process = subprocess.Popen('{cmd}'.format(cmd=current_command), shell=True)
                current_pid = my_process.pid
    else:
        poll = my_process.poll()
        if poll == None:
	    pass
            #print('Still Executing "{} : {}"'.format(current_command, current_pid))
        else:
            #print('End detected')
            current_pid = False
            current_command = False
	    with open(db, 'r') as my_file:
	        commands = my_file.readlines()
            with open(db, 'w') as my_file:
                firstLine = True
                for my_command in commands:
                    if firstLine:
                        firstLine = False
                    else:
                        my_file.write(my_command)
    time.sleep(5)
