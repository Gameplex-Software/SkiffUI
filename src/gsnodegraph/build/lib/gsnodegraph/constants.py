# ----------------------------------------------------------------------------
# gsnodegraph Copyright 2019-2021 by Noah Rahm and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License" ;
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

SOCKET_DATATYPE_COLORS = {
    "RGBAIMAGE": "#C6C62D",  # Yellow
    "VALUE": "#A0A0A0",  # Grey
}

SOCKET_INPUT = 0
SOCKET_OUTPUT = 1

SOCKET_RADIUS = 8
SOCKET_HIT_RADIUS = 12

SOCKET_BORDER_COLOR = (27, 28, 30, 255)

WIRE_NORMAL_COLOR = (128, 128, 128, 255)
WIRE_ACTIVE_COLOR = (210, 210, 210, 255)

DEFAULT_WIRE_CURVATURE = 40

NODE_HEADER_CATEGORY_COLORS = {
    "INPUT": "#498DB8",  # Burgendy
    "DRAW": "#AF4467",  # Pink
    "MASK": "#084D4D",  # Blue-green
    "CONVERT": "#564B7C",  # Purple
    "FILTER": "#878aad",  # Green
    "BLEND": "#558333",  # Light blue
    "COLOR": "#C2AF3A",  # Yellow
    "TRANSFORM": "#6B8B8B", # Blue-grey
    "OUTPUT": "#7176bf"  # Blue
}
NODE_HEADER_MUTED_COLOR = (70, 70, 70, 255)

NODE_NORMAL_COLOR = (54, 56, 60, 255)
NODE_SELECTED_COLOR = (63, 66, 70, 255)
NODE_MUTED_COLOR = (63, 66, 70, 90)

NODE_BORDER_NORMAL_COLOR = (27, 28, 30, 255)
NODE_BORDER_SELECTED_COLOR = (255, 255, 255, 255)

NODE_THUMB_BORDER_COLOR = (27, 28, 30, 255)

NODE_DEFAULT_WIDTH = 250
NODE_DEFAULT_HEIGHT = 400
NODE_THUMB_PADDING = 16
NODE_Y_PADDING = 10

SELECTION_BOX_BORDER_COLOR = (194, 194, 194, 255)
SELECTION_BOX_COLOR = (100, 100, 100, 56)

GRAPH_BACKGROUND_COLOR = (36, 37, 40, 255)

BTN_NORMAL_COLOR = (0, 0, 0, 0)
BTN_CLICKED_COLOR = (90, 127, 200, 255)
BTN_FOCUSED_COLOR = (54, 56, 60, 255)
