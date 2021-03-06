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
from typing import Dict, Tuple, Type


class AggregateConfiguration:
    def __init__(self, configurations: Dict[Type, Tuple]) -> None:
        """
        Initializes a new instance of the AggregateConfiguration class.
        Configurations that use files that are not found are ignored.

        Args:
            configurations (Dict[Type, Tuple]): The configurations in order of priority.
        """
        self._configurations = set()

        for c_type, c_args in configurations.items():
            try:
                self._configurations.add(c_type(*c_args))
            except FileNotFoundError:
                pass

    def get_bot_name(self) -> str:
        """
        Returns the name of the bot.

        Raises:
            KeyError: No configuration has a bot name.

        Returns:
            str: The name of the bot.
        """
        for configuration in self._configurations:
            try:
                return configuration.get_bot_name()
            except KeyError:
                pass

        raise KeyError("No configuration has a bot name.")

    def get_citizen_number(self) -> int:
        """
        Returns the citizen number of the owner of the bot.

        Raises:
            KeyError: No configuration has a citizen number.

        Returns:
            int: The citizen number of the owner of the bot.
        """
        for configuration in self._configurations:
            try:
                return configuration.get_citizen_number()
            except KeyError:
                pass
            except TypeError:
                pass

        raise KeyError("No configuration has a citizen number.")

    def get_password(self) -> str:
        """
        Returns the priviledge password of the owner of the bot.

        Raises:
            KeyError: No configuration has a password.

        Returns:
            str: The priviledge password of the owner of the bot.
        """
        for configuration in self._configurations:
            try:
                return configuration.get_password()
            except KeyError:
                pass

        raise KeyError("No configuration has a password.")

    def get_world_name(self) -> str:
        """
        Returns the name of the world the bot will enter.

        Raises:
            KeyError: No configuration has a world name.

        Returns:
            str: The name of the world the bot will enter.
        """
        for configuration in self._configurations:
            try:
                return configuration.get_world_name()
            except KeyError:
                pass

        raise KeyError("No configuration has a world name.")

    def get_world_coordinates(self) -> tuple:
        """
        Returns the coordinates of the world the bot will enter.

        Raises:
            KeyError: No configuration has world coordinates.

        Returns:
            tuple: The coordinates where the bot will enter.
        """
        for configuration in self._configurations:
            try:
                return configuration.get_world_coordinates()
            except KeyError:
                pass
            except TypeError:
                pass

        raise KeyError("No configuration has world coordinates.")

    def get_plugin_path(self) -> str:
        """
        Returns the path where the plugins are stored.

        Raises:
            KeyError: No configuration has a plugin path.

        Returns:
            str: The path where the plugins are stored.
        """
        for configuration in self._configurations:
            try:
                return configuration.get_plugin_path()
            except KeyError:
                pass

        raise KeyError("No configuration has a plugin path.")
