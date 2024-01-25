# Resume Generator

This project is a Python script that generates a resume from a TOML file. It generates a LaTeX document.

## Features

- Generates a resume from a TOML file
- Supports different sections such as profile, skills, work experiences, and projects
- Allows for customization of the resume layout on a per role basis

## Usage

This project uses poetry.

1. Install the required Python libraries with `poetry install`.
2. Create a `resume.toml` file in the current directory. This file should contain your resume information in TOML format.
3. Run the script with `poetry run toml-resume`.
4. The script will print the LaTeX document to stdout.

## Example

Example resume can be seen in `resume.toml.example`
