"""followers

Revision ID: 258f3a1c86ef
Revises: a524776a1ebb
Create Date: 2019-11-07 16:06:42.362799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '258f3a1c86ef'
down_revision = 'a524776a1ebb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
