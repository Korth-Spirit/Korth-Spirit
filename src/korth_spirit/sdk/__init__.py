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
from ctypes import (CDLL, CFUNCTYPE, POINTER, byref, c_char, c_char_p, c_int,
                    c_uint, c_ulong, c_void_p)
from dataclasses import fields
from os import path
from typing import List, Optional, Union

from ..data import (AddressData, BotMenuData, CameraSetData, CavChangeData,
                    CavDeleteData, CellIteratorData, LoginData,
                    ObjectChangeData, ObjectCreateData, ObjectCreatedData,
                    ObjectDeleteData, StateChangeData)
from .enums import (AttributeEnum, CallBackEnum, CameraEnum, EventEnum,
                    RightsEnum)

SDK_FILE = './aw64.dll'
SDK = CDLL(SDK_FILE)
AW_BUILD = 134 # AW 7.0
AW_CALLBACK = CFUNCTYPE(None)

def aw_int_set(attribute: AttributeEnum, value: int) -> None:
    """
    Sets an initialization attribute.

    Args:
        AttributeEnum (AttributeEnum): The attribute name.
        value (int): The attribute value.

    Raises:
        Exception: If the attribute could not be set.
    """
    rc = SDK.aw_int_set(attribute.value, value)

    if rc:
        raise Exception(f"Failed to set initialization attribute: {rc}")

def aw_string_set(attribute: AttributeEnum, value: str) -> None:
    """
    Sets an initialization attribute.

    Args:
        attribute (AttributeEnum): The attribute name.
        value (str): The attribute value.

    Raises:
        Exception: If the attribute could not be set.
    """
    rc = SDK.aw_string_set(attribute.value, value.encode('utf-8'))

    if rc:
        raise Exception(f"Failed to set initialization attribute: {rc}")

def aw_address(session_id: int) -> AddressData:
    """
    Returns the IP address of the provided session.

    Args:
        session_id (int): The session ID to get the IP address of.

    Returns:
        AddressData: The IP address of the session.
    """
    rc = SDK.aw_address(session_id)

    if rc != 0:
        raise Exception(f'Failed to get the IP address of the session. Error code: {rc}')

    return AddressData(
        aw_int(AttributeEnum.AW_AVATAR_SESSION.value),
        aw_int(AttributeEnum.AW_AVATAR_ADDRESS.value)
    )

def aw_avatar_click(session_id: int) -> None:
    """
    Sends a click event to the avatar. Simulates a left click.
    AW_EVENT_AVATAR_CLICK is triggered.

    Args:
        session_id (int): The session ID of the avatar to click.
    """
    rc = SDK.aw_avatar_click(session_id)

    if rc != 0:
        raise Exception(f'Failed to click the avatar. Error code: {rc}')

def aw_avatar_location(
    citizen: Optional[int] = None,
    session: Optional[int] = None,
    name: Optional[str] = None
) -> None:
    """
    Queries the location of an avatar.
    Returns the location via the callback.
    Only one of these parameters can be specified.

    Args:
        citizen (Optional[int], optional): The citizen ID. Defaults to None.
        session (Optional[int], optional): The session ID. Defaults to None.
        name (Optional[str], optional): The name of the avatar. Defaults to None.

    Raises:
        Exception: If the location could not be queried.
    """
    rc = SDK.aw_avatar_location(
        citizen,
        session,
        name.encode('utf-8') if name else None
    )

    if rc:
        raise Exception(f"Failed to query avatar location: {rc}")

def aw_avatar_reload(citizen: int = 0, session: int = 0) -> None:
    """
    If the avatar exists and call was successful send AW_EVENT_AVATAR_RELOAD to all users in the world.
    Only one of the parameters can be set to a non-zero/non-null value. 

    Args:
        citizen (int, optional): The citizen ID to reload the avatar of. Defaults to 0.
        session (int, optional): The session ID to reload the avatar of. Defaults to 0.
    """
    if citizen is None and session is None:
        raise Exception('One of the parameters must be set to a non-zero/non-null value.')

    rc = SDK.aw_avatar_reload(citizen, session)

    if rc != 0:
        raise Exception(f'Failed to reload the avatar. Error code: {rc}')

