# runner-cli

A command-line interface (CLI) tool to execute scripts defined in ```package.json``` files within your project's packages. This tool simplifies running package scripts by providing an interactive shell with auto-completion features.


![Nov-29-2024 10-08-36](https://github.com/user-attachments/assets/c1ff2c2b-db8f-4d07-bfc2-b045deef2282)


## Features

- **Interactive CLI**: Navigate and execute scripts using a simple command-line interface.
- **Auto-Completion**: Provides tab completion for package names and scripts.
- **Cross-Platform**: Compatible with Windows, macOS, and Linux systems.
- **Simplified Workflow**: Run any package script without navigating to the package directory.

## Installation

Since the package is currently local to your project, you can install it directly from your codebase.

### Install from Local Source

Navigate to the root directory of your project (where ```setup.py``` is located) and run:

```bash
pip install .
```

Or, to install in editable mode (useful for development):

```bash
pip install -e .
```

## Usage

Ensure you are in the root directory of your project, which should have a ```packages``` subdirectory containing your packages.

### Starting the CLI

Run the following command to start the interactive CLI:

```bash
runner-cli
```

### CLI Commands

Once inside the CLI, you can execute scripts from your packages:

```
runner-cli: [package_name] [script_name]
```

- **```[package_name]```**: The name of the package (directory inside ```packages```).
- **```[script_name]```**: The name of the script defined in the package's ```package.json``` under the ```scripts``` section.

### Example

Suppose you have a package named ```authentication``` with a script ```test``` defined in its ```package.json```. You can run:

```bash
runner-cli: authentication test
```

This command will execute the ```test``` script inside the ```authentication``` package.

### Auto-Completion

Press ```Tab``` to auto-complete package names and script names:

- Start typing the package name and press ```Tab``` to auto-complete.
- After the package name, press ```Tab``` again to auto-complete available scripts.

### Exiting the CLI

To exit the CLI, you can use the ```EOF``` command or press ```Ctrl+D```.

## Project Structure Requirement

Your project should follow this structure:

```
root/
├─ packages/
│  ├─ package1/
│  │  ├─ package.json
│  ├─ package2/
│  │  ├─ package.json
```

Each package should contain a ```package.json``` file with a ```scripts``` section.

## How It Works

- The tool scans the ```packages/``` directory for all packages.
- It parses each ```package.json``` to collect available scripts.
- Generates CLI commands dynamically for each package and its scripts.
- Executes the selected script using ```yarn run``` inside the package directory.

## Dependencies

- **Python 3.6 or higher**
- **```yarn```** should be installed and available in your system's PATH.

## Development

### Cloning the Repository

If you have your code in a repository, clone it:

```bash
git clone https://github.com/yourusername/runner-cli.git
cd runner-cli
```

### Installing in Development Mode

Install the package in editable mode to reflect code changes immediately:

```bash
pip install -e .
```

### Running the Tool

From the project root:

```bash
runner-cli
```

## License

This project is licensed under the MIT License.

## Author

**Jason Poindexter**

- **Email**: [poindexter.json@gmail.com](mailto:poindexter.json@gmail.com)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## Acknowledgments

- Inspired by the need to simplify running package scripts across multiple packages in a monorepo setup.
