import json
from connectors_sdk.utils import create_connector
import click

known_connector_types = [
    "elastic_connectors.filesystem:FilesystemConnector",
    "external_contribution_connector.connector:ExternalContributionConnector"
]

@click.group(
    invoke_without_command=True,
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.pass_context
def main(ctx):
    # print help page if no subcommands provided
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        return
    

@click.command(help="Run a connector once")
@click.option('--connector-type', type=click.Choice(known_connector_types))
def run(connector_type):
    while connector_type is None:
        click.echo("Please select connector type:")
        for idx, value in enumerate(known_connector_types):
            click.echo(f"\t[{idx}] {value}")

        selected_idx = click.prompt("Enter index of the type", type=int)

        if selected_idx < len(known_connector_types):
            connector_type = known_connector_types[selected_idx]



    click.echo(f"Running connector: {connector_type}")
    connector = create_connector(connector_type, {})

    for doc in connector.get_docs():
        print(json.dumps(doc, indent=4))

main.add_command(run)
