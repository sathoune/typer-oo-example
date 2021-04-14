# Typer-oo

This is answer to question from [typer issue 261](
https://github.com/tiangolo/typer/issues/261
).

# Getting started.

### Poetry

```shell
poetry install
```

### pip

```shell
pip install -r requirements.txt
```

# Run.

### Modules including `click`:

Given name of the module `something_click_else`:

```shell
python -m something_click_else.runner
```

### Module `typer_example`:

```shell
python -m typer_example.dev
```

# Content:

## click_example

Example from [this post](
https://github.com/tiangolo/typer/issues/261#issuecomment-819174185
) with additions to make the script able to execute.

## click_to_typer

* AbstractBaseClass that uses static methods to declare commands.
* Wrapper around `app.commmand()(lambda x: "my function")`

## config_click_to_typer

* Usage of `self` attribute to expose some data.

## click_to_many_typers

* registering two typers.

## typer_example

* Modified code from original question to the state the user goes through designed path.