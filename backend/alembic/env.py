from logging.config import fileConfig

from alembic import context
from geoalchemy2.alembic_helpers import include_object as ga_include_object
from geoalchemy2.alembic_helpers import render_item, writer
from sqlalchemy import engine_from_config, pool

from app.core.config import settings
from app.core.database import Base
from app.models import user, location, journal_entry  # noqa: F401  (register models with Base.metadata)

config = context.config
config.set_main_option("sqlalchemy.url", settings.database_url)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

# postgis/postgis ships with tiger geocoder + topology extension tables that
# aren't part of our schema. Without this filter, autogenerate proposes
# dropping them (including spatial_ref_sys) since they're not in our models.
OUR_TABLES = set(target_metadata.tables.keys())


def include_object(object, name, type_, reflected, compare_to):
    if not ga_include_object(object, name, type_, reflected, compare_to):
        return False
    if reflected:
        table = object if type_ == "table" else getattr(object, "table", None)
        if table is not None and table.name not in OUR_TABLES:
            return False
    return True


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        include_object=include_object,
        render_item=render_item,
        process_revision_directives=writer,
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_object=include_object,
            render_item=render_item,
            process_revision_directives=writer,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
