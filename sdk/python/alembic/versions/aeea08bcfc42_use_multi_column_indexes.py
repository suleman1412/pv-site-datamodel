"""Use multi-column indexes

Revision ID: aeea08bcfc42
Revises: 2ad22925d16f
Create Date: 2023-03-13 19:22:03.183403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aeea08bcfc42'
down_revision = '2ad22925d16f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_forecast_values_forecast_uuid', table_name='forecast_values')
    op.drop_index('ix_forecast_values_horizon_minutes', table_name='forecast_values')
    op.create_index('ix_forecast_values_forecast_uuid_horizon_minutes', 'forecast_values', ['forecast_uuid', 'horizon_minutes'], unique=False)
    op.drop_index('ix_forecasts_site_uuid', table_name='forecasts')
    op.drop_index('ix_forecasts_timestamp_utc', table_name='forecasts')
    op.create_index('ix_forecasts_site_uuid_timestamp_utc', 'forecasts', ['site_uuid', 'timestamp_utc'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_forecasts_site_uuid_timestamp_utc', table_name='forecasts')
    op.create_index('ix_forecasts_timestamp_utc', 'forecasts', ['timestamp_utc'], unique=False)
    op.create_index('ix_forecasts_site_uuid', 'forecasts', ['site_uuid'], unique=False)
    op.drop_index('ix_forecast_values_forecast_uuid_horizon_minutes', table_name='forecast_values')
    op.create_index('ix_forecast_values_horizon_minutes', 'forecast_values', ['horizon_minutes'], unique=False)
    op.create_index('ix_forecast_values_forecast_uuid', 'forecast_values', ['forecast_uuid'], unique=False)
    # ### end Alembic commands ###
