"""empty message

Revision ID: 40709a13f64d
Revises: dcc03295ba71
Create Date: 2016-06-15 21:59:35.739000

"""

# revision identifiers, used by Alembic.
revision = '40709a13f64d'
down_revision = 'dcc03295ba71'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('session', sa.Column('comments', sa.Text(), nullable=True))
    op.add_column('speaker', sa.Column('long_biography', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('speaker', 'long_biography')
    op.drop_column('session', 'comments')
    ### end Alembic commands ###