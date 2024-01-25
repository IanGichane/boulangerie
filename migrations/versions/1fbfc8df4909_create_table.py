"""create table

Revision ID: 1fbfc8df4909
Revises: 
Create Date: 2024-01-25 21:55:12.697624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fbfc8df4909'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=25), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('noProducts', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('image', sa.String(length=25), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orderdetails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('unit_price', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('to_be_delivered_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('ordered_date', sa.TIMESTAMP(), nullable=False),
    sa.Column('deliver_address', sa.String(length=25), nullable=False),
    sa.Column('payment_method', sa.String(length=25), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orderdetails')
    op.drop_table('product')
    op.drop_table('cart')
    op.drop_table('user')
    op.drop_table('category')
    # ### end Alembic commands ###
