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
from enum import IntEnum, auto

from .attribute import AttributeEnum


class WorldEnum(IntEnum):
    AW_WORLD_NAME = AttributeEnum.AW_WORLD_NAME.value
    AW_WORLD_TITLE = auto()
    AW_WORLD_BACKDROP = auto()
    AW_WORLD_GROUND = auto()
    AW_WORLD_OBJECT_PATH = auto()
    AW_WORLD_OBJECT_REFRESH = auto()
    AW_WORLD_BUILD_RIGHT = auto()
    AW_WORLD_EMINENT_DOMAIN_RIGHT = auto()
    AW_WORLD_ENTER_RIGHT = auto()
    AW_WORLD_SPECIAL_OBJECTS_RIGHT = auto()
    AW_WORLD_FOG_RED = auto()
    AW_WORLD_FOG_GREEN = auto()
    AW_WORLD_FOG_BLUE = auto()
    AW_WORLD_CARETAKER_CAPABILITY = auto()
    AW_WORLD_RESTRICTED_RADIUS = auto()
    AW_WORLD_PUBLIC_SPEAKER_CAPABILITY = auto()
    AW_WORLD_PUBLIC_SPEAKER_RIGHT = auto()
    AW_WORLD_CREATION_TIMESTAMP = auto()
    AW_WORLD_HOME_PAGE = auto()
    AW_WORLD_BUILD_NUMBER = auto()
    AW_WORLD_OBJECT_PASSWORD = auto()
    AW_WORLD_DISABLE_CREATE_URL = auto()
    AW_WORLD_RATING = auto()
    AW_WORLD_WELCOME_MESSAGE = auto()
    AW_WORLD_EJECT_RIGHT = auto()
    AW_WORLD_EJECT_CAPABILITY = auto()
    AW_WORLD_CELL_LIMIT = auto()
    AW_WORLD_BUILD_CAPABILITY = auto()
    AW_WORLD_ALLOW_PASSTHRU = auto()
    AW_WORLD_ALLOW_FLYING = auto()
    AW_WORLD_ALLOW_TELEPORT = auto()
    AW_WORLD_ALLOW_OBJECT_SELECT = auto()
    AW_WORLD_BOTS_RIGHT = auto()
    AW_WORLD_SPEAK_CAPABILITY = auto()
    AW_WORLD_SPEAK_RIGHT = auto()
    AW_WORLD_ALLOW_TOURIST_WHISPER = auto()
    AW_WORLD_LIGHT_X = auto()
    AW_WORLD_LIGHT_Y = auto()
    AW_WORLD_LIGHT_Z = auto()
    AW_WORLD_LIGHT_RED = auto()
    AW_WORLD_LIGHT_GREEN = auto()
    AW_WORLD_LIGHT_BLUE = auto()
    AW_WORLD_AMBIENT_LIGHT_RED = auto()
    AW_WORLD_AMBIENT_LIGHT_GREEN = auto()
    AW_WORLD_AMBIENT_LIGHT_BLUE = auto()
    AW_WORLD_ALLOW_AVATAR_COLLISION = auto()
    AW_WORLD_FOG_ENABLE = auto()
    AW_WORLD_FOG_MINIMUM = auto()
    AW_WORLD_FOG_MAXIMUM = auto()
    AW_WORLD_FOG_TINTED = auto()
    AW_WORLD_MAX_USERS = auto()
    AW_WORLD_SIZE = auto()
    AW_WORLD_OBJECT_COUNT = auto()
    AW_WORLD_EXPIRATION = auto()
    AW_WORLD_SPECIAL_COMMANDS_RIGHT = auto()
    AW_WORLD_MAX_LIGHT_RADIUS = auto()
    AW_WORLD_SKYBOX = auto()
    AW_WORLD_MINIMUM_VISIBILITY = auto()
    AW_WORLD_REPEATING_GROUND = auto()
    AW_WORLD_KEYWORDS = auto()
    AW_WORLD_ENABLE_TERRAIN = auto()
    AW_WORLD_ALLOW_3_AXIS_ROTATION = auto()
    AW_WORLD_TERRAIN_TIMESTAMP = auto()
    AW_WORLD_ENTRY_POINT = auto()
    AW_WORLD_SKY_NORTH_RED = auto()
    AW_WORLD_SKY_NORTH_GREEN = auto()
    AW_WORLD_SKY_NORTH_BLUE = auto()
    AW_WORLD_SKY_SOUTH_RED = auto()
    AW_WORLD_SKY_SOUTH_GREEN = auto()
    AW_WORLD_SKY_SOUTH_BLUE = auto()
    AW_WORLD_SKY_EAST_RED = auto()
    AW_WORLD_SKY_EAST_GREEN = auto()
    AW_WORLD_SKY_EAST_BLUE = auto()
    AW_WORLD_SKY_WEST_RED = auto()
    AW_WORLD_SKY_WEST_GREEN = auto()
    AW_WORLD_SKY_WEST_BLUE = auto()
    AW_WORLD_SKY_TOP_RED = auto()
    AW_WORLD_SKY_TOP_GREEN = auto()
    AW_WORLD_SKY_TOP_BLUE = auto()
    AW_WORLD_SKY_BOTTOM_RED = auto()
    AW_WORLD_SKY_BOTTOM_GREEN = auto()
    AW_WORLD_SKY_BOTTOM_BLUE = auto()
    AW_WORLD_CLOUDS_LAYER1_TEXTURE = auto()
    AW_WORLD_CLOUDS_LAYER1_MASK = auto()
    AW_WORLD_CLOUDS_LAYER1_TILE = auto()
    AW_WORLD_CLOUDS_LAYER1_SPEED_X = auto()
    AW_WORLD_CLOUDS_LAYER1_SPEED_Z = auto()
    AW_WORLD_CLOUDS_LAYER1_OPACITY = auto()
    AW_WORLD_CLOUDS_LAYER2_TEXTURE = auto()
    AW_WORLD_CLOUDS_LAYER2_MASK = auto()
    AW_WORLD_CLOUDS_LAYER2_TILE = auto()
    AW_WORLD_CLOUDS_LAYER2_SPEED_X = auto()
    AW_WORLD_CLOUDS_LAYER2_SPEED_Z = auto()
    AW_WORLD_CLOUDS_LAYER2_OPACITY = auto()
    AW_WORLD_CLOUDS_LAYER3_TEXTURE = auto()
    AW_WORLD_CLOUDS_LAYER3_MASK = auto()
    AW_WORLD_CLOUDS_LAYER3_TILE = auto()
    AW_WORLD_CLOUDS_LAYER3_SPEED_X = auto()
    AW_WORLD_CLOUDS_LAYER3_SPEED_Z = auto()
    AW_WORLD_CLOUDS_LAYER3_OPACITY = auto()
    AW_WORLD_DISABLE_CHAT = auto()
    AW_WORLD_ALLOW_CITIZEN_WHISPER = auto()
    AW_WORLD_ALWAYS_SHOW_NAMES = auto()
    AW_WORLD_DISABLE_AVATAR_LIST = auto()
    AW_WORLD_AVATAR_REFRESH_RATE = auto()
    AW_WORLD_WATER_TEXTURE = auto()
    AW_WORLD_WATER_MASK = auto()
    AW_WORLD_WATER_BOTTOM_TEXTURE = auto()
    AW_WORLD_WATER_BOTTOM_MASK = auto()
    AW_WORLD_WATER_OPACITY = auto()
    AW_WORLD_WATER_RED = auto()
    AW_WORLD_WATER_GREEN = auto()
    AW_WORLD_WATER_BLUE = auto()
    AW_WORLD_WATER_LEVEL = auto()
    AW_WORLD_WATER_SURFACE_MOVE = auto()
    AW_WORLD_WATER_WAVE_MOVE = auto()
    AW_WORLD_WATER_SPEED = auto()
    AW_WORLD_WATER_ENABLED = auto()
    AW_WORLD_EMINENT_DOMAIN_CAPABILITY = auto()
    AW_WORLD_LIGHT_TEXTURE = auto()
    AW_WORLD_LIGHT_MASK = auto()
    AW_WORLD_LIGHT_DRAW_SIZE = auto()
    AW_WORLD_LIGHT_DRAW_FRONT = auto()
    AW_WORLD_LIGHT_DRAW_BRIGHT = auto()
    AW_WORLD_LIGHT_SOURCE_USE_COLOR = auto()
    AW_WORLD_LIGHT_SOURCE_COLOR = auto()
    AW_WORLD_TERRAIN_AMBIENT = auto()
    AW_WORLD_TERRAIN_DIFFUSE = auto()
    AW_WORLD_WATER_VISIBILITY = auto()
    AW_WORLD_SOUND_FOOTSTEP = auto()
    AW_WORLD_SOUND_WATER_ENTER = auto()
    AW_WORLD_SOUND_WATER_EXIT = auto()
    AW_WORLD_SOUND_AMBIENT = auto()
    AW_WORLD_GRAVITY = auto()
    AW_WORLD_BUOYANCY = auto()
    AW_WORLD_FRICTION = auto()
    AW_WORLD_WATER_FRICTION = auto()
    AW_WORLD_SLOPESLIDE_ENABLED = auto()
    AW_WORLD_SLOPESLIDE_MIN_ANGLE = auto()
    AW_WORLD_SLOPESLIDE_MAX_ANGLE = auto()
    AW_WORLD_ALLOW_TOURIST_BUILD = auto()
    AW_WORLD_ENABLE_REFERER = auto()
    AW_WORLD_WATER_UNDER_TERRAIN = auto()
    AW_WORLD_TERRAIN_OFFSET = auto()
    AW_WORLD_VOIP_RIGHT = auto()
    AW_WORLD_DISABLE_MULTIPLE_MEDIA = auto()
    AW_WORLD_BOTMENU_URL = auto()
    AW_WORLD_ENABLE_BUMP_EVENT = auto()
    AW_WORLD_ENABLE_SYNC_EVENTS = auto()
    AW_WORLD_ENABLE_CAV = auto()
    AW_WORLD_ENABLE_PAV = auto()
    AW_WORLD_CHAT_DISABLE_URL_CLICKS = auto()
    AW_WORLD_MOVER_EMPTY_RESET_TIMEOUT = auto()
    AW_WORLD_MOVER_USED_RESET_TIMEOUT = auto()
    AW_WORLD_V4_OBJECTS_RIGHT = AttributeEnum.AW_WORLD_V4_OBJECTS_RIGHT.value
    AW_WORLD_DISABLE_SHADOWS = AttributeEnum.AW_WORLD_DISABLE_SHADOWS.value
    AW_WORLD_ENABLE_CAMERA_COLLISION = AttributeEnum.AW_WORLD_ENABLE_CAMERA_COLLISION.value
    AW_WORLD_SPECIAL_COMMANDS = auto()
    AW_WORLD_CAV_OBJECT_PATH = AttributeEnum.AW_WORLD_CAV_OBJECT_PATH.value
    AW_WORLD_CAV_OBJECT_PASSWORD = auto()
    AW_WORLD_CAV_OBJECT_REFRESH = auto()
    AW_WORLD_TERRAIN_RIGHT = AttributeEnum.AW_WORLD_TERRAIN_RIGHT.value
    AW_WORLD_VOIP_CONFERENCE_GLOBAL = AttributeEnum.AW_WORLD_VOIP_CONFERENCE_GLOBAL.value
    AW_WORLD_VOIP_MODERATE_GLOBAL = auto()
    AW_WORLD_CAMERA_ZOOM = AttributeEnum.AW_WORLD_CAMERA_ZOOM.value
    AW_WORLD_WAIT_LIMIT = auto()
    AW_WORLD_VOIPCAST_HOST = AttributeEnum.AW_WORLD_VOIPCAST_HOST.value
    AW_WORLD_VOIPCAST_PORT = auto()
    AW_WORLD_ENABLE_WIREFRAME = AttributeEnum.AW_WORLD_ENABLE_WIREFRAME.value
    AW_WORLD_CHAT_CHANNEL1_NAME = AttributeEnum.AW_WORLD_CHAT_CHANNEL1_NAME.value
    AW_WORLD_CHAT_CHANNEL2_NAME = auto()
    AW_WORLD_CHAT_CHANNEL3_NAME = auto()
    AW_WORLD_CHAT_CHANNEL4_NAME = auto()
    AW_WORLD_CHAT_CHANNEL5_NAME = auto()
    AW_WORLD_CHAT_CHANNEL1_COLOR = auto()
    AW_WORLD_CHAT_CHANNEL2_COLOR = auto()
    AW_WORLD_CHAT_CHANNEL3_COLOR = auto()
    AW_WORLD_CHAT_CHANNEL4_COLOR = auto()
    AW_WORLD_CHAT_CHANNEL5_COLOR = auto()
    AW_WORLD_OWNER_CAPABILITY = AttributeEnum.AW_WORLD_OWNER_CAPABILITY.value
    AW_WORLD_RIGHTS_OFFERED = auto()
    AW_WORLD_RIGHTS_ENTER_COSTS = auto()
    AW_WORLD_RIGHTS_BUILD_COSTS = auto()
    AW_WORLD_RIGHTS_V4_OBJS_COSTS = auto()
    AW_WORLD_RIGHTS_SPECIAL_OBJS_COSTS = auto()
    AW_WORLD_RIGHTS_SPECIAL_CMDS_COSTS = auto()
    AW_WORLD_WATER_USE_SHADERS = AttributeEnum.AW_WORLD_WATER_USE_SHADERS.value
    AW_WORLD_WATER_SURFACE_COLOR = auto()
    AW_WORLD_WATER_TINT_COLOR = auto()
    AW_WORLD_WATER_WAVELET_SPEED = auto()
    AW_WORLD_WATER_WAVELET_DIRECTION_X = auto()
    AW_WORLD_WATER_WAVELET_DIRECTION_Z = auto()
    AW_WORLD_WATER_WAVELET_HEIGHT = auto()
    AW_WORLD_WATER_WAVE1_SPEED = auto()
    AW_WORLD_WATER_WAVE1_DIRECTION_X = auto()
    AW_WORLD_WATER_WAVE1_DIRECTION_Z = auto()
    AW_WORLD_WATER_WAVE1_HEIGHT = auto()
    AW_WORLD_WATER_WAVE2_SPEED = auto()
    AW_WORLD_WATER_WAVE2_DIRECTION_X = auto()
    AW_WORLD_WATER_WAVE2_DIRECTION_Z = auto()
    AW_WORLD_WATER_WAVE2_HEIGHT = auto()
    AW_WORLD_WATER_WAVE3_SPEED = auto()
    AW_WORLD_WATER_WAVE3_DIRECTION_X = auto()
    AW_WORLD_WATER_WAVE3_DIRECTION_Z = auto()
    AW_WORLD_WATER_WAVE3_HEIGHT = auto()
    AW_WORLD_WATER_WAVE4_SPEED = auto()
    AW_WORLD_WATER_WAVE4_DIRECTION_X = auto()
    AW_WORLD_WATER_WAVE4_DIRECTION_Z = auto()
    AW_WORLD_WATER_WAVE4_HEIGHT = auto()
    AW_WORLD_AUTO_CUBEMAP = auto()
    AW_WORLD_AUTO_CUBEMAP_QUALITY = auto()
    AW_WORLD_AUTO_CUBEMAP_INTERVAL = auto()
    AW_WORLD_WATER_REFLECTION_HIGHLIGHT = auto()
    AW_WORLD_WATER_SHALLOW_DEPTH = auto()
    AW_WORLD_WATER_SHALLOW_INTENSITY = auto()
    AW_WORLD_WATER_SHALLOW_DISTORTION = auto()
    AW_WORLD_WATER_SHALLOW_SCALE = auto()
    AW_WORLD_WATER_GRID_SCALE = auto()
    AW_WORLD_DISABLE_BALLOONS = AttributeEnum.AW_WORLD_DISABLE_BALLOONS.value
    AW_WORLD_MAXIMUM_VISIBILITY = auto()
