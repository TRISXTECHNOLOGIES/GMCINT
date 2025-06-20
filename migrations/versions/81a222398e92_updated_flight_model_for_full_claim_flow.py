"""Updated Flight model for full claim flow

Revision ID: 81a222398e92
Revises: 77352436850c
Create Date: 2025-06-10 23:45:44.866362

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '81a222398e92'
down_revision = '77352436850c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flight', schema=None) as batch_op:
        batch_op.add_column(sa.Column('signature_path', sa.String(length=255), nullable=True))
        batch_op.alter_column('verification_token',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=255),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flight', schema=None) as batch_op:
        batch_op.alter_column('verification_token',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=True)
        batch_op.drop_column('signature_path')

    # ### end Alembic commands ###
