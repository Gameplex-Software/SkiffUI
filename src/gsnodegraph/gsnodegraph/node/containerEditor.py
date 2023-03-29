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

import wx

class ContainerEditor(wx.Dialog):
    def __init__(self):
        super().__init__(None, title="Container Editor", size=(900, 800))
        
        self.SetBackgroundColour('#1E1E1E') # set the background color to dark
        
        # create the notebook with tabs
        self.notebook = wx.Notebook(self)
        self.general_tab = wx.Panel(self.notebook)
        self.ports_tab = wx.Panel(self.notebook)
        self.volumes_tab = wx.Panel(self.notebook)
        self.environment_tab = wx.Panel(self.notebook)
        self.notebook.AddPage(self.general_tab, "General")
        self.notebook.AddPage(self.ports_tab, "Ports")
        self.notebook.AddPage(self.volumes_tab, "Volumes")
        self.notebook.AddPage(self.environment_tab, "Environment")
        
        # create controls for the General tab
        self.container_name_label = wx.StaticText(self.general_tab, label="Container Name:")
        # set the label text color to white
        self.container_name_label.SetForegroundColour(wx.WHITE)
        self.container_name_text = wx.TextCtrl(self.general_tab)
        
        # create a sizer for the General tab
        general_sizer = wx.BoxSizer(wx.VERTICAL)
        general_sizer.Add(self.container_name_label, 0, wx.ALL, 5)
        general_sizer.Add(self.container_name_text, 0, wx.ALL, 5)
        self.general_tab.SetSizer(general_sizer)
        
        # create the buttons
        self.cancel_button = wx.Button(self, label="Cancel")
        self.save_button = wx.Button(self, label="Save")
        self.apply_button = wx.Button(self, label="Apply")
        
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(self.cancel_button, 0, wx.ALL, 5)
        button_sizer.Add(self.save_button, 0, wx.ALL, 5)
        button_sizer.Add(self.apply_button, 0, wx.ALL, 5)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.notebook, 1, wx.EXPAND)
        sizer.Add(button_sizer, 0, wx.ALIGN_CENTER)
        
        self.SetSizer(sizer)
        self.Layout()
        
        self.SetSize((900, 800)) # set the size of the entire dialog, including borders and title bar
        
        self.ShowModal()
        
if __name__ == '__main__':
    app = wx.App()
    ContainerEditor()
    app.MainLoop()