import os
import subprocess

wd = os.getcwd()

if __name__ == '__main__':

    while True:
        user_input = input("runner-cli: ").split(' ')  # '*package_name* *yarn command* example: 'accounts build'
        command = 'cd ./' + user_input[0] + ' && yarn run ' + user_input[1]
        print(command)
        result = subprocess.run(command,
                                stdout=subprocess.PIPE, cwd=wd,
                                shell=True)
        print(result.stdout.decode('utf-8'))
