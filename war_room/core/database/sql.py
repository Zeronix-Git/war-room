from typing import Any, Dict, List

import sqlalchemy
from option import Option, Result
from sqlalchemy import Column, Float, Integer, MetaData, String, Table, create_engine
from sqlalchemy.sql import select

from war_room.core.custom_types import Match, User
from war_room.core.custom_types.interfaces import UniqueDictionaryLike
from war_room.core.database.base import UniqueDictionaryLikeDatabase


def _get_table_columns_from_schema(schema: Dict[str, Any]):
    return [Column(key, value) for key, value in schema.items()]


class SQLUniqueDictionaryLikeDatabase(UniqueDictionaryLikeDatabase[UniqueDictionaryLike]):
    def __init__(self, name: str, schema: Dict[str, Any], database_path: str, object_class: Any):
        self.engine = create_engine(f'sqlite:///{database_path}')
        self.meta = MetaData()
        self.schema = schema

        self.table = Table(
            name, self.meta, Column('uid', Integer, primary_key=True), *_get_table_columns_from_schema(schema)
        )
        self._object_class = object_class
        self.meta.create_all(self.engine)

    @property
    def _object_columns(self) -> List[Column]:
        return [col for col in self.table.columns if col.key != 'uid']

    def get(self, uid: int) -> Result[Option[UniqueDictionaryLike], str]:
        try:
            with self.engine.connect() as connection:
                command = select(self._object_columns).where(self.table.c.uid == uid)
                result = connection.execute(command)
                record = result.fetchone()

                if record is None:
                    return Result.Ok(Option.NONE())
                else:
                    dict = {key: value for key, value in zip(self.schema.keys(), record)}
                    udl = self._object_class.from_dict(dict)
                    return Result.Ok(Option.Some(udl))

        except sqlalchemy.exc.SQLAlchemyError as e:
            return Result.Err(str(e))

    def update(self, udl: UniqueDictionaryLike) -> Result[None, str]:
        return self.contains(udl.uid).map(
            lambda contains: self._update_existing(udl) if contains else self._add_new(udl)
        )

    def _add_new(self, udl: UniqueDictionaryLike) -> Result[None, str]:
        try:
            with self.engine.connect() as connection:
                command = self.table.insert().values(uid=udl.uid, **udl.to_dict())
                connection.execute(command)
            return Result.Ok(None)

        except sqlalchemy.exc.SQLAlchemyError as e:
            return Result.Err(str(e))

    def _update_existing(self, udl: UniqueDictionaryLike) -> Result[None, str]:
        try:
            with self.engine.connect() as connection:
                command = self.table.update().where(self.table.c.uid == udl.uid).values(uid=udl.uid, **udl.to_dict())
                connection.execute(command)

            return Result.Ok(None)

        except sqlalchemy.exc.SQLAlchemyError as e:
            return Result.Err(str(e))


class SQLUserDatabase(SQLUniqueDictionaryLikeDatabase):
    def __init__(self, database_path):
        return super(SQLUserDatabase, self).__init__(
            database_path=database_path,
            name='users',
            schema={'id': Integer, 'game_count': Integer, 'rating': Float},
            object_class=User,
        )


class SQLMatchDatabase(SQLUniqueDictionaryLikeDatabase):
    def __init__(self, database_path):
        return super(SQLUserDatabase, self).__init__(
            database_path=database_path,
            name='matches',
            schema={
                'id': Integer,
                'p1_user_id': Integer,
                'p2_user_id': Integer,
                'tier': Integer,
                'status': String,
            },
            object_class=Match,
        )
