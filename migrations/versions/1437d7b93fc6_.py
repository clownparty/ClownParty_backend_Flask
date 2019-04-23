"""empty message

Revision ID: 1437d7b93fc6
Revises: 
Create Date: 2019-04-23 13:09:24.781779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1437d7b93fc6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pokemon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('pokemonnumber', sa.Integer(), nullable=False),
    sa.Column('pokemondescription', sa.Text(), nullable=False),
    sa.Column('pokemonimage', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('fav_poke', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('team',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('teamname', sa.String(length=128), nullable=False),
    sa.Column('slot1', sa.Integer(), nullable=True),
    sa.Column('slot2', sa.Integer(), nullable=True),
    sa.Column('slot3', sa.Integer(), nullable=True),
    sa.Column('slot4', sa.Integer(), nullable=True),
    sa.Column('slot5', sa.Integer(), nullable=True),
    sa.Column('slot6', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['slot1'], ['pokemon.id'], ),
    sa.ForeignKeyConstraint(['slot2'], ['pokemon.id'], ),
    sa.ForeignKeyConstraint(['slot3'], ['pokemon.id'], ),
    sa.ForeignKeyConstraint(['slot4'], ['pokemon.id'], ),
    sa.ForeignKeyConstraint(['slot5'], ['pokemon.id'], ),
    sa.ForeignKeyConstraint(['slot6'], ['pokemon.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('team')
    op.drop_table('user')
    op.drop_table('pokemon')
    # ### end Alembic commands ###