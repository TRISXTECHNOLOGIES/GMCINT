"""Restore Partner model"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect

revision = '77352436850c'
down_revision = '858928b2446b'
branch_labels = None
depends_on = None

def upgrade():
    conn = op.get_bind()
    inspector = inspect(conn)
    if 'partner' not in inspector.get_table_names():
        op.create_table(
            'partner',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('name', sa.String(length=100), nullable=True),
            sa.Column('email', sa.String(length=100), nullable=True),
            sa.Column('password', sa.String(length=200), nullable=True),
            sa.PrimaryKeyConstraint('id'),
            sa.UniqueConstraint('email')
        )

