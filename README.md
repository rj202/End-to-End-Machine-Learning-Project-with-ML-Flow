# End-to-End-Machine-Learning-Project-with-ML-Flow

## .github\workflow folder is used for cicd deployments and the gitkeep is the document used for commit the folder.
## config.yaml is the file in which saves all the configuration of the project.

    Use YAML when:

    You need a human-readable format for configurations or structured data.
    You are working with applications that require complex configurations, such as Docker, Kubernetes, CI/CD pipelines, etc.
    You prefer a flexible format but are willing to deal with indentation as a strict rule.


## the yaml files should not be empty

## Config file:
A config file is usually meant to hold dynamic settings (like user settings, environment-specific configurations, or settings that change between deployments). This allows for easy adjustments without touching the code.
## Constant file:
This is more focused on values that are static and code-related, such as file paths, hardcoded configuration values, or other system-level constants.

## UTILS.PY
A utils.py file generally contains functions that are used throughout your project, such as data processing, file manipulation, validations, and more.

## Workflows

1. Update config.yaml 
2. Update schema.yaml 
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.yaml


