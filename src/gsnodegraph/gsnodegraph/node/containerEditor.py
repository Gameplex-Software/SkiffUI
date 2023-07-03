import wx
import wx.grid
from shiphelm import helm

helm = helm.helm()
helm.set_engine_manual(engine_select="docker")


class PortsTable(wx.grid.Grid):
    def __init__(self, parent):
        super().__init__(parent)
        self.CreateGrid(1, 3)

        self.SetColLabelValue(0, "Internal Port")
        self.SetColLabelValue(1, "External Port")
        self.SetColLabelValue(2, "Remove port")

        self.SetColSize(0, 100)
        self.SetColSize(1, 100)
        self.SetColSize(2, 100)

        self.SetDefaultCellAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        self.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.on_left_click)

        self.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.on_label_left_click)

        self.SetRowLabelSize(0)
        self.AutoSize()

    def on_left_click(self, event):
        row = event.GetRow()
        col = event.GetCol()
        if col == 2:
            self.DeleteRows(row)

    def on_label_left_click(self, event):
        col = event.GetCol()
        if col == 2:
            for row in range(self.GetNumberRows()):
                self.DeleteRows(row)


class ContainerEditor(wx.Dialog):
    def __init__(self, id):
        super().__init__(None, title="Container Editor", size=(600, 700))

        # store the ID of the container to be edited
        ContainerEditor.id = id

        # Get volume data (for now this is a placeholder)
        self.data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Gender': ['Female', 'Male', 'Male']}

        # set the background color to dark
        self.SetBackgroundColour('#1E1E1E')

        # create a notebook and tabs
        self.notebook = wx.Notebook(self)
        self.general_tab = wx.Panel(self.notebook)
        self.volumes_tab = wx.Panel(self.notebook)
        self.ports_tab = wx.Panel(self.notebook)
        self.environment_tab = wx.Panel(self.notebook)
        self.command_tab = wx.Panel(self.notebook)

        self.notebook.AddPage(self.general_tab, "General")
        self.notebook.AddPage(self.volumes_tab, "Volumes")
        self.notebook.AddPage(self.ports_tab, "Ports")
        self.notebook.AddPage(self.environment_tab, "Environment")
        self.notebook.AddPage(self.command_tab, "Command")

        # General tab
        self.container_name_label = wx.StaticText(self.general_tab, label="Container Name:")
        self.container_name_label.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        self.container_name_label.SetForegroundColour(wx.WHITE)
        ContainerEditor.container_name_text = wx.TextCtrl(self.general_tab,
                                                          value=str(helm.get_container_by_id(ContainerEditor.id).name))

        self.container_image_label = wx.StaticText(self.general_tab, label="Container Image:")
        self.container_image_label.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        self.container_image_label.SetForegroundColour(wx.WHITE)
        choices = ['Gameplex-Software/Nginx', 'Gameplex-Software/BusyBox', 'Gameplex-Software/Apache',
                   'Gameplex-Software/NginxPlus']
        ContainerEditor.container_image_text = wx.ComboBox(self.general_tab, choices=choices)

        static_box = wx.StaticBox(self.general_tab, label="Container Details")
        general_sizer = wx.BoxSizer(wx.VERTICAL)
        static_box_sizer = wx.StaticBoxSizer(static_box, wx.VERTICAL)

        static_box_sizer.Add(self.container_name_label, 0, wx.ALL | wx.LEFT, 5)
        static_box_sizer.Add(ContainerEditor.container_name_text, 0, wx.ALL | wx.EXPAND, 5)

        static_box_sizer.Add(self.container_image_label, 0, wx.ALL | wx.LEFT, 5)
        static_box_sizer.Add(self.container_image_text, 0, wx.ALL | wx.EXPAND, 5)

        general_sizer.Add(static_box_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self.general_tab.SetSizer(general_sizer)

        # Volumes tab
        volume_sizer = wx.BoxSizer(wx.VERTICAL)

        static_box = wx.StaticBox(self.volumes_tab, label="Container Volumes:")
        static_box_sizer = wx.StaticBoxSizer(static_box, wx.VERTICAL)

        volume_sizer.Add(static_box_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self.volumes_tab.SetSizer(volume_sizer)

        # Ports tab
        self.ports_table = PortsTable(self.ports_tab)
        self.add_row_button = wx.Button(self.ports_tab, label="Add Rule")
        self.add_row_button.Bind(wx.EVT_BUTTON, self.on_add_row)

        self.ports_table.SetGridLineColour(wx.Colour(64, 64, 64))

        ports_sizer = wx.BoxSizer(wx.VERTICAL)
        ports_sizer.Add(self.ports_table, 1, wx.EXPAND | wx.ALL, 5)
        ports_sizer.Add(self.add_row_button, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.ports_tab.SetSizer(ports_sizer)

        # Environment tab
        environment_sizer = wx.BoxSizer(wx.VERTICAL)

        static_box = wx.StaticBox(self.environment_tab, label="Container Environment Variables")
        static_box_sizer = wx.StaticBoxSizer(static_box, wx.VERTICAL)

        environment_sizer.Add(static_box_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self.environment_tab.SetSizer(environment_sizer)

        # Command tab
        command_sizer = wx.BoxSizer(wx.VERTICAL)

        static_box = wx.StaticBox(self.command_tab, label="Container docker Run Command")
        static_box_sizer = wx.StaticBoxSizer(static_box, wx.VERTICAL)

        command_sizer.Add(static_box_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self.command_tab.SetSizer(command_sizer)

        self.container_command_label = wx.StaticText(self.command_tab, label="Container Command:")
        self.container_command_label.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        self.container_command_label.SetForegroundColour(wx.WHITE)
        helm.set_engine_manual('docker')
        ContainerEditor.container_command_text = wx.TextCtrl(self.command_tab,
                                                             value=str(helm.get_run_command(container_id=ContainerEditor.id)))

        static_box = wx.StaticBox(self.command_tab, label="Container Details")
        command_sizer = wx.BoxSizer(wx.VERTICAL)
        static_box_sizer = wx.StaticBoxSizer(static_box, wx.VERTICAL)

        static_box_sizer.Add(self.container_command_label, 0, wx.ALL | wx.LEFT, 5)
        static_box_sizer.Add(ContainerEditor.container_command_text, 0, wx.ALL | wx.EXPAND, 5)

        command_sizer.Add(static_box_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self.command_tab.SetSizer(command_sizer)

        # End of tabs
        self.cancel_button = wx.Button(self, label="Cancel")
        self.save_button = wx.Button(self, label="Save")
        self.apply_button = wx.Button(self, label="Apply")

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(self.cancel_button, 0, wx.ALL, 5)
        button_sizer.Add(self.save_button, 0, wx.ALL, 5)
        button_sizer.Add(self.apply_button, 0, wx.ALL, 5)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.notebook, 1, wx.EXPAND)
        sizer.Add(button_sizer, 0, wx.CENTRE)

        self.SetSizer(sizer)
        self.Layout()

        self.cancel_button.SetBackgroundColour('#333333')
        self.save_button.SetBackgroundColour('#333333')
        self.apply_button.SetBackgroundColour('#333333')

        self.notebook.SetBackgroundColour('#333333')

        self.container_name_label.SetBackgroundColour('#333333')
        self.container_image_label.SetBackgroundColour('#333333')

        self.container_name_label.SetForegroundColour(wx.WHITE)
        self.container_image_label.SetForegroundColour(wx.WHITE)

        self.container_name_text.SetBackgroundColour('#444444')
        self.container_image_text.SetBackgroundColour('#444444')
        self.container_command_text.SetBackgroundColour('#444444')

        self.ports_table.SetBackgroundColour('#444444')
        self.add_row_button.SetBackgroundColour('#444444')

        self.SetBackgroundColour('#1E1E1E')

        # Set the text color in textboxes
        self.container_name_text.SetForegroundColour(wx.WHITE)
        self.container_image_text.SetForegroundColour(wx.WHITE)
        self.container_command_text.SetForegroundColour(wx.WHITE)

        self.ports_table.SetForegroundColour(wx.WHITE)

        self.cancel_button.SetForegroundColour(wx.WHITE)
        self.save_button.SetForegroundColour(wx.WHITE)
        self.apply_button.SetForegroundColour(wx.WHITE)

        # bind events to buttons
        self.cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)
        self.save_button.Bind(wx.EVT_BUTTON, self.on_save)
        self.apply_button.Bind(wx.EVT_BUTTON, self.on_apply)

    def on_apply(self, event):
        container_name = self.container_name_text.GetValue()
        container_image = self.container_image_text.GetValue()

        helm.rename_container(str(ContainerEditor.id), str(container_name))
        print("Applied changes to container", self.id)

    def on_save(self, event):
        self.on_apply()
        print("Saved", ContainerEditor.id)
        self.EndModal(wx.ID_CANCEL)

    def on_cancel(self, event):
        self.EndModal(wx.ID_CANCEL)

    def on_add_row(self, event):
        num_rows = self.ports_table.GetNumberRows()
        self.ports_table.InsertRows(num_rows)
