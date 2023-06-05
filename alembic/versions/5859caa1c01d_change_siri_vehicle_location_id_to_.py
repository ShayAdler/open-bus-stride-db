"""change siri vehicle location id to bigint

Revision ID: 5859caa1c01d
Revises: 8cc970f13408
Create Date: 2023-06-05 16:04:20.892090+00:00

"""
from alembic import op
import sqlalchemy as sa


import open_bus_stride_db


# revision identifiers, used by Alembic.
revision = '5859caa1c01d'
down_revision = '8cc970f13408'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('siri_ride', 'first_vehicle_location_id', existing_type=sa.Integer, type_=sa.BigInteger)
    op.alter_column('siri_ride', 'last_vehicle_location_id', existing_type=sa.Integer, type_=sa.BigInteger)
    op.alter_column('siri_ride_stop', 'nearest_siri_vehicle_location_id', existing_type=sa.Integer, type_=sa.BigInteger)
    op.alter_column('siri_vehicle_location', 'id', existing_type=sa.Integer, type_=sa.BigInteger)
    op.execute('ALTER SEQUENCE siri_vehicle_location_id_seq AS BIGINT')
    op.execute('SELECT setval(\'siri_vehicle_location_id_seq\', 2147483648)')


def downgrade():
    raise Exception('Cannot downgrade')
