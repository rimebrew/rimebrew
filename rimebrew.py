#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Command line interface
# Reference Projects: OPAM & Flatpak & Homebrew
# Both OPAM & Flatpak have similar module of distribution as rimebrew

import click

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
    from inspector import print_schemas
    print_schemas()


@cli.command()
def remove():
    """Remove a installed schema"""
    pass


@cli.command()
def update():
    """Fetch new schemas form repos and refresh local index."""
    from update import update
    update()


@cli.command()
def upgrade():
    """Update an installed schema"""
    pass


if __name__ == '__main__':

    cli()
