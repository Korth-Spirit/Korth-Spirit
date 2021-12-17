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
from typing import Type, Union

from . import aw_bool, aw_data, aw_float, aw_int, aw_string
from .attribute import AttributeEnum


def get_data(attribute: AttributeEnum, type: Type) -> Union[int, float, bool, str]:
    """
    Gets a data attribute.

    Args:
        attribute (AttributeEnum): The attribute name.
        type (Type): The type of the attribute.

    Raises:
        Exception: If the attribute could not be retrieved.

    Returns:
        Union[int, float, bool, str, bytes]: The attribute value.
    """
    switcher = {
        int: aw_int,
        str: aw_string,
        bool: aw_bool,
        float: aw_float,
        bytes: aw_data
    }

    return switcher[type](attribute)
