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
from enum import Enum, auto


class AttributeEnum(Enum):
    AW_LOGIN_NAME = 0
    AW_LOGIN_PASSWORD = auto()
    AW_LOGIN_OWNER = auto()
    AW_LOGIN_PRIVILEGE_PASSWORD = auto()
    AW_LOGIN_PRIVILEGE_NUMBER = auto()
    AW_LOGIN_PRIVILEGE_NAME = auto()
    AW_LOGIN_APPLICATION = auto()
    AW_LOGIN_EMAIL = auto()
    AW_UNIVERSE_BROWSER_MINIMUM = auto()
    AW_UNIVERSE_BROWSER_RELEASE = auto()
    AW_UNIVERSE_BROWSER_BETA = auto()
    AW_UNIVERSE_WORLD_MINIMUM = auto()
    AW_UNIVERSE_WORLD_START = auto()
    AW_UNIVERSE_REGISTRATION_REQUIRED = auto()
    AW_UNIVERSE_BUILD_NUMBER = auto()
    AW_UNIVERSE_MONTHLY_CHARGE = auto()
    AW_UNIVERSE_ANNUAL_CHARGE = auto()
    AW_UNIVERSE_REGISTER_METHOD = auto()
    AW_UNIVERSE_TIME = auto()
    AW_UNIVERSE_CITIZEN_CHANGES_ALLOWED = auto()
    AW_UNIVERSE_BROWSER_RELEASE_22 = auto()
    AW_UNIVERSE_WELCOME_MESSAGE = auto()
    AW_UNIVERSE_WORLD_RELEASE = auto()
    AW_UNIVERSE_WORLD_BETA = auto()
    AW_UNIVERSE_ALLOW_TOURISTS = auto()
    AW_UNIVERSE_SEARCH_URL = auto()
    AW_UNIVERSE_NOTEPAD_URL = auto()
    AW_UNIVERSE_NAME = auto()
    AW_UNIVERSE_USER_LIST_ENABLED = auto()
    AW_CITIZEN_NUMBER = auto()
    AW_CITIZEN_NAME = auto()
    AW_CITIZEN_PASSWORD = auto()
    AW_CITIZEN_EMAIL = auto()
    AW_CITIZEN_TIME_LEFT = auto()
    AW_CITIZEN_PRIVILEGE_PASSWORD = auto()
    AW_CITIZEN_IMMIGRATION_TIME = auto()
    AW_CITIZEN_EXPIRATION_TIME = auto()
    AW_CITIZEN_BETA = auto()
    AW_CITIZEN_LAST_LOGIN = auto()
    AW_CITIZEN_BOT_LIMIT = auto()
    AW_CITIZEN_TOTAL_TIME = auto()
    AW_CITIZEN_ENABLED = auto()
    AW_CITIZEN_COMMENT = auto()
    AW_CITIZEN_URL = auto()
    AW_WORLD_NAME = auto()
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
    AW_MY_X = auto()
    AW_MY_Y = auto()
    AW_MY_Z = auto()
    AW_MY_YAW = auto()
    AW_MY_PITCH = auto()
    AW_MY_TYPE = auto()
    AW_MY_GESTURE = auto()
    AW_MY_STATE = auto()
    AW_AVATAR_SESSION = auto()
    AW_AVATAR_NAME = auto()
    AW_AVATAR_X = auto()
    AW_AVATAR_Y = auto()
    AW_AVATAR_Z = auto()
    AW_AVATAR_YAW = auto()
    AW_AVATAR_PITCH = auto()
    AW_AVATAR_TYPE = auto()
    AW_AVATAR_GESTURE = auto()
    AW_AVATAR_STATE = auto()
    AW_AVATAR_ADDRESS = auto()
    AW_AVATAR_VERSION = auto()
    AW_AVATAR_CITIZEN = auto()
    AW_AVATAR_PRIVILEGE = auto()
    AW_AVATAR_LOCK = auto()
    AW_AVATAR_FLAGS = auto()
    AW_CHAT_SESSION = auto()
    AW_CHAT_MESSAGE = auto()
    AW_CELL_X = auto()
    AW_CELL_Z = auto()
    AW_CELL_SEQUENCE = auto()
    AW_CELL_SIZE = auto()
    AW_CELL_ITERATOR = auto()
    AW_CELL_COMBINE = auto()
    AW_OBJECT_ID = auto()
    AW_OBJECT_NUMBER = auto()
    AW_OBJECT_X = auto()
    AW_OBJECT_Y = auto()
    AW_OBJECT_Z = auto()
    AW_OBJECT_YAW = auto()
    AW_OBJECT_TILT = auto()
    AW_OBJECT_ROLL = auto()
    AW_OBJECT_MODEL = auto()
    AW_OBJECT_DESCRIPTION = auto()
    AW_OBJECT_ACTION = auto()
    AW_OBJECT_OLD_NUMBER = auto()
    AW_OBJECT_OLD_X = auto()
    AW_OBJECT_OLD_Z = auto()
    AW_OBJECT_OWNER = auto()
    AW_OBJECT_SESSION = auto()
    AW_OBJECT_BUILD_TIMESTAMP = auto()
    AW_OBJECT_SYNC = auto()
    AW_OBJECT_TYPE = auto()
    AW_OBJECT_DATA = auto()
    AW_QUERY_COMPLETE = auto()
    AW_CHAT_TYPE = auto()
    AW_LICENSE_NAME = auto()
    AW_LICENSE_PASSWORD = auto()
    AW_LICENSE_USERS = auto()
    AW_LICENSE_RANGE = auto()
    AW_LICENSE_EMAIL = auto()
    AW_LICENSE_COMMENT = auto()
    AW_LICENSE_CREATION_TIME = auto()
    AW_LICENSE_EXPIRATION_TIME = auto()
    AW_LICENSE_LAST_START = auto()
    AW_LICENSE_LAST_ADDRESS = auto()
    AW_LICENSE_HIDDEN = auto()
    AW_LICENSE_ALLOW_TOURISTS = auto()
    AW_LICENSE_VOIP = auto()
    AW_LICENSE_PLUGINS = auto()
    AW_WORLDLIST_NAME = auto()
    AW_WORLDLIST_STATUS = auto()
    AW_WORLDLIST_USERS = auto()
    AW_WORLDLIST_RATING = auto()
    AW_WORLDLIST_MORE = auto()
    AW_EJECT_SESSION = auto()
    AW_EJECT_DURATION = auto()
    AW_EJECTION_TYPE = auto()
    AW_EJECTION_ADDRESS = auto()
    AW_EJECTION_EXPIRATION_TIME = auto()
    AW_EJECTION_CREATION_TIME = auto()
    AW_EJECTION_COMMENT = auto()
    AW_DISCONNECT_REASON = auto()
    AW_FILE_RECIPIENT = auto()
    AW_FILE_SENDER = auto()
    AW_FILE_SENDER_NAME = auto()
    AW_FILE_SESSION = auto()
    AW_FILE_ADDRESS = auto()
    AW_FILE_PORT = auto()
    AW_CLICKED_SESSION = auto()
    AW_CLICKED_NAME = auto()
    AW_URL_NAME = auto()
    AW_URL_POST = auto()
    AW_URL_TARGET = auto()
    AW_URL_TARGET_3D = auto()
    AW_TELEPORT_WORLD = auto()
    AW_TELEPORT_X = auto()
    AW_TELEPORT_Y = auto()
    AW_TELEPORT_Z = auto()
    AW_TELEPORT_YAW = auto()
    AW_TELEPORT_WARP = auto()
    AW_SERVER_BUILD = auto()
    AW_SERVER_NAME = auto()
    AW_SERVER_PASSWORD = auto()
    AW_SERVER_REGISTRY = auto()
    AW_SERVER_CARETAKERS = auto()
    AW_SERVER_ID = auto()
    AW_SERVER_INSTANCE = auto()
    AW_SERVER_ENABLED = auto()
    AW_SERVER_STATE = auto()
    AW_SERVER_USERS = auto()
    AW_SERVER_MAX_USERS = auto()
    AW_SERVER_OBJECTS = auto()
    AW_SERVER_SIZE = auto()
    AW_SERVER_EXPIRATION = auto()
    AW_SERVER_START_RC = auto()
    AW_SERVER_MORE = auto()
    AW_SERVER_TERRAIN_NODES = auto()
    AW_TERRAIN_X = auto()
    AW_TERRAIN_Z = auto()
    AW_TERRAIN_PAGE_X = auto()
    AW_TERRAIN_PAGE_Z = auto()
    AW_TERRAIN_NODE_X = auto()
    AW_TERRAIN_NODE_Z = auto()
    AW_TERRAIN_NODE_SIZE = auto()
    AW_TERRAIN_NODE_TEXTURE_COUNT = auto()
    AW_TERRAIN_NODE_HEIGHT_COUNT = auto()
    AW_TERRAIN_NODE_TEXTURES = auto()
    AW_TERRAIN_NODE_HEIGHTS = auto()
    AW_TERRAIN_SEQUENCE = auto()
    AW_TERRAIN_COMPLETE = auto()
    AW_TERRAIN_VERSION_NEEDED = auto()
    AW_ENTER_GLOBAL = auto()
    AW_CONSOLE_RED = auto()
    AW_CONSOLE_GREEN = auto()
    AW_CONSOLE_BLUE = auto()
    AW_CONSOLE_BOLD = auto()
    AW_CONSOLE_ITALICS = auto()
    AW_CONSOLE_MESSAGE = auto()
    AW_BOTGRAM_TO = auto()
    AW_BOTGRAM_FROM = auto()
    AW_BOTGRAM_FROM_NAME = auto()
    AW_BOTGRAM_TYPE = auto()
    AW_BOTGRAM_TEXT = auto()
    AW_TOOLBAR_ID = auto()
    AW_TOOLBAR_SESSION = auto()
    AW_USERLIST_MORE = auto()
    AW_USERLIST_NAME = auto()
    AW_USERLIST_WORLD = auto()
    AW_USERLIST_EMAIL = auto()
    AW_USERLIST_CITIZEN = auto()
    AW_USERLIST_PRIVILEGE = auto()
    AW_USERLIST_STATE = auto()
    AW_USERLIST_ADDRESS = auto()
    AW_USERLIST_ID = auto()
    AW_SOUND_NAME = auto()
    AW_CAMERA_LOCATION_TYPE = auto()
    AW_CAMERA_LOCATION_OBJECT = auto()
    AW_CAMERA_LOCATION_SESSION = auto()
    AW_CAMERA_TARGET_TYPE = auto()
    AW_CAMERA_TARGET_OBJECT = auto()
    AW_CAMERA_TARGET_SESSION = auto()
    AW_PLUGIN_STRING = auto()
    AW_BOTMENU_TO_SESSION = auto()
    AW_BOTMENU_FROM_NAME = auto()
    AW_BOTMENU_FROM_SESSION = auto()
    AW_BOTMENU_QUESTION = auto()
    AW_BOTMENU_ANSWER = auto()
    # attributes below are not used by the SDK
    AW_CONTACT_NUMBER = auto()
    AW_CONTACT_STATUS = auto()
    AW_CONTACT_NAME = auto()
    AW_CONTACT_WORLD = auto()
    AW_CONTACT_MORE = auto()
    AW_CONTACT_OPTIONS = auto()
    AW_TELEGRAM_TO = auto()
    AW_TELEGRAM_FROM = auto()
    AW_TELEGRAM_TEXT = auto()
    AW_TELEGRAM_SENT = auto()
    AW_TELEGRAM_MORE = auto()
    AW_JOIN_NAME = auto()
    AW_JOIN_CITIZEN = auto()
    AW_JOIN_WORLD = auto()
    AW_JOIN_X = auto()
    AW_JOIN_Y = auto()
    AW_JOIN_Z = auto()
    AW_JOIN_YAW = auto()
    AW_REGISTER_CC_NAME = auto()
    AW_REGISTER_CC_NUMBER = auto()
    AW_REGISTER_CC_MONTH = auto()
    AW_REGISTER_CC_YEAR = auto()
    AW_REGISTER_ADDRESS = auto()
    AW_REGISTER_CITY = auto()
    AW_REGISTER_STATE = auto()
    AW_REGISTER_ZIP = auto()
    AW_REGISTER_PHONE_NUMBER = auto()
    AW_REGISTER_BUSINESS_NAME = auto()
    AW_REGISTER_VENDOR = auto()
    AW_REGISTER_RESULT = auto()
    AW_REGISTER_METHOD = auto()
    AW_VOIP_DATA = auto()
    # attributes below are used by the SDK
    AW_UNIVERSE_CAV_PATH = auto()
    AW_CITIZEN_PAV_ENABLED = auto()
    AW_CAV_CITIZEN = auto()
    AW_CAV_DEFINITION = auto()
    AW_ENTITY_TYPE = auto()
    AW_ENTITY_ID = auto()
    AW_ENTITY_STATE = auto()
    AW_ENTITY_FLAGS = auto()
    AW_ENTITY_X = auto()
    AW_ENTITY_Y = auto()
    AW_ENTITY_Z = auto()
    AW_ENTITY_YAW = auto()
    AW_ENTITY_PITCH = auto()
    AW_ENTITY_ROLL = auto()
    AW_ENTITY_OWNER_SESSION = auto()
    AW_ENTITY_OWNER_CITIZEN = auto()
    AW_AVATAR_DISTANCE = auto()
    AW_AVATAR_ANGLE = auto()
    AW_AVATAR_Y_DELTA = auto()
    AW_AVATAR_YAW_DELTA = auto()
    AW_AVATAR_PITCH_DELTA = auto()
    AW_AVATAR_WORLD_INSTANCE = auto()
    AW_ATTRIB_SENDER_SESSION = auto()
    AW_ENTITY_MODEL_NUM = auto()
    AW_WORLD_V4_OBJECTS_RIGHT = auto()
    AW_CITIZEN_LAST_ADDRESS = auto()
    AW_HUD_ELEMENT_TYPE = auto()
    AW_HUD_ELEMENT_ID = auto()
    AW_HUD_ELEMENT_SESSION = auto()
    AW_HUD_ELEMENT_ORIGIN = auto()
    AW_HUD_ELEMENT_X = auto()
    AW_HUD_ELEMENT_Y = auto()
    AW_HUD_ELEMENT_Z = auto()
    AW_HUD_ELEMENT_FLAGS = auto()
    AW_HUD_ELEMENT_TEXT = auto()
    AW_HUD_ELEMENT_COLOR = auto()
    AW_HUD_ELEMENT_OPACITY = auto()
    AW_HUD_ELEMENT_SIZE_X = auto()
    AW_HUD_ELEMENT_SIZE_Y = auto()
    AW_HUD_ELEMENT_SIZE_Z = auto()
    AW_HUD_ELEMENT_CLICK_X = auto()
    AW_HUD_ELEMENT_CLICK_Y = auto()
    AW_HUD_ELEMENT_CLICK_Z = auto()
    AW_HUD_ELEMENT_TEXTURE_OFFSET_X = auto()
    AW_HUD_ELEMENT_TEXTURE_OFFSET_Y = auto()
    AW_CITIZEN_PRIVACY = auto()
    AW_CITIZEN_TRIAL = auto()
    AW_UNIVERSE_CAV_PATH2 = auto()
    AW_WORLD_DISABLE_SHADOWS = auto()
    AW_WORLD_ENABLE_CAMERA_COLLISION = auto()
    AW_WORLD_SPECIAL_COMMANDS = auto()
    AW_UNIVERSE_OBJECT_REFRESH = auto()
    AW_UNIVERSE_OBJECT_PASSWORD = auto()
    AW_CAV_SESSION = auto()
    AW_CITIZEN_CAV_ENABLED = auto()
    AW_WORLD_CAV_OBJECT_PATH = auto()
    AW_WORLD_CAV_OBJECT_PASSWORD = auto()
    AW_WORLD_CAV_OBJECT_REFRESH = auto()
    AW_OBJECT_CALLBACK_REFERENCE = auto()
    AW_WORLD_TERRAIN_RIGHT = auto()
    AW_UNIVERSE_ALLOW_TOURISTS_CAV = auto()
    AW_UNIVERSE_ALLOW_BOTS_CAV = auto()
    AW_WORLD_VOIP_CONFERENCE_GLOBAL = auto()
    AW_WORLD_VOIP_MODERATE_GLOBAL = auto()
    AW_OBJECT_SESSION_TO = auto()
    AW_WORLD_CAMERA_ZOOM = auto()
    AW_WORLD_WAIT_LIMIT = auto()
    AW_XFER_DISCONNECT_REASON = auto()
    AW_XFER_TYPE = auto()
    AW_XFER_FROM_SESSION = auto()
    AW_XFER_FROM_NAME = auto()
    AW_XFER_TO_SESSION = auto()
    AW_XFER_TO_NAME = auto()
    AW_XFER_TO_WORLD_NAME = auto()
    AW_XFER_TO_ZONE_NAME = auto()
    AW_XFER_TO_TAG_NAME = auto()
    AW_XFER_DATA_ID = auto()
    AW_XFER_DATA_FILE_NAME = auto()
    AW_XFER_DATA_LEN_TOTAL = auto()
    AW_XFER_DATA_LEN_OFFSET = auto()
    AW_XFER_DATA = auto()
    AW_XFER_DATA2 = auto()
    AW_XFER_DATA3 = auto()
    AW_XFER_DATA_MORE = auto()
    AW_XFER_RC = auto()
    AW_XFER_SHOW_NAME = auto()
    AW_XFER_OPTIONS = auto()
    AW_XFER_EXPIRATION = auto()
    AW_LICENSE_XFER_SHOW_RIGHTS = auto()
    AW_XFER_SHOW_CAPABILITY = auto()
    AW_XFER_SHOW_SEQUENCE = auto()
    AW_LASER_BEAM_SOURCE_TYPE = auto()
    AW_LASER_BEAM_SOURCE_ID = auto()
    AW_LASER_BEAM_SOURCE_X = auto()
    AW_LASER_BEAM_SOURCE_Y = auto()
    AW_LASER_BEAM_SOURCE_Z = auto()
    AW_LASER_BEAM_TARGET_TYPE = auto()
    AW_LASER_BEAM_TARGET_ID = auto()
    AW_LASER_BEAM_TARGET_X = auto()
    AW_LASER_BEAM_TARGET_Y = auto()
    AW_LASER_BEAM_TARGET_Z = auto()
    AW_LASER_BEAM_STYLE = auto()
    AW_LASER_BEAM_COLOR = auto()
    AW_LASER_BEAM_DEFINITION = auto()
    AW_WORLD_VOIPCAST_HOST = auto()
    AW_WORLD_VOIPCAST_PORT = auto()
    AW_MY_ZONE = auto()
    AW_AVATAR_ZONE = auto()
    AW_UNIVERSE_PER_CITIZEN_CAV = auto()
    AW_XFER_OWNER = auto()
    AW_WORLD_ENABLE_WIREFRAME = auto()
    AW_SHOPITEM_ID = auto()
    AW_SHOPITEM_CREATION = auto()
    AW_SHOPITEM_EXPIRATION = auto()
    AW_SHOPITEM_PRICE = auto()
    AW_SHOPITEM_TYPE = auto()
    AW_SHOPITEM_CATEGORY = auto()
    AW_SHOPITEM_DESCRIPTION = auto()
    AW_SHOPITEM_OBJECT = auto()
    AW_SHOPITEM_DEFINITION = auto()
    AW_SHOPTRANS_ID = auto()
    AW_SHOPTRANS_CITIZEN = auto()
    AW_SHOPTRANS_ITEMID = auto()
    AW_SHOPTRANS_AMOUNT = auto()
    AW_SHOPTRANS_DATE = auto()
    AW_SHOPTRANS_SELLER = auto()
    AW_SHOPTRANS_COMMENT = auto()
    AW_SHOPTRANS_TOTAL = auto()
    AW_SHOPTRANS_ITERATOR = auto()
    AW_SHOPTRANS_MORE = auto()
    AW_SHOPITEM_CHANGED = auto()
    AW_LICENSE_SHOP = auto()
    AW_CITIZEN_PWD_EXP = auto()
    AW_UNIVERSE_EXPIRATION_DATE = auto()
    AW_UNIVERSE_IMMIGRATION = auto()
    AW_CITIZEN_SEC_PASSWORD = auto()
    AW_CHAT_CHANNEL = auto()
    AW_CHAT_CITIZEN = auto()
    AW_WORLD_CHAT_CHANNEL1_NAME = auto()
    AW_WORLD_CHAT_CHANNEL2_NAME = auto()
    AW_WORLD_CHAT_CHANNEL3_NAME = auto()
    AW_WORLD_CHAT_CHANNEL4_NAME = auto()
    AW_WORLD_CHAT_CHANNEL5_NAME = auto()
    AW_WORLD_CHAT_CHANNEL1_COLOR = auto()
    AW_WORLD_CHAT_CHANNEL2_COLOR = auto()
    AW_WORLD_CHAT_CHANNEL3_COLOR = auto()
    AW_WORLD_CHAT_CHANNEL4_COLOR = auto()
    AW_WORLD_CHAT_CHANNEL5_COLOR = auto()
    AW_WORLDLIST_BOTS = auto()
    AW_LICENSE_OWNER = auto()
    AW_WORLD_OWNER_CAPABILITY = auto()
    AW_WORLD_RIGHTS_OFFERED = auto()
    AW_WORLD_RIGHTS_ENTER_COSTS = auto()
    AW_WORLD_RIGHTS_BUILD_COSTS = auto()
    AW_WORLD_RIGHTS_V4_OBJS_COSTS = auto()
    AW_WORLD_RIGHTS_SPECIAL_OBJS_COSTS = auto()
    AW_WORLD_RIGHTS_SPECIAL_CMDS_COSTS = auto()
    AW_PURCHASE_KIND = auto()
    AW_PURCHASE_TYPE = auto()
    AW_PURCHASE_COSTS = auto()
    AW_CITRIGHT_TYPES = auto()
    AW_DLG_ORIGINATOR_SESSION = auto()
    AW_DLG_RECIPIENT_SESSION = auto()
    AW_DLG_REFERENCE = auto()
    AW_DLG_OPTION = auto()
    AW_DLG_TITLE = auto()
    AW_DLG_TEXT = auto()
    AW_DLG_ANSWER_ORIGINATOR_SESSION = auto()
    AW_DLG_ANSWER_RECIPIENT_SESSION = auto()
    AW_DLG_ANSWER_REFERENCE = auto()
    AW_DLG_ANSWER_OPTION = auto()
    AW_DLG_ANSWER_TEXT = auto()
    AW_WORLD_WATER_USE_SHADERS = auto()
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
    AW_UNIVERSE_BUY_CREDITS_URL = auto()
    AW_CITIZEN_ONLINE_STATE = auto()
    AW_CITIZEN_TITLE_NUMBER = auto()
    AW_CITIZEN_TITLE_STARS = auto()
    AW_UNIVERSE_IMMIGRATE_URL = auto()
    AW_CITIZEN_SESSION = auto()
    AW_CHAT_TARGET_TYPES = auto()
    AW_CHAT_TARGET_SESSION = auto()
    AW_CITIZEN_HASH = auto()
    AW_XFER_DATA4 = auto()
    AW_XFER_DATA5 = auto()
    AW_LICENSE_LAST_PORT = auto()
    AW_LICENSE_LAST_STOP = auto()
    AW_CONTACT_LAST_SEEN = auto()
    AW_WORLD_DISABLE_BALLOONS = auto()
    AW_WORLD_MAXIMUM_VISIBILITY = auto()
    AW_TELEGRAM_JOURNAL_START = auto()
    AW_TELEGRAM_JOURNAL_END = auto()
    AW_TELEGRAM_STATUS = auto()
    AW_MAX_ATTRIBUTE = auto()
