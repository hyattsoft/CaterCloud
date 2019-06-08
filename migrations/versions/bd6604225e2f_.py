"""empty message

Revision ID: bd6604225e2f
Revises: 
Create Date: 2019-06-08 18:25:48.068904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd6604225e2f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sys_user',
    sa.Column('code', sa.String(length=6), nullable=False, comment='编码'),
    sa.Column('nick_name', sa.String(length=20), nullable=False, comment='姓名'),
    sa.Column('login_name', sa.String(length=20), nullable=False, comment='登陆名称'),
    sa.Column('login_pass', sa.String(length=32), nullable=False, comment='登陆密码'),
    sa.Column('isDownload', sa.Integer(), nullable=False, comment='是否可下载'),
    sa.Column('isServices', sa.Integer(), nullable=False, comment='是否服务员'),
    sa.PrimaryKeyConstraint('code'),
    sa.UniqueConstraint('login_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sys_user')
    # ### end Alembic commands ###
