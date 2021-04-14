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
python -m something_click_else
```

### Module `typer_example`:

```shell
python -m typer_example
```

# Content:

## click_example

#### Command

```shell
python -m click_example
```

Example from [this post](
https://github.com/tiangolo/typer/issues/261#issuecomment-819174185
) with additions to make the script able to execute.

## click_to_typer

#### Command

```shell
python -m click_to_typer
```

#### Features

* AbstractBaseClass that uses static methods to declare commands.
* Wrapper around `app.commmand()(lambda x: "my function")`

## config_click_to_typer

#### Command

```shell
python -m config_click_to_typer
```

#### Features

* Usage of `self` attribute to expose some data.

## click_to_many_typers

#### Command

```shell
python -m click_to_many_typers
```

#### Features

* registering two typers.

## typer_example

#### Command

```shell
python -m typer_example
```

#### Features

* Modified code from original question to the state the user goes through designed path.