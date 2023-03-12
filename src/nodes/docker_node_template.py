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

from gimelstudio import api

class DockerNode(api.Node):
    def __init__(self, nodegraph, _id):
        api.Node.__init__(self, nodegraph, _id)

    @property
    def NodeMeta(self):
        meta_info = {
            "label": "{{container_name}}",
            "author": "Gameplex Software",
            "version": (0, 0, 1),
            "category": "FILTER",
            "description": "Show {{container_name}} container on the node graph",
        }
        return meta_info

    def NodeInitProps(self):
        container_id = api.LabelProp(
            idname="container_id",
            default="{{container_id}}",
            show_p=False
        )
        self.NodeAddProp(container_id)

        container_name = api.LabelProp(
            idname="container_name",
            default="{{container_name}}",
            show_p=False
        )
        self.NodeAddProp(container_name)

        container_status = api.LabelProp(
            idname="container_status",
            default="{{container_status}}",
            show_p=True,
            fpb_label="Status"
        )
        self.NodeAddProp(container_status)

        container_image = api.LabelProp(
            idname="container_image",
            default="{{container_image}}",
            show_p=True,
            fpb_label="Image"
        )
        self.NodeAddProp(container_image)

    def NodeInitParams(self):
        pass

    def MutedNodeEvaluation(self, eval_info):
        return self.EvalMutedNode(eval_info)

    def NodeEvaluation(self, eval_info):
        render_image = api.RenderImage()
        return render_image

api.RegisterNode(DockerNode, "{{container_id}}")