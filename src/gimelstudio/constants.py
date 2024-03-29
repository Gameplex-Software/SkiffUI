# ----------------------------------------------------------------------------
# Gimel Studio Copyright 2019-2022 by Noah Rahm and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# SkiffUI Copyright 2020-2023 by Gameplex Software and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------

import os
import sys
import os.path


# Application
APP_FROZEN = getattr(sys, "frozen", False)
APP_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))

APP_VERSION = "0.2.3"
APP_VERSION_TAG = " pre-alpha 1"
APP_VERSION_FULL = "{0}{1}".format(APP_VERSION, APP_VERSION_TAG)

APP_NAME = "SkiffUI"
APP_DESCRIPTION = "Container management made easy"
APP_COPYRIGHT = "© 2019–2023 Gameplex Software, Noah Rahm, and contributors"

APP_WEBSITE_URL = "https://gameplexsoftware.com/SkiffUI"
APP_LICENSE_URL = "https://github.com/Gameplex-Software/SkiffUI/blob/master/LICENSE"
APP_GITHUB_URL =  "https://github.com/Gameplex-Software/SkiffUI"
APP_CREDITS_URL = "https://github.com/Gameplex-Software/SkiffUI/graphs/contributors"
APP_DISCORD_URL = "[Discord URL]"  # Remove dashes when using this
APP_YOUTUBE_URL = ""

APP_FULL_TITLE = "{0} v{1}".format(APP_NAME, APP_VERSION_FULL)

APP_CONFIG_FILE = os.path.expanduser("~/.Skiffui/pre-a2-config.json")

# File system
SUPPORTED_FT_OPEN_LIST = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".exr",
    ".webp",
    ".tiff"
]
SUPPORTED_FT_OPEN_WILDCARD = \
    "All files (*.*)|*.*|" \
    "JPG file (*.jpg)|*.jpg|" \
    "JPEG file (*.jpeg)|*.jpeg|" \
    "PNG file (*.png)|*.png|" \
    "BMP file (*.bmp)|*.bmp|" \
    "GIF file (*.gif)|*.gif|" \
    "EXR file (*.exr)|*.exr|" \
    "WEBP file (*.webp)|*.webp|" \
    "TIFF file (*.tiff)|*.tiff"

SUPPORTED_FT_SAVE_LIST = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".exr",
    ".webp",
    ".tiff"
]
SUPPORTED_FT_SAVE_WILDCARD = \
    "JPG file (*.jpg)|*.jpg|" \
    "JPEG file (*.jpeg)|*.jpeg|" \
    "PNG file (*.png)|*.png|" \
    "BMP file (*.bmp)|*.bmp|" \
    "GIF file (*.gif)|*.gif|" \
    "EXR file (*.exr)|*.exr|" \
    "WEBP file (*.webp)|*.webp|" \
    "TIFF file (*.tiff)|*.tiff|" \
    "All files (*.*)|*.*"

PROJECT_FILE_WILDCARD = "SkiffUI file (*.skf)|*.skf"

# Colors
AREA_BG_COLOR = "#242528"
AREA_TOPBAR_COLOR = "#3f4146"

PROP_HEADER_COLOR = "#3f4146"
PROP_BG_COLOR = "#36383c"

ACCENT_COLOR = "#5173b5"
DARK_COLOR = "#1b1c1e"

TEXT_COLOR = "#dfdfdf"

ADD_NODE_MENU_BG = "#121314"

NODE_DEFAULT_WIDTH = "300"
NODE_DEFAULT_HEIGHT = "400"