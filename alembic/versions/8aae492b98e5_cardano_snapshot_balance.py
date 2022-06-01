"""cardano_snapshot_balance

Revision ID: 8aae492b98e5
Revises: f2a83041662e
Create Date: 2022-06-01 08:40:11.800031

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8aae492b98e5'
down_revision = 'f2a83041662e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('token',
                    sa.Column('row_id', sa.BIGINT(), autoincrement=True, nullable=False),
                    sa.Column('id', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('name', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('blockchain_name', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('description', sa.TEXT(), nullable=False),
                    sa.Column('symbol', sa.VARCHAR(length=30), nullable=False),
                    sa.Column('token_address', sa.VARCHAR(length=100), nullable=False),
                    sa.Column('balance_types', sa.VARCHAR(length=100), nullable=False),
                    sa.Column('allowed_decimal', sa.INTEGER(), nullable=True),
                    sa.Column('is_enabled', sa.BOOLEAN(), nullable=True),
                    sa.Column('created_by', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'),
                              nullable=False),
                    sa.Column('updated_at', mysql.TIMESTAMP(),
                              server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
                    sa.PrimaryKeyConstraint('row_id'),
                    sa.UniqueConstraint('blockchain_name', 'symbol'),
                    sa.UniqueConstraint('id'),
                    sa.UniqueConstraint('token_address')
                    )
    op.create_table('cardano_balance',
                    sa.Column('row_id', sa.BIGINT(), autoincrement=True, nullable=False),
                    sa.Column('id', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('token_id', sa.BIGINT(), nullable=True),
                    sa.Column('address', sa.VARCHAR(length=120), nullable=False),
                    sa.Column('stake_key', sa.VARCHAR(length=120), nullable=True),
                    sa.Column('balance', sa.NUMERIC(precision=30, scale=0), nullable=False),
                    sa.Column('balance_type', sa.VARCHAR(length=30), nullable=True),
                    sa.Column('created_by', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'),
                              nullable=False),
                    sa.Column('updated_at', mysql.TIMESTAMP(),
                              server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
                    sa.ForeignKeyConstraint(['token_id'], ['token.row_id'], ),
                    sa.PrimaryKeyConstraint('row_id'),
                    sa.UniqueConstraint('id'),
                    sa.UniqueConstraint('token_id', 'address', 'balance_type')
                    )
    op.create_table('snapshot_history',
                    sa.Column('row_id', sa.BIGINT(), autoincrement=True, nullable=False),
                    sa.Column('id', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('token_id', sa.BIGINT(), nullable=True),
                    sa.Column('status', sa.VARCHAR(length=30), nullable=False),
                    sa.Column('address_count', sa.BIGINT(), nullable=False),
                    sa.Column('delta_count', sa.BIGINT(), nullable=False),
                    sa.Column('snapshot_type', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('snapshot_date', mysql.TIMESTAMP(), nullable=False),
                    sa.Column('created_by', sa.VARCHAR(length=50), nullable=False),
                    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'),
                              nullable=False),
                    sa.Column('updated_at', mysql.TIMESTAMP(),
                              server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
                    sa.ForeignKeyConstraint(['token_id'], ['token.row_id'], ),
                    sa.PrimaryKeyConstraint('row_id'),
                    sa.UniqueConstraint('id'),
                    sa.UniqueConstraint('token_id', 'snapshot_type', 'snapshot_date')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('snapshot_history')
    op.drop_table('cardano_balance')
    op.drop_table('token')
    # ### end Alembic commands ###