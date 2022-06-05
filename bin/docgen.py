import os
import sys
from textwrap import dedent
from collections import OrderedDict

from open_bus_stride_db.model import Base

from sqlalchemy_schemadisplay import create_schema_graph


DATA_MODEL_URL = 'https://github.com/hasadna/open-bus-stride-db/blob/main/DATA_MODEL.md'


# TODO: populate automatically and link to the ETL documentation
ETL_LINKS = {
    "open_bus_stride_etl.gtfs.update_ride_aggregations": {},
    "open-bus-stride-etl.siri.add-ride-duration-minutes": {},
    "open-bus-stride-etl.siri.update-rides-gtfs": {},
}


def generate_dbschema(output_dir):
    graph = create_schema_graph(
        metadata=Base.metadata,
        show_datatypes=False,  # The image would get nasty big if we'd show the datatypes
        show_indexes=False,  # ditto for indexes
        rankdir='LR',  # From left to right (instead of top to bottom)
        concentrate=False  # Don't try to join the relation lines together
    )
    graph.write_png(os.path.join(output_dir, 'dbschema.png'))  # write out the file


def get_desc_markdown(tables, table_name_, desc):
    desc = dedent(desc).strip()
    for table_name, table in tables.items():
        desc = desc.replace(
            f'[[{table_name}]]',
            f'[{table_name}]({DATA_MODEL_URL}#{table_name})'
        )
        for column_name in table['columns'].keys():
            desc = desc.replace(
                f'[[{table_name}.{column_name}]]',
                f'[{table_name}.{column_name}]({DATA_MODEL_URL}#{table_name}{column_name})'
            )
            if table_name_ == table_name:
                desc = desc.replace(
                    f'[[{column_name}]]',
                    f'[{column_name}]({DATA_MODEL_URL}#{table_name}{column_name})'
                )
    for etl_link_id in ETL_LINKS.keys():
        desc = desc.replace(
            f'[[{etl_link_id}]]',
            f'`{etl_link_id}`',
        )
    return desc + "\n\n"


def generate_markdown(output_dir):
    markdown = "# Open Bus Stride Data Model\n\n"
    markdown += "![Database Schema Diagram](dbschema.png)\n\n"
    tables = OrderedDict()
    for table_name, table in Base.metadata.tables.items():
        columns = OrderedDict()
        for column_name, column in table.columns.items():
            if not column.info.get('hide'):
                columns[column_name] = {'desc': column.info.get('desc')}
        tables[table_name] = {
            'desc': table.info.get('desc'),
            'columns': columns
        }
    for table_name, table in tables.items():
        markdown += f'## {table_name}\n\n'
        if table['desc']:
            markdown += get_desc_markdown(tables, table_name, table['desc'])
        for column_name, column in table['columns'].items():
            markdown += f'#### {table_name}.{column_name}\n\n'
            if column['desc']:
                markdown += get_desc_markdown(tables, table_name, column['desc'])
    with open(os.path.join(output_dir, "DATA_MODEL.md"), 'w') as f:
        f.write(markdown)


generate_dbschema(sys.argv[1])
generate_markdown(sys.argv[1])
