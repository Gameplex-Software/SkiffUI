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

from .output_eval import OutputNodeEval
from .datatypes import RenderImage
import 

class Renderer(object):
    """
    The core renderer which evaluates the data of the node tree and
    outputs the final render image.
    """
    def __init__(self, parent):
        self.parent = parent
        self.render = None

    def GetParent(self):
        return self.parent

    def GetRender(self):
        return self.render

    def SetRender(self, render):
        self.render = render

    def Render(self, nodes):
        """ Render method for evaluating the Node Graph
        to render an image.

        :param nodes: dictionary of nodes of the Node Graph
        :returns: rendered image
        """

        # Render the image
        output_node = self.GetOutputNode(nodes)
        rendered_image = self.RenderNodeGraph(output_node, nodes)

        # Get rendered image, otherwise use
        # a default transparent image.
        if rendered_image != None:
            image = rendered_image
        else:
            image = RenderImage()

        # TODO: Only if node thumbnails are enabled
        output_node.NodeUpdateThumb(image)

        self.SetRender(image)
        return image

    def RenderNodeGraph(self, output_node, nodes):
        print ("Renderer called")
        """ Render the image, starting from the output node.

        :param output_node: the output node object
        :param nodes: dictionary of nodes of the Node Graph
        :returns: RenderImage object
        """
        output_data = OutputNodeEval()
        output_data.SetNode(output_node)
        return output_data.RenderImage()

    def GetOutputNode(self, nodes):
        """ Get the output composite node.

        :param nodes: dictionary of nodes of the Node Graph
        :returns: node object of output node
        """
        for node_id in nodes:
            if nodes[node_id].IsOutputNode() is True:
                output_node = nodes[node_id]
        return output_node
