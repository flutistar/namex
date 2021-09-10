"""state consumed

Revision ID: 0be658f07ac6
Revises: bd1e892d0609
Create Date: 2021-07-18 21:26:04.588007

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String


# revision identifiers, used by Alembic.
revision = '0be658f07ac6'
down_revision = 'bd1e892d0609'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    
    # Create an ad-hoc table to use for the insert statement.
    states_table = table('states',
                           column('cd', String),
                           column('description', String)
                           )
    op.bulk_insert(
        states_table,
        [
            {'cd': 'CONSUMED',  'description': 'CONSUMED by a corp'}
        ]
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("DELETE FROM states WHERE cd = 'CONSUMED';")
    # ### end Alembic commands ###
