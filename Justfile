install:
    python -m pip install pipx

make-example:
    #!/bin/bash
    cat << EOF > ./example-cookiecutter.yaml
    default_context:
        repo_name: hi-repo
        repo_description: description yall
        import_name: hi_import_name
    EOF

    pipx run cookiecutter ./ \
        --output-dir ./example \
        --overwrite-if-exists \
        --accept-hooks yes \
        --no-input \
        --config-file ./example-cookiecutter.yaml

test: clean make-example
    #!/bin/bash
    set -e

    rm ./example-cookiecutter.yaml
    cd ./example/hi-repo
    pipx run pre-commit run --all-files

    # just --justfile ./infrastructure/Justfile --working-directory ./infrastructure -- install
    cd ./infrastructure/
    just install
    just cdk synth

clean:
    rm -rf example-cookiecutter.yaml ./example/
    find . \
        -name "node_modules" -prune -false \
        -o -name "*venv" -prune -false \
        -o -name ".git" -prune -false \
        -o -type d -name "*.egg-info" \
        -o -type d -name "dist" \
        -o -type d -name ".projen" \
        -o -type d -name "build_" \
        -o -type d -name "build" \
        -o -type d -name "cdk.out" \
        -o -type d -name ".mypy_cache" \
        -o -type d -name ".pytest_cache" \
        -o -type d -name "test-reports" \
        -o -type d -name "htmlcov" \
        -o -type d -name ".coverage" \
        -o -type d -name ".ipynb_checkpoints" \
        -o -type d -name "__pycache__" \
        -o -type f -name "coverage.xml" \
        -o -type f -name ".DS_Store" \
        -o -type f -name "*.pyc" \
        -o -type f -name ".coverage" \
        -o -type f -name "*cdk.context.json" | xargs rm -rf {}

