"""empty message

Revision ID: 199117b69374
Revises: 4ff8e3093e04
Create Date: 2022-12-23 15:10:04.691275

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '199117b69374'
down_revision = '4ff8e3093e04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.alter_column('genres',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.alter_column('genres',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               nullable=True)

    # ### end Alembic commands ###
