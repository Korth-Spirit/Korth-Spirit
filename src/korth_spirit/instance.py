# Copyright (c) 2021-2022 Johnathan P. Irvin
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from dataclasses import dataclass, field
from typing import Any, List

from .avatar import Avatar
from .coords import Coordinates
from .events import EventBus
from .query import QueryEnum, QueryFactory
from .sdk import (EventEnum, aw_create, aw_destroy, aw_enter, aw_instance_set,
                  aw_login, aw_say, aw_state_change, aw_whisper)


@dataclass
class Instance:
    name: str
    coords: Coordinates
    _coords: Coordinates = field(init=False, repr=False, default=Coordinates(0, 0, 0))
    bus: EventBus = field(init=False, repr=False, default_factory=EventBus)

    @property
    def coords(self) -> Coordinates:
        """
        Get the coordinates of the instance.

        Returns:
            Coordinates: The coordinates of the instance.
        """
        return self._coords

    @coords.setter
    def coords(self, coords: Coordinates) -> None:
        """
        Set the coordinates of the instance.

        Args:
            coords (Coordinates): The coordinates of the instance.
        """
        from .data import StateChangeData
        
        if not hasattr(self, '_instance'):
            self._coords = coords
            return
    
        aw_state_change(self._instance, StateChangeData(
            x = coords.x,
            y = coords.y,
            z = coords.z
        ))
        
        self._coords = coords

    def __enter__(self) -> "Instance":
        self._instance = aw_create()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        aw_instance_set(self._instance)
        aw_destroy(self._instance)

    def login(self, citizen_number: int, password: str) -> "Instance":
        """
        Login to the universe.

        Returns:
            Instance: The instance.
        """
        from .data import LoginData

        aw_login(self._instance, LoginData(
            citizen=citizen_number,
            password=password,
            app_name=f'Python Wrapped Application #{citizen_number}',
            bot_name=self.name
        ))

        return self
    
    def enter_world(self, world_name: str) -> "Instance":
        """
        Enter the specified world.

        Args:
            world_name (str): The name of the world.

        Returns:
            Instance: The instance.
        """
        aw_instance_set(self._instance)
        aw_enter(world_name)
        return self

    def move_to(self, coords: Coordinates) -> "Instance":
        """
        Move to the specified coordinates.

        Args:
            coords (Coordinates): The coordinates.

        Returns:
            Instance: The instance.
        """
        self.coords = coords
        return self

    def say(self, message: str) -> "Instance":
        """
        Say something.

        Args:
            message (str): The message.

        Returns:
            Instance: The instance.
        """
        aw_instance_set(self._instance)
        aw_say(message)
        return self

    def whisper(self, session: int, message: str) -> "Instance":
        """
        Whisper something.

        Args:
            session (int): The session to whisper to.
            message (str): The message.

        Returns:
            Instance: The instance.
        """
        aw_instance_set(self._instance)
        aw_whisper(session, message)
        
        return self

    def query(self, query_type: QueryEnum = QueryEnum.OBJECT, **kwargs) -> List[Any]:
        """
        Make a query from the instance.

        Args:
            query_type (QueryEnum, optional): The query type. Defaults to QueryEnum.OBJECT.
            **kwargs: The query arguments.

        Returns:
            List[Any]: The query results.
        """        
        aw_instance_set(self._instance)

        return QueryFactory(self, query_type)(**kwargs)

    def get_avatar(self, citizen: int) -> Avatar:
        """
        Get the avatar for the specified citizen.

        Args:
            citizen (int): The citizen.

        Returns:
            Avatar: The avatar.
        """
        return Avatar(self, citizen)

    def subscribe(self, event: EventEnum, subscriber: callable) -> "Instance":
        """
        Subscribe to an event.

        Args:
            event (Event): The event to subscribe to.
            subscriber (callable): The subscriber to the event.

        Returns:
            Instance: The instance.
        """
        self.bus.subscribe(event, subscriber)
        return self

    def unsubscribe(self, event: EventEnum, subscriber: callable) -> "Instance":
        """
        Unsubscribe from an event.

        Args:
            event (Event): The event to unsubscribe from.
            subscriber (callable): The subscriber to the event.

        Returns:
            Instance: The instance.
        """
        self.bus.unsubscribe(event, subscriber)
        return self
