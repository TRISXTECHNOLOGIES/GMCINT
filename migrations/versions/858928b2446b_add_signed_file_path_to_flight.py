"""add signed_file_path to Flight"""

from alembic import op
import sqlalchemy as sa

# Match this to the revision before 858928b2446b — likely None if it was the first
down_revision = None
revision = '858928b2446b'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('flight', sa.Column('signed_file_path', sa.String(length=255), nullable=True))

def downgrade():
    op.drop_column('flight', 'signed_file_path')
