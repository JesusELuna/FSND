"""empty message

Revision ID: 0b447827b2dc
Revises: f0a089916452
Create Date: 2020-02-27 18:51:19.312813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b447827b2dc'
down_revision = 'f0a089916452'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('genress', sa.ARRAY(sa.String()), nullable=True))
    op.drop_column('Artist', 'genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'genress')
    # ### end Alembic commands ###
