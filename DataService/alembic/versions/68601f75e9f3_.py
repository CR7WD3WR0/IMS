"""empty message

Revision ID: 68601f75e9f3
Revises: 19336b62adb3
Create Date: 2018-06-21 16:26:00.746540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68601f75e9f3'
down_revision = '19336b62adb3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fields', sa.Column('description', sa.String(length=256), nullable=True))
    op.add_column('fields', sa.Column('note', sa.Text(), nullable=True))
    op.add_column('tables', sa.Column('description', sa.String(length=256), nullable=True))
    op.add_column('tables', sa.Column('note', sa.Text(), nullable=True))
    op.create_unique_constraint(None, 'tables', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tables', type_='unique')
    op.drop_column('tables', 'note')
    op.drop_column('tables', 'description')
    op.drop_column('fields', 'note')
    op.drop_column('fields', 'description')
    # ### end Alembic commands ###
