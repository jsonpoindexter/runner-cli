import os
import subprocess
import cmd
import json


# Run from root dir of project
# Can execute any packages/packageName scripts from package.json
#   To do tab completion for packages just use the package name. ie: accounts

working_directory = os.getcwd()

print("Working directory: ", working_directory)


# Assume we are in root of project. Project dir:
# root/
# ├─ packages/
# │  ├─ authentication/
# │  │  ├─ package.json
# │  ├─ accounts/
# │  │  ├─ package.json
# Iterate packages/packageName/package.json, parse scripts section and add to dictionary.
# Output:
# {
#   'accounts': {'test': 'echo "You ran Accounts TEST"'},
#   'authentication': {'test': 'echo "You ran Authentication TEST"'}
# }
def parse_package_scripts():
    package_scripts = {}
    if os.path.exists('./packages'):
        os.chdir(working_directory + '/packages')
        packages = [d for d in os.listdir('.') if os.path.isdir(d)]
        print("Found packages: ", ", ".join(packages))
        for package in packages:
            package_json_path = f'./{package}/package.json'
            if not os.path.isfile(package_json_path):
                print(f'[INFO] {package_json_path} does not exist')
                continue
            package_json_data  = json.load(open(package_json_path))
            package_scripts[package] = package_json_data["scripts"]
        return package_scripts
    else:
        raise Exception("Tool needs to be run in directory where 'packages' as a direct sub-directory")

class RunnerCli(cmd.Cmd):
    prompt = 'runner-cli: '
    def preloop(self):
        self.do_help("")


def main():
    scripts_dict = parse_package_scripts()

    # print(scripts_dict)
    for package_name, package_scripts_dict in scripts_dict.items():
        # Create method ie: do_accounts
        main_method_name = f"do_{package_name}"
        script_names = list(package_scripts_dict.keys())
        exec_string = f"def {main_method_name}(self, script_name): \n \
              \t\"\"\"{package_name} [script]\n \
              Execute {package_name} script: {script_names}\"\"\"\n \
              \tif script_name and script_name in {script_names}:\n \
                  \t\tcommand = f'cd ./packages/{package_name} && yarn run {{script_name}}'\n \
                  \t\tprint(command)\n \
                  \t\tresult = subprocess.run(command,stdout=subprocess.PIPE, cwd='{working_directory}',shell=True)\n \
                  \t\tprint(result.stdout.decode('utf-8')) \
          "
        # print(exec_string)
        exec(exec_string)  # Create do_*main_method_name* cmd command
        main_method = locals()[main_method_name]
        setattr(RunnerCli, main_method_name, main_method)

        # Create auto-completion for main method ie: complete_accounts
        complete_method_name = f"complete_{package_name}"
        exec_string = f"def {complete_method_name}(self, text, line, begidx, endidx):\n \
              \tif not text:\n \
                  \t\tcompletions = {script_names}[:]\n \
              \telse:\n \
                  \t\tcompletions = [ f \n\
                                  \t\t\tfor f in {script_names}\n \
                                  \t\t\tif f.startswith(text)\n \
                                  \t\t]\n \
              \treturn completions"

        # print(exec_string)
        exec(exec_string)  # Create do_*main_method_name* cmd command
        complete_method = locals()[complete_method_name]
        setattr(RunnerCli, complete_method_name, complete_method)

    RunnerCli().cmdloop()

