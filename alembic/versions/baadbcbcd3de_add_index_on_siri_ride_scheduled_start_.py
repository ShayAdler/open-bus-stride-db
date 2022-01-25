"""add index on siri_ride scheduled_start_time converted to date

Revision ID: baadbcbcd3de
Revises: abd8075c2d94
Create Date: 2022-01-25 15:10:58.165464+00:00

"""
from textwrap import dedent

from alembic import op
import sqlalchemy as sa


import open_bus_stride_db


# revision identifiers, used by Alembic.
revision = 'baadbcbcd3de'
down_revision = 'abd8075c2d94'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(dedent("""
        CREATE INDEX idx_siri_ride_scheduled_start_date
        ON siri_ride
        (date_trunc('day', scheduled_start_time))
    """))


def downgrade():
    op.execute(dedent("""
        DROP INDEX idx_siri_ride_scheduled_start_date
    """))