def aw_avatar_set(session_id: int) -> None:
    """
    Sets the avatar with the provided session ID.

    Args:
        session_id (int): The session ID of the avatar to set.
    """
    rc = SDK.aw_avatar_set(session_id)

    if rc != 0:
        raise Exception(f'Failed to set the avatar. Error code: {rc}')

def aw_bool(attribute: AttributeEnum) -> bool:
    """
    Returns the value of a boolean attribute

    Args:
        attribute (AttributeEnum): The attribute to get the value of.

    Returns:
        bool: The value of the attribute.
    """
    return bool(SDK.aw_bool(attribute.value))

def aw_bool_set(attribute: AttributeEnum, value: bool) -> None:
    """
    Sets an initialization attribute.

    Args:
        attribute (AttributeEnum): The attribute name.
        value (bool): The attribute value.

    Raises:
        Exception: If the attribute could not be set.
    """
    rc = SDK.aw_bool_set(attribute.value, value)

    if rc:
        raise Exception(f"Failed to set initialization attribute: {rc}")

def aw_botgram_send(text: str, citizen: int) -> None:
    """
    Sends a botgram to the bots of the provided citizen.
    
    Args:
        text (str): The text to send.
        citizen (int): The citizen ID to send the botgram to.
    """
    aw_string_set(AttributeEnum.AW_BOTGRAM_TEXT, text)
    aw_int_set(AttributeEnum.AW_BOTGRAM_TO, citizen)

    rc = SDK.aw_botgram_send()

    if rc != 0:
        raise Exception(f'Failed to send the botgram. Error code: {rc}')

def aw_botmenu_send(data: BotMenuData) -> None:
    """
    Builds and sends a botmenu to the defined session.

    Raises:
        Exception: If the botmenu could not be sent.

    Args:
        data (BotMenuData): The botmenu data.
    """
    aw_int_set(AttributeEnum.AW_BOTMENU_TO_SESSION, data.to_session)
    aw_string_set(AttributeEnum.AW_BOTMENU_QUESTION, data.question)
    aw_string_set(AttributeEnum.AW_BOTMENU_ANSWER, data.answer)

    rc = SDK.aw_botmenu_send()
    
    if rc != 0:
        raise Exception(f'Failed to send the botmenu. Error code: {rc}')

def aw_callback(callback: CallBackEnum) -> c_void_p:
    """
    Returns the address of a callback function.

    Args:
        callback (CallBackEnum): The callback to get the address of.

    Returns:
        c_void_p: The address of the callback.
    """
    return SDK.aw_callback(callback.value)

def aw_callback_set(callback: CallBackEnum, handler: AW_CALLBACK) -> None:
    """
    Set a callback to the specified handler.

    Args:
        callback (CallBackEnum): The callback to set.
        handler (AW_CALLBACK): The callback handler.
    """
    rc = SDK.aw_callback_set(callback.value, handler)

    if rc != 0:
        raise Exception(f'Failed to set the callback. Error code: {rc}')

def aw_camera_set(session_id: int, data: CameraSetData) -> None:
    """
    Sets the camera of the specified session.

    Args:
        session_id (int): The session ID of the avatar to set the camera of.
        data (CameraSetData): The camera data.
    
    Raises:
        Exception: If the camera could not be set.
    """
    from .write_data import write_data
    for field in fields(data):
        value = getattr(data, field.name, None)
        attr = getattr(AttributeEnum, f'AW_CAMERA_{field.name.upper()}')

        if value is not None:
            write_data(attr, value)
    
    rc = SDK.aw_camera_set(session_id)

    if rc != 0:
        raise Exception(f'Failed to set the camera. Error code: {rc}')

def aw_cav_change(data: CavChangeData) -> None:
    """
    Changes the CAV of the specified citizen.

    Args:
        data (CavChangeData): The CAV change data.

    Raises:
        Exception: If the CAV could not be changed.
    """
    aw_int_set(AttributeEnum.AW_CAV_CITIZEN, data.citizen)
    aw_int_set(AttributeEnum.AW_CAV_SESSION, data.session)
    aw_data_set(AttributeEnum.AW_CAV_DEFINITION, data.definition)

    rc = SDK.aw_cav_change()

    if rc != 0:
        raise Exception(f'Failed to change the CAV. Error code: {rc}')
    
