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
from korth_spirit.sdk import aw_has_world_right, aw_instance_set
from korth_spirit.sdk.enums import RightsEnum


class Avatar:
    def __init__(self, instance: "Instance", citizen: int) -> None:
        """
        Constructor of an avatar.

        Args:
            instance (Instance): The bot instance to gather information on the avatar from.
            citizen (int): The citizen number of the avatar.
        """        
        aw_instance_set(self._instance)

        for right in RightsEnum:
            setattr(
                self,
                right.name.replace('AW_WORLD_', '').lower(),
                aw_has_world_right(citizen, right.value)
            )
