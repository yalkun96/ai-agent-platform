"""Align agents table with the provider-based ORM model.

Revision ID: f6d2a7b91c40
Revises: d800ed353b09
Create Date: 2026-10-13
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = "f6d2a7b91c40"
down_revision: Union[str, None] = "d800ed353b09"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    provider_enum = postgresql.ENUM(
        "OpenAI", "Anthropic", "Google", name="aiprovider"
    )
    provider_enum.create(bind, checkfirst=True)

    op.add_column("agents", sa.Column("provider", provider_enum, nullable=True))
    op.add_column("agents", sa.Column("model_name", sa.String(), nullable=True))
    op.add_column(
        "agents",
        sa.Column(
            "temperature",
            sa.Float(),
            nullable=False,
            server_default=sa.text("0.7"),
        ),
    )
    op.add_column(
        "agents",
        sa.Column(
            "max_tokens",
            sa.Integer(),
            nullable=False,
            server_default=sa.text("256"),
        ),
    )
    op.add_column(
        "agents",
        sa.Column(
            "is_active",
            sa.Boolean(),
            nullable=False,
            server_default=sa.text("true"),
        ),
    )

    # Backfill the new columns before making them non-nullable.
    op.execute(
        """
        UPDATE agents
        SET
            provider = CASE model::text
                WHEN 'GPT_5' THEN 'OpenAI'::aiprovider
                WHEN 'CLAUDE' THEN 'Anthropic'::aiprovider
                WHEN 'GEMINI' THEN 'Google'::aiprovider
                ELSE 'OpenAI'::aiprovider
            END,
            model_name = CASE model::text
                WHEN 'GPT_5' THEN 'gpt-5'
                WHEN 'CLAUDE' THEN 'claude'
                WHEN 'GEMINI' THEN 'gemini'
                ELSE lower(model::text)
            END
        """
    )

    op.alter_column("agents", "provider", nullable=False)
    op.alter_column("agents", "model_name", nullable=False)
    op.drop_column("agents", "model")
    postgresql.ENUM(name="aimodel").drop(bind, checkfirst=True)


def downgrade() -> None:
    bind = op.get_bind()
    legacy_enum = postgresql.ENUM("GPT_5", "CLAUDE", "GEMINI", name="aimodel")
    legacy_enum.create(bind, checkfirst=True)

    op.add_column("agents", sa.Column("model", legacy_enum, nullable=True))
    op.execute(
        """
        UPDATE agents
        SET model = CASE provider::text
            WHEN 'OpenAI' THEN 'GPT_5'::aimodel
            WHEN 'Anthropic' THEN 'CLAUDE'::aimodel
            WHEN 'Google' THEN 'GEMINI'::aimodel
            ELSE 'GPT_5'::aimodel
        END
        """
    )
    op.alter_column("agents", "model", nullable=False)

    op.drop_column("agents", "provider")
    op.drop_column("agents", "model_name")
    op.drop_column("agents", "temperature")
    op.drop_column("agents", "max_tokens")
    op.drop_column("agents", "is_active")
    postgresql.ENUM(name="aiprovider").drop(bind, checkfirst=True)
