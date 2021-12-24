# Copyright (c) 2021 Johnathan P. Irvin
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
from typing import Any, Iterable, Union

from .aw_object import AWObject
from .sdk import aw_instance_set
from .sdk.enums import AttributeEnum, WorldEnum
from .sdk.get_data import get_data
from .sdk.write_data import write_data
from .utilities import ceil_division


class World:
    def __init__(self, instance: "Instance") -> None:
        """
        Initialize the world object.

        Args:
            instance (Instance): The instance to initialize the world object with.
        """
        self.instance = instance

    def get_attribute(self, attribute: Union[str, WorldEnum]) -> Any:
        """
        Get a world attribute.

        Args:
            attribute (Union[str, WorldEnum]): The name of the attribute to get.

        Raises:
            AttributeError: If the attribute does not exist.

        Returns:
            Any: The value of the attribute.
        """
        if type(attribute) is str:
            try:
                attribute = WorldEnum['AW_WORLD_' + attribute.upper()]
            except KeyError:
                raise AttributeError(f"No world attribute named {attribute}")

        aw_instance_set(self.instance._instance)

        return get_data(AttributeEnum(attribute.value))

    def set_attribute(self, attribute: Union[str, WorldEnum], value: Any) -> None:
        """
        Set a world attribute.

        Args:
            attribute (Union[str, WorldEnum]): The name of the attribute to set.
            value (Any): The value to set the attribute to.

        Raises:
            AttributeError: If the attribute does not exist.
        """
        if type(attribute) is str:
            try:
                attribute = WorldEnum['AW_WORLD_' + attribute.upper()]
            except KeyError:
                raise AttributeError(f"No world attribute named {attribute}")

        
        aw_instance_set(self.instance._instance)
        write_data(AttributeEnum(attribute.value), value)

    def query(self) -> Iterable[AWObject]:
        """
        Queries the entire world. Assumes priveleges.
        It is important to remember that we're scanning sectors of 8x8 cells in a 3x3 grid.

        Returns:
            Iterable[AWObject]: A list of the objects queried.
        """
        world_size = self.get_attribute(WorldEnum.AW_WORLD_SIZE)
        scan_range = ceil_division(world_size, 8)

        for x in range(-scan_range, scan_range + 1):
            for z in range(-scan_range, scan_range + 1):
                for obj in self.instance.query(x * 8, z * 8):
                    yield AWObject.from_cell_object(obj)