def aw_cav_delete(data: CavDeleteData) -> None:
    """
    Deletes the CAV of the specified citizen.

    Args:
        data (CavDeleteData): The CAV delete data.

    Raises:
        Exception: If the CAV could not be deleted.
    """
    aw_int_set(AttributeEnum.AW_CAV_CITIZEN, data.citizen)
    aw_int_set(AttributeEnum.AW_CAV_SESSION, data.session)

    rc = SDK.aw_cav_delete()

    if rc != 0:
        raise Exception(f'Failed to delete the CAV. Error code: {rc}')

def aw_cav_request(citizen: int, session: int) -> None:
    """
    Queries the universe for the CAV of the specified citizen.

    Args:
        citizen (int): The citizen ID to query the CAV of.
        session (int): The session ID to query the CAV of.

    Raises:
        Exception: If the CAV could not be requested.
    """    
    rc = SDK.aw_cav_request(citizen, session)

    if rc != 0:
        raise Exception(f'Failed to request the CAV. Error code: {rc}')

def aw_cell_next(combine: bool = False, iterator: CellIteratorData = None) -> None:
    """
    Queries the next cell in the cell iterator.
    If combine is set to true this call will batch multiple cells.
    A specific cell can be set by setting the iterator to zero and z and x cell coordinates.

    Args:
        combine (bool, optional): Whether to combine multiple cells. Defaults to False.
        iterator (CellIteratorData, optional):  The cell iterator. Defaults to None.

    Raises:
        Exception: If the cell could not be queried.
    """    
    if iterator:
        aw_int_set(AttributeEnum.AW_CELL_ITERATOR, iterator.iterator)

    aw_bool_set(AttributeEnum.AW_CELL_COMBINE, combine)
    rc = SDK.aw_cell_next()

    if rc != 0:
        raise Exception(f'Failed to get the next cell. Error code: {rc}')

def aw_check_right(citizen: int, right: str) -> bool:
    """
    Checks if the citizen has the specified right.

    Args:
        citizen (int): The citizen number to check the right of.
        right (str): A rights list.
            0    ... tourists
            any# ... citizen number
            -    ... exclusion sign
            #~#  ... citizen range
            *    ... everyone
            , blank  ... delimiters

    Example:
        "1~2300,-512~1024" 
            Grants rights to 1 to 2300
            Deny rights to 512 to 1024.

    Returns:
        bool: True if the citizen has the right, False otherwise.
    """ 
    SDK.aw_check_right.argtypes = [c_int, c_char_p]
    SDK.aw_check_right.restype = c_int

    return bool(SDK.aw_check_right(citizen, right))

