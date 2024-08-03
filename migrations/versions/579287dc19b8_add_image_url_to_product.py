"""Add image_url to Product

Revision ID: 579287dc19b8
Revises: 
Create Date: 2024-07-30 20:51:10.710052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '579287dc19b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.String(length=200), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_column('image_url')

    # ### end Alembic commands ###