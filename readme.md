# Introduction

This azure functions app demonstrates how to use htmx with Python and Jinja2 as a basis.

## Environment Setup

Run inside the devcontainer or make sure you have python 3.9(.2) installed.
As well as the azure function core tools (not sure if .NET is required but it is contained in the devcontainer)

```sh
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt 
```

## Run

Either run locally using

```sh
func start
```

where the endpoints are reached under `<BASE_URL>/api/<ENDPOINT>`,

or deploy to an azure function app.
