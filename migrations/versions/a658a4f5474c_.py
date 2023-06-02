"""empty message

Revision ID: a658a4f5474c
Revises: aac11852b1bc
Create Date: 2023-06-01 20:34:00.129994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a658a4f5474c'
down_revision = 'aac11852b1bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.DateTime(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.drop_column('email')

    # ### end Alembic commands ###