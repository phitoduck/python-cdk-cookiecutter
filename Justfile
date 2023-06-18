install:
    python -m pip install pipx

test:
    #!/bin/bash
    cat << EOF > ./example-cookiecutter.yaml
    default_context:
        repo_name: hi-repo
        repo_description: description yall
        import_name: hi_import_name
    EOF

    pipx run cookiecutter ~/repos/extra/python-cdk-cookiecutter \
        --output-dir ./example \
        --overwrite-if-exists \
        --accept-hooks yes \
        --no-input \
        --config-file ./example-cookiecutter.yaml

    rm ./example-cookiecutter.yaml
    cd ./example/hi-repo
    pipx run pre-commit run --all-files