def aw_check_right_all(right: str) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_citizen_add() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_citizen_attributes_by_name(name: str) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_citizen_attributes_by_number(citizen: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_citizen_change() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_citizen_delete(citizen: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_citizen_next() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_citizen_previous() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_console_message(session_id: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_create(
    domain: str = "auth.activeworlds.com",
    port: int = 6670
) -> c_void_p:
    """
    Creates a bot instance for the specified domain and port.

    Args:
        domain (str): The universe domain. Defaults to "auth.activeworlds.com".
        port (int): The universe port. Defaults to 6670.

    Raises:
        Exception: If the bot instance could not be created.

    Returns:
        c_void_p: The bot instance.
    """
    instance = c_void_p()
    rc = SDK.aw_create(domain.encode('utf-8'), port, byref(instance))
    
    if rc:
        raise Exception(f"Failed to create bot instance: {rc}")

    return instance

def aw_create_resolved(address: int, port: int) -> None:
    raise NotImplementedError('This function is not implemented yet.')

def aw_data(attribute: AttributeEnum, ret_type = c_char) -> Union[bytes, list[bytes]]:
    """
    Gets a data attribute.

    Args:
        attribute (AttributeEnum): The attribute name.
        ret_type (c_char, optional): The return type. Defaults to c_char.

    Raises:
        Exception: If the attribute could not be retrieved.

    Returns:
        Union[bytes, list[bytes]]: The attribute value.
    """
    SDK.aw_data.restype = POINTER(ret_type)
    SDK.aw_data.argtypes = [c_int, POINTER(c_uint)]
    data_length = c_uint()

    data_p = SDK.aw_data(attribute.value, byref(data_length))

    if data_length.value == 1:
        return data_p
        
    return [data_p[i] for i in range(data_length.value)]
    

def aw_data_set(attribute: AttributeEnum, value: bytes) -> None:
    """
    Sets a data attribute.

    Args:
        attribute (AttributeEnum): The attribute name.
        value (bytes): The attribute value.

    Raises:
        Exception: If the attribute could not be set.
    """
    SDK.aw_data_set.restype = c_int
    SDK.aw_data_set.argtypes = [c_int, c_char_p, c_uint]

    length = len(value) if value else 0

    rc = SDK.aw_data_set(attribute.value, value, length)

    if rc:
        raise Exception(f"Failed to set data attribute: {rc}")

def aw_delete_all_objects() -> None:
    """
    Deletes all objects in a world.
    """
    SDK.aw_delete_all_objects.restype = c_int
    SDK.aw_delete_all_objects.argtypes = []

    SDK.aw_delete_all_objects()   

def aw_destroy(instance: c_void_p) -> None:
    """
    Destroys a bot instance.

    Args:
        instance (c_void_p): The bot instance.
    """
    rc = SDK.aw_destroy(instance)

    if rc:
        raise Exception(f"Failed to destroy bot instance: {rc}")

def aw_enter(world: str) -> None:
    """
    Enters the universe at a specified world.

    Args:
        name (str): The name of the world.

    Raises:
        Exception: If the world could not be entered.
    """
    rc = SDK.aw_enter(world.encode('utf-8'))

    if rc:
        raise Exception(f"Failed to enter universe: {rc}")

def aw_event(event: EventEnum) -> None:
    raise NotImplementedError('This function is not implemented yet.')

def aw_event_set(event: EventEnum, handler: AW_CALLBACK) -> None:
    """
    Sets an event handler.

    Args:
        event (Event): The event.
        handler (AW_CALLBACK): The event handler.

    Raises:
        Exception: If the event handler could not be set.
    """
    rc = SDK.aw_event_set(event.value, handler)

    if rc:
        raise Exception(f"Failed to set event handler: {rc}, {event}")

def aw_exit() -> None:
    """
    Exits the world.

    Raises:
        Exception: If the world could not be exited.
    """
    rc = SDK.aw_exit()

    if rc:
        raise Exception(f"Failed to exit world: {rc}")

def aw_float(attribute: AttributeEnum) -> float:
    """
    Gets a float attribute.

    Args:
        attribute (AttributeEnum): The attribute name.

    Raises:
        Exception: If the attribute could not be retrieved.

    Returns:
        float: The attribute value.
    """
    return float(SDK.aw_float(attribute.value))

def aw_float_set(attribute: AttributeEnum, value: float) -> None:
    """
    Sets an initialization attribute.

    Args:
        attribute (AttributeEnum): The attribute name.
        value (float): The attribute value.

    Raises:
        Exception: If the attribute could not be set.
    """
    rc = SDK.aw_float_set(attribute.value, value)

    if rc:
        raise Exception(f"Failed to set initialization attribute: {rc}")

def aw_has_world_right(citizen: int, right: RightsEnum) -> bool:
    """
    Checks if a citizen has a specified world right.

    Args:
        citizen (int): The citizen number.
        right (RightsEnum): The right.

    Returns:
        bool: True if the citizen has the right, False otherwise.
    """    
    return SDK.aw_has_world_right(citizen, right.value)

def aw_has_world_right_all(right: AttributeEnum) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_hud_clear(session: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_hud_click() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_hud_create() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_hud_destroy(session: int, id: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_init(build: int) -> None:
    """
    Initializes the Active Worlds Software Development Kit.

    Args:
        build (int): The build number of the SDK.

    Returns:
        int: The result of the initialization.

    Raises:
        Exception: If the initialization fails.

    See:
        http://wiki.activeworlds.com/index.php?title=SDK_Reason_Codes
    """
    rc = SDK.aw_init(build)

    if rc:
        raise Exception(f"Failed to initialize SDK: {rc}")

def aw_init_bind(build: int, long: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_instance() -> None:
    raise NotImplementedError('This function is not implemented yet.')

def aw_instance_callback_set(c: AW_CALLBACK, callback: c_void_p, rc: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_instance_event_set(event: EventEnum, handler: c_void_p) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_instance_set(instance: c_void_p) -> None:
    """
    Sets the bot instance.

    Args:
        instance (c_void_p): The bot instance.

    Raises:
        Exception: If the instance could not be set.
    """
    rc = SDK.aw_instance_set(instance)

    if rc:
        raise Exception(f"Failed to set instance: {rc}")

def aw_int(attribute: AttributeEnum) -> int:
    """
    Gets an integer attribute.

    Args:
        attribute (AttributeEnum): The attribute name.

    Raises:
        Exception: If the attribute could not be retrieved.

    Returns:
        int: The attribute value.
    """
    return int(SDK.aw_int(attribute.value))

def aw_laser_beam() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_license_add() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_license_attributes(name: str) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_license_change() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_license_delete(name: str) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_license_next() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_license_previous() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_login(instance: c_void_p, data: LoginData) -> None:
    """
    Logs into the universe.

    Args:
        instance (c_void_p): The bot instance.
        data (LoginData): The login data.

    Raises:
        Exception: If the login failed.
    """
    aw_instance_set(instance)

    aw_int_set(AttributeEnum.AW_LOGIN_OWNER, data.citizen)
    aw_string_set(AttributeEnum.AW_LOGIN_PRIVILEGE_PASSWORD, data.password)
    aw_string_set(AttributeEnum.AW_LOGIN_APPLICATION, data.app_name)
    aw_string_set(AttributeEnum.AW_LOGIN_NAME, data.bot_name)
    
    rc = SDK.aw_login()

    if rc:
        raise Exception(f"Failed to login: {rc}")

def aw_mover_links(id: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_mover_rider_add(id: int, session: int, dist: int, angle: int, y_delta: int, yaw_delta: int, pitch_delta: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_mover_rider_change(id: int, session: int, dist: int, angle: int, y_delta: int, yaw_delta: int, pitch_delta: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_mover_rider_delete(id: int, session: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_mover_set_position(id: int, x: int, y: int, z: int, yaw: int, pitch: int, roll: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_mover_set_state(id: int, state: int, model_num: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_noise(session_id: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_object_add(data: ObjectCreateData) -> ObjectCreatedData:
    """
    Creates an object.

    Args:
        data (ObjectCreateData): The object data.

    Returns:
        ObjectCreatedData: The created object data.
    """
    from .get_data import get_data
    from .write_data import write_data

    for field in fields(data):
        value = getattr(data, field.name, None)
        attr = getattr(AttributeEnum, f'AW_OBJECT_{field.name.upper()}')
        write_data(attr, value)

    rc = SDK.aw_object_add()

    if rc:
        raise Exception(f"Failed to create object: {rc}")

    ret = ObjectCreatedData()
    for field in fields(ret):
        prepend = 'AW_OBJECT_'
        if 'CELL' in field.name.upper():
            prepend = 'AW_'
        attr = getattr(AttributeEnum, f'{prepend}{field.name.upper()}')
        data = get_data(attr)

        if data:
            setattr(ret, field.name, data)

    return ret

def aw_object_bump() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_object_change(data: ObjectChangeData) -> None:
    """
    Changes an object.

    Args:
        data (ObjectChangeData): The object data.

    Raises:
        Exception: If the object could not be changed.
        Exception: If the change data has an unsupported type.
    """
    from .write_data import write_data

    for field in fields(data):
        value = getattr(data, field.name, None)
        attr = getattr(AttributeEnum, f'AW_OBJECT_{field.name.upper()}')
        write_data(attr, value)

    rc = SDK.aw_object_change()

    if rc:
        raise Exception(f"Failed to change object: {rc}")

def aw_object_click() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_object_delete(data: ObjectDeleteData) -> None:
    """
    Deletes an object.

    Args:
        data (ObjectDeleteData): The object data.

    Raises:
        Exception: If the object could not be deleted.
    """
    from .write_data import write_data

    for field in fields(data):
        value = getattr(data, field.name, None)
        attr = getattr(AttributeEnum, f'AW_OBJECT_{field.name.upper()}')
        if value:
            write_data(attr, value)

    rc = SDK.aw_object_delete()

    if rc:
        raise Exception(f"Failed to delete object: {rc}")

def aw_object_load() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_object_query() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_object_select() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_query(x_sector: int, z_sector: int, sequence3_x_3: List[List[int]]) -> None:
    """
    Queries the world using longitude and latitude.

    Args:
        x_sector (int): The longitude sector.
        z_sector (int): The latitude sector.
        sequence3_x_3 (List[List[int]]): The sequence of 3 x 3 cells.

    Raises:
        Exception: If the query failed.
        Exception: If the sequence is invalid.
    """
    if len(sequence3_x_3) != 3:
        raise Exception("The sequence must be 3 x 3.")

    for row in sequence3_x_3:
        if len(row) != 3:
            raise Exception("The sequence must be 3 x 3.")
    
    sequence = (c_int * 9)(*[x for row in sequence3_x_3 for x in row])
    SDK.aw_query.argtypes = [c_int, c_int, (c_int * 9)]
    SDK.aw_query.restype = c_int
    rc = SDK.aw_query(x_sector, z_sector, sequence)

    if rc:
        raise Exception(f"Failed to query: {rc}")

def aw_query_5x5(x_sector: int, z_sector: int, sequence5_x_5: list) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_random() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_say(message: str) -> None:
    """
    Sends a message to the universe.

    Args:
        message (str): The message to send.

    Raises:
        Exception: If the message could not be sent.
    """
    rc = SDK.aw_say(message.encode('utf-8'))

    if rc:
        raise Exception(f"Failed to send message: {rc}")

def aw_sector_from_cell(cell: int) -> int:
    """
    Get the sector that a cell is located in.

    Args:
        cell (int): The cell.
    """
    SDK.aw_sector_from_cell.argtypes = [c_int]
    SDK.aw_sector_from_cell.restype = c_int
    
    return SDK.aw_sector_from_cell(cell)

def aw_server_admin(domain: str, port: int, password: str, instance: c_void_p) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_server_world_add() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_server_world_change(id: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_server_world_delete(id: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_server_world_instance_add(id: int, instance_id: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_server_world_instance_delete(id: int, instance_id: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_server_world_instance_set(id: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_server_world_list() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_server_world_set(id: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_server_world_start(id: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_server_world_stop(id: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_session() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_state_change(instance: c_void_p, data: StateChangeData) -> None:
    """
    Informs the world server of your avatar's current state.

    Args:
        instance (c_void_p): The bot instance.
        data (StateChangeData): The state change data.

    Raises:
        Exception: If the state change failed.
    """
    aw_instance_set(instance)
    
    for field in fields(data):
        value = getattr(data, field.name, None)
        attr = getattr(AttributeEnum, f'AW_MY_{field.name.upper()}')
        if value:
            aw_int_set(attr, value)

    rc = SDK.aw_state_change()

    if rc:
        raise Exception(f"Failed to check state change: {rc}")

def aw_string(attribute: AttributeEnum) -> str:
    """
    Gets a string attribute.

    Args:
        attribute (AttributeEnum): The attribute name.

    Raises:
        Exception: If the attribute could not be retrieved.

    Returns:
        str: The attribute value.
    """
    SDK.aw_string.restype = c_char_p
    return SDK.aw_string(attribute.value).decode('utf-8')

def aw_string_from_unicode(the_string: str) -> str:
    raise NotImplementedError('This function is not implemented yet.')

def aw_string_set_MBCS_codepage(codepage: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_string_to_unicode(the_string: str) -> None:
    raise NotImplementedError('This function is not implemented yet.')

def aw_teleport(session_id: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_term() -> None:
    """
    Terminates the Active Worlds Software Development Kit.
    """    
    SDK.aw_term()

def aw_terrain_delete_all() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_terrain_load_node() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_terrain_next() -> bool:
    """
    Gets the next terrain node.

    Raises:
        Exception: If an error occured.

    Returns:
        bool: True if completed, False if not.
    """
    aw_int_set(
        AttributeEnum.AW_TERRAIN_VERSION_NEEDED,
        2
    )

    SDK.aw_terrain_next.restype = c_int
    rc = SDK.aw_terrain_next()

    if rc:
        raise Exception(f"Failed to get next terrain: {rc}")

    return aw_bool(AttributeEnum.AW_TERRAIN_COMPLETE)

def aw_terrain_query(page_x: int, page_z: int, sequence: int) -> bool:
    """
    Queries the terrain for the specified page.

    Args:
        page_x (int): The page's X coordinate.
        page_z (int): The page's Z coordinate.
        sequence (int): The sequence number.

    Raises:
        Exception: If the terrain query failed.

    Returns:
        bool: True if the terrain query has completed, False otherwise.
    """
    SDK.aw_terrain_query.argtypes = [c_int, c_int, c_ulong]
    SDK.aw_terrain_query.restype = c_int
    
    rc = SDK.aw_terrain_query(page_x, page_z, sequence)

    if rc:
        raise Exception(f"Failed to query terrain: {rc}")

    return aw_bool(AttributeEnum.AW_TERRAIN_COMPLETE)

def aw_terrain_set(cell_x: int, cell_z: int, count: int, texture: int, *heights: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_tick() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_toolbar_click() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_traffic_count(traffic_in: int, traffic_out: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_universe_attributes_change() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_universe_ejection_add() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_universe_ejection_delete(address: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_universe_ejection_lookup() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_universe_ejection_next() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_universe_ejection_previous() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_unzip() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_url_click(url: str) -> None:
    raise NotImplementedError('This function is not implemented yet.')

def aw_url_send(session_id: int, url: str, target: str)-> None:
    raise NotImplementedError('This function is not implemented yet.')

def aw_user_data() -> None:
    raise NotImplementedError('This function is not implemented yet.')

def aw_user_data_set(data: bytes) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_user_list() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_wait(milliseconds: int = -1) -> None:
    """
    Waits for a specified amount of time.
    Negative 1 is infinite.

    Args:
        milliseconds (int, optional): The amount of time to wait in milliseconds. Defaults to -1.

    Raises:
        Exception: If the wait failed.
    """    
    rc = SDK.aw_wait(milliseconds)

    if rc:
        raise Exception(f"Failed to wait: {rc}")

def aw_whisper(session_id: int, message: str) -> None:
    """
    Whispers a message to a specified session.

    Args:
        session_id (int): The session to whisper to.
        message (str): The message to whisper.
    """
    rc = SDK.aw_whisper(session_id, message.encode('utf-8'))

    if rc:
        raise Exception(f"Failed to send whisper: {rc}")

def aw_world_attribute_get(attribute: int) -> Union[bool, str]:
    """
    Gets a world attribute.

    Args:
        attribute (int): The attribute to get. These attributes aren't documented.

    Raises:
        Exception: If the attribute could not be retrieved.

    Returns:
        Union[bool, str]: Read Only, The attribute value.
    """    
    SDK.aw_world_attribute_get.argtypes = [c_int, POINTER(c_int), c_char_p]

    read_only = c_int()
    value = c_char_p()
    rc = SDK.aw_world_attribute_get(attribute, read_only, value.encode('utf-8'))

    if rc:
        raise Exception(f"Failed to get world attribute: {rc}")

    return bool(read_only), value.decode('utf-8')

def aw_world_attribute_set(attribute: int, value: str) -> None:
    """
    Sets a world attribute.
    
    Args:
        attribute (int): The attribute to set. These attributes aren't documented.
        value (str): The attribute value.
    """
    rc = SDK.aw_world_attribute_set(attribute, value.encode('utf-8'))

    if rc:
        raise Exception(f"Failed to set world attribute: {rc}")

def aw_world_attributes_change() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_world_attributes_reset() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_world_attributes_send(session_id: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_world_cav_change() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_world_cav_delete() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_world_cav_request(citizen: int, session: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_world_eject() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_world_ejection_add() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_world_ejection_delete() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_world_ejection_lookup() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_world_ejection_next() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_world_ejection_previous() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_world_instance_get(citizen: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_world_instance_set(citizen: int, id: int) -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_world_list() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_world_reload_registry() -> int:
    raise NotImplementedError('This function is not implemented yet.')

def aw_zip() -> int:
    raise NotImplementedError('This function is not implemented yet.')
