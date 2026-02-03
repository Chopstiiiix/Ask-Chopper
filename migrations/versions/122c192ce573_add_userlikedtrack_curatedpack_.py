"""Add UserLikedTrack, CuratedPack, CuratedPackTrack models

Revision ID: 122c192ce573
Revises: c39a4a5a6ae1
Create Date: 2026-02-03 13:11:15.845437

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '122c192ce573'
down_revision = 'c39a4a5a6ae1'
branch_labels = None
depends_on = None


def upgrade():
    # Create user_liked_tracks table
    op.create_table('user_liked_tracks',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('beat_id', sa.Integer(), nullable=False),
        sa.Column('liked_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['beat_id'], ['beats.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('user_id', 'beat_id', name='unique_user_liked_beat')
    )

    # Create curated_packs table
    op.create_table('curated_packs',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=200), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('recipient_name', sa.String(length=100), nullable=True),
        sa.Column('share_code', sa.String(length=8), nullable=False),
        sa.Column('is_free', sa.Boolean(), nullable=True),
        sa.Column('view_count', sa.Integer(), nullable=True),
        sa.Column('download_count', sa.Integer(), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('share_code')
    )

    # Create curated_pack_tracks table
    op.create_table('curated_pack_tracks',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('curated_pack_id', sa.Integer(), nullable=False),
        sa.Column('beat_id', sa.Integer(), nullable=False),
        sa.Column('track_order', sa.Integer(), nullable=True),
        sa.Column('added_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['beat_id'], ['beats.id'], ),
        sa.ForeignKeyConstraint(['curated_pack_id'], ['curated_packs.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('curated_pack_id', 'beat_id', name='unique_curated_pack_beat')
    )


def downgrade():
    op.drop_table('curated_pack_tracks')
    op.drop_table('curated_packs')
    op.drop_table('user_liked_tracks')
