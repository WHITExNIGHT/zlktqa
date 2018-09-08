"""empty message

Revision ID: 7f45919965ef
Revises: 42037a2f9972
Create Date: 2018-09-07 18:14:32.442143

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7f45919965ef'
down_revision = '42037a2f9972'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('content', sa.Text(), nullable=False))
    op.drop_column('answer', 'title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('title', mysql.TEXT(), nullable=False))
    op.drop_column('answer', 'content')
    # ### end Alembic commands ###