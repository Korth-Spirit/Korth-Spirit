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
from typing import List

from .data import CellIteratorData, CellObjectData
from .events import Event
from .sdk import EventEnum, aw_cell_next, aw_wait


class Query:    
    def __init__(self, x: int = None, z: int = None):
        """
        If x and z are not provided, the query will run until it fails.

        Args:
            x (int, optional): The x coordinate of the 3x3 sector. Defaults to None.
            z (int, optional): The z coordinate of the 3x3 sector. Defaults to None.
        """
        self.x = x
        self.z = z
        self._objects = []
    
    def on_receive_object(self, event: Event):
        """
        This is the callback that is called when an object is found in a cell.

        Args:
            event (Event): The event that was triggered.
        """        
        self._objects.append(
            CellObjectData(
                type = event.object_type,
                id = event.object_type,
                number = event.object_number,
                owner = event.object_owner,
                build_timestamp = event.object_build_timestamp,
                x = event.object_x,
                y = event.object_y,
                z = event.object_z,
                yaw = event.object_yaw,
                tilt = event.object_tilt,
                roll = event.object_roll,
                model = event.object_model,
                description = event.object_description,
                action = event.object_action,
                data = event.object_data,
            )
        )

    def run(self, instance: "Instance") -> List[CellObjectData]:
        """
        Runs the query.

        Args:
            instance (Instance): The instance to run the query on.

        Returns:
            List[CellObjectData]: The list of objects found in the 3x3 sector.
        """        
        instance.subscribe(EventEnum.AW_EVENT_CELL_OBJECT, self.on_receive_object)

        if self.x and self.z:
            aw_cell_next(
                combine=False,
                iterator=CellIteratorData(
                    x=self.x,
                    z=self.z,
                )
            )
            aw_wait(1)
        else:
            try:
                while True:
                    aw_cell_next(
                        combine=True,
                    )
                    aw_wait(1)
            except Exception as e:
                print(e)

        instance.unsubscribe(EventEnum.AW_EVENT_CELL_OBJECT, self.on_receive_object)

        return self._objects
