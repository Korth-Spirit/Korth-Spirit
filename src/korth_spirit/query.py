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

from .data import CellObjectData
from .events import Event
from .sdk import (AttributeEnum, CallBackEnum, EventEnum, aw_int, aw_query,
                  aw_sector_from_cell, aw_wait)


class Query:    
    def __init__(self, x: int, z: int):
        self._running = False
        self.x = x
        self.z = z
        self._objects = []
        self._sequence = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
    
    def on_cell_begin(self, event: Event):
        """
        This is the callback that is called when a cell begins.

        Args:
            event (Event): The event that was triggered.
        """        
        sector_x = aw_sector_from_cell(event.cell_X)
        sector_z = aw_sector_from_cell(event.cell_Z)

        self._sequence[sector_x][sector_z] = aw_int(AttributeEnum.AW_CELL_SEQUENCE)

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
                decription = event.object_description,
                action = event.object_action,
                data = event.object_data,
            )
        )

    def on_query_finished(self, event: Event):
        """
        This is the callback that is called when the query finishes.

        Args:
            event (Event): The event that was triggered.
        """        
        if event.query_complete:
            self._running = False
        else:
            aw_query(self.x, self.z, self._sequence)

    def run(self, instance: "Instance") -> List[CellObjectData]:
        """
        Runs the query.

        Args:
            instance (Instance): The instance to run the query on.

        Returns:
            List[CellObjectData]: The list of objects found in the 3x3 sector.
        """        
        instance.subscribe(EventEnum.AW_CELL_BEGIN, self.on_cell_begin)
        instance.subscribe(EventEnum.AW_CELL_OBJECT, self.on_receive_object)
        instance.subscribe(CallBackEnum.AW_CALLBACK_QUERY, self.on_query_finished)

        while self._running:
            aw_wait()

        instance.unsubscribe(EventEnum.AW_CELL_BEGIN, self.on_cell_begin)
        instance.unsubscribe(EventEnum.AW_CELL_OBJECT, self.on_receive_object)
        instance.unsubscribe(CallBackEnum.AW_CALLBACK_QUERY, self.on_query_finished)

        return self._objects
