#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Command line interface
# Reference Projects: OPAM & Flatpak & Homebrew
# Both OPAM & Flatpak have similar module of distribution as rimebrew

from . import click
from .utility_functions import RimePaths, mkdir
import os.path


@click.group()
def cli():
    """rimebrew: the canonical input schemas manager :D"""


@cli.command()
@click.argument('help_entry')
@click.pass_context  # TODO ？？
def help(ctx, help_entry):
    subcommand_obj = cli.get_command(ctx, help_entry)
    if subcommand_obj is None:
        click.echo("Unknown command!")
    else:
        click.echo(subcommand_obj.get_help(ctx))


@cli.command()
@click.argument('schema_name')
def install(schema_name):
    """Install a schema"""
    _schema_name = schema_name
    print(_schema_name)
    if _schema_name is None:
        click.echo("rimebrew install <schema_id>: Missing schema name  ")
    else:
        from .install import basic_install
        basic_install(schema_name)
        print("Installed")
        # TODO modify user.yaml


@cli.command()
def list():
    """Display a table of available schemas"""
    from .inspector import print_schemas
    print_schemas()


@cli.command()
def remove():
    """Remove a installed schema"""
    pass


@cli.command()
def update():
    """Fetch new schemas form repos and refresh local index."""
    from .update import update

    # warning: maybe it looks reluctant, the MacOS require such way to create a file.
    # TODO move this into somewhere init
    if not os.path.exists(RimePaths.user_profile_yaml):
        with open(RimePaths.user_profile_yaml, 'w'): pass
    update()


@cli.command()
def upgrade():
    """Update an installed schema"""
    pass


@cli.command()
def debug():
    """Used for developers"""
    from .user_profile import user_profile
    test_profile = user_profile(path="/home/slb/.config/ibus/rime/rimebrew/user_profile.yaml")
    print(test_profile.get_installed_schema())


# I don't know its my problem or python's problem
# The relative import mechism of py is not intuitive
# with some obscure rules.

def main():
    cli()

if __name__ == '__main__':
     main()
