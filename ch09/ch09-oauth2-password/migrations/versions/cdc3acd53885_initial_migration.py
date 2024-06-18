"""Initial migration.

Revision ID: cdc3acd53885
Revises: 
Create Date: 2024-01-28 01:15:21.763656

"""
from alembic import op
import sqlalchemy as sa
import authlib.integrations.sqla_oauth2


# revision identifiers, used by Alembic.
revision = 'cdc3acd53885'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('login',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('user_id', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('vaccination_center',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vaccenterid', sa.String(length=20), nullable=False),
    sa.Column('centername', sa.String(length=100), nullable=False),
    sa.Column('telephone', sa.String(length=20), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.Column('city', sa.String(length=50), nullable=False),
    sa.Column('province', sa.String(length=50), nullable=False),
    sa.Column('region', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('vaccenterid')
    )
    op.create_table('vaccine',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vacid', sa.String(length=20), nullable=False),
    sa.Column('vacname', sa.String(length=50), nullable=False),
    sa.Column('vacdesc', sa.String(length=100), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.Column('price', sa.Double(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('vacid')
    )
    op.create_table('administrator',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('adminid', sa.String(length=12), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('firstname', sa.String(length=50), nullable=False),
    sa.Column('midname', sa.String(length=50), nullable=False),
    sa.Column('lastname', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=25), nullable=False),
    sa.Column('mobile', sa.String(length=15), nullable=False),
    sa.Column('position', sa.String(length=100), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.ForeignKeyConstraint(['username'], ['login.username'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('adminid')
    )
    op.create_table('doctor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('docid', sa.String(length=12), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('firstname', sa.String(length=50), nullable=False),
    sa.Column('midname', sa.String(length=50), nullable=False),
    sa.Column('lastname', sa.String(length=50), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.Column('email', sa.String(length=25), nullable=False),
    sa.Column('mobile', sa.String(length=15), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('vaccenterid', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['username'], ['login.username'], ),
    sa.ForeignKeyConstraint(['vaccenterid'], ['vaccination_center.vaccenterid'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('docid')
    )
    op.create_table('inventory',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vacid', sa.String(length=20), nullable=False),
    sa.Column('vaccenterid', sa.String(length=20), nullable=False),
    sa.Column('date_delivered', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['vaccenterid'], ['vaccination_center.vaccenterid'], ),
    sa.ForeignKeyConstraint(['vacid'], ['vaccine.vacid'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('vacid')
    )
    op.create_table('oauth2_client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=20), nullable=True),
    sa.Column('client_id', sa.String(length=48), nullable=True),
    sa.Column('client_secret', sa.String(length=120), nullable=True),
    sa.Column('client_id_issued_at', sa.Integer(), nullable=False),
    sa.Column('client_secret_expires_at', sa.Integer(), nullable=False),
    sa.Column('client_metadata', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['login.username'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    with op.batch_alter_table('oauth2_client', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_oauth2_client_client_id'), ['client_id'], unique=False)

    op.create_table('oauth2_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=40), nullable=False),
    sa.Column('client_id', sa.String(length=48), nullable=True),
    sa.Column('token_type', sa.String(length=40), nullable=True),
    sa.Column('access_token', sa.String(length=255), nullable=False),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.Column('scope', sa.Text(), nullable=True),
    sa.Column('issued_at', sa.Integer(), nullable=False),
    sa.Column('access_token_revoked_at', sa.Integer(), nullable=False),
    sa.Column('refresh_token_revoked_at', sa.Integer(), nullable=False),
    sa.Column('expires_in', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['login.username'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('access_token')
    )
    with op.batch_alter_table('oauth2_token', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_oauth2_token_refresh_token'), ['refresh_token'], unique=False)

    op.create_table('patient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patientid', sa.String(length=20), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('firstname', sa.String(length=50), nullable=False),
    sa.Column('midname', sa.String(length=50), nullable=False),
    sa.Column('lastname', sa.String(length=50), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=25), nullable=False),
    sa.Column('mobile', sa.String(length=15), nullable=False),
    sa.Column('gender', sa.String(length=10), nullable=False),
    sa.ForeignKeyConstraint(['username'], ['login.username'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('patientid')
    )
    op.create_table('vaccine_card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cardid', sa.String(length=20), nullable=False),
    sa.Column('patientid', sa.String(length=20), nullable=False),
    sa.Column('docid', sa.String(length=100), nullable=False),
    sa.Column('vacid', sa.String(length=20), nullable=False),
    sa.Column('date_vaccinated', sa.Double(), nullable=False),
    sa.ForeignKeyConstraint(['docid'], ['doctor.docid'], ),
    sa.ForeignKeyConstraint(['patientid'], ['patient.patientid'], ),
    sa.ForeignKeyConstraint(['vacid'], ['vaccine.vacid'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cardid')
    )
    op.create_table('vaccine_registration',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vacid', sa.String(length=20), nullable=False),
    sa.Column('regcode', sa.String(length=50), nullable=False),
    sa.Column('adminid', sa.String(length=12), nullable=False),
    sa.Column('date_registration', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['adminid'], ['administrator.adminid'], ),
    sa.ForeignKeyConstraint(['vacid'], ['vaccine.vacid'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('vacid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vaccine_registration')
    op.drop_table('vaccine_card')
    op.drop_table('patient')
    with op.batch_alter_table('oauth2_token', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_oauth2_token_refresh_token'))

    op.drop_table('oauth2_token')
    with op.batch_alter_table('oauth2_client', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_oauth2_client_client_id'))

    op.drop_table('oauth2_client')
    op.drop_table('inventory')
    op.drop_table('doctor')
    op.drop_table('administrator')
    op.drop_table('vaccine')
    op.drop_table('vaccination_center')
    op.drop_table('login')
    # ### end Alembic commands ###
