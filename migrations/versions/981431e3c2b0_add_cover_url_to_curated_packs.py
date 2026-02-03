"""Add cover_url to curated_packs

Revision ID: 981431e3c2b0
Revises: 122c192ce573
Create Date: 2026-02-03 13:38:26.409479

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '981431e3c2b0'
down_revision = '122c192ce573'
branch_labels = None
depends_on = None


def upgrade():
    # Add cover_url column to curated_packs
    op.add_column('curated_packs', sa.Column('cover_url', sa.String(length=500), nullable=True))


def downgrade():
    # Remove cover_url column from curated_packs
    op.drop_column('curated_packs', 'cover_url')
