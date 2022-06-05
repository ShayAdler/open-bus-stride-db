from textwrap import dedent
from collections import OrderedDict

from open_bus_stride_db.model import Base

from sqlalchemy_schemadisplay import create_schema_graph


def generate_dbschema():
    graph = create_schema_graph(
        metadata=Base.metadata,
        show_datatypes=False,  # The image would get nasty big if we'd show the datatypes
        show_indexes=False,  # ditto for indexes
        rankdir='LR',  # From left to right (instead of top to bottom)
        concentrate=False  # Don't try to join the relation lines together
    )
    graph.write_png('dbschema.png')  # write out the file


def get_desc_markdown(tables, table_name, desc):
    return dedent(desc).strip() + "\n\n"


def generate_markdown():
    markdown = "# Open Bus Stride Data Model\n\n"
    markdown += "![Database Schema Diagram](dbschema.png)\n\n"
    tables = OrderedDict()
    for table_name, table in Base.metadata.tables.items():
        columns = OrderedDict()
        for column_name, column in table.columns.items():
            columns[column_name] = {'desc': column.info.get('desc')}
        tables[table_name] = {
            'desc': table.info.get('desc'),
            'columns': columns
        }
    for table_name, table in tables.items():
        markdown += f'### {table_name}\n\n'
        if table['desc']:
            markdown += get_desc_markdown(tables, table_name, table['desc'])
        for column_name, column in table['columns'].items():
            markdown += f'#### {column_name}\n\n'
            if column['desc']:
                markdown += get_desc_markdown(tables, table_name, column['desc'])
    with open("./DATA_MODEL.md", 'w') as f:
        f.write(markdown)


# generate_dbschema()
generate_markdown()
