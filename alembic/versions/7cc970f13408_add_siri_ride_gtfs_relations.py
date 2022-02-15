"""add siri ride gtfs relations

Revision ID: 7cc970f13408
Revises: baadbcbcd3de
Create Date: 2022-02-01 14:17:00.290873+00:00

"""
from alembic import op
import sqlalchemy as sa


import open_bus_stride_db


# revision identifiers, used by Alembic.
revision = '7cc970f13408'
down_revision = 'baadbcbcd3de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('siri_ride', sa.Column('journey_gtfs_ride_id', sa.Integer(), nullable=True))
    op.add_column('siri_ride', sa.Column('route_gtfs_ride_id', sa.Integer(), nullable=True))
    op.add_column('siri_ride', sa.Column('gtfs_ride_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('siri_ride', 'gtfs_ride_id')
    op.drop_column('siri_ride', 'route_gtfs_ride_id')
    op.drop_column('siri_ride', 'journey_gtfs_ride_id')
    # ### end Alembic commands ###