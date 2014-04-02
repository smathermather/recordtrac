"""Add reason_unassigned to Owner

Revision ID: 53a8fafffb47
Revises: 49b52a2b959f
Create Date: 2014-03-22 16:52:34.850678

"""

# revision identifiers, used by Alembic.
revision = '53a8fafffb47'
down_revision = '49b52a2b959f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('owner', sa.Column('reason_unassigned', sa.String()))
    ### end Alembic commands ###

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('owner', 'reason_unassigned')
    ### end Alembic commands ###


