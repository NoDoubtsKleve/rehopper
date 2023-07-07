#!/usr/bin/env ipy
# -*- coding: utf-8 -*-

__all__ = ['AssemblyInfo']

# - - - - BUILT-IN IMPORTS
import System
import traceback

# - - - - LOCAL IMPORTS
import reload_grasshopper

# - - - - RH/GH IMPORTS
import clr
clr.AddReference("Grasshopper")
import Grasshopper
import GhPython

# - - - - CLASS LIBRARY
class AssemblyInfo(GhPython.Assemblies.PythonAssemblyInfo):

    Name = "Rehopper"
    
    def get_icon(self):
        icon_text = "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAFvSURBVEhL7ZWxLgVREIY33ESpJRoFhUKnUKk8gkYjIqFS6EWh8wB4AI3CC9wXuNUtaJUi0ehEQkLwfTdnkutuVmZR3j/5Mjnn7Jk9OzszpxrrL5qEOdiHHrzCZ+ERrmANpqG1pmAPruEdwvEoL3AJS5CWzk/hGcLRLRzDNuzASZlz7QP6kNIEbMETuPkBdqFJB+BXrg9GCc2CpwnnG9CBJrk2U2xK/tCIuSdPb8yqCxHztpqH82JrWoUjiNjflLHzWZ2Be7U1LcM9+EDg2PmMNiHqROu4JmP+Bj6k/Sl7hrUIdzB8OMfOf5P5fwE+oHWc0QocgmF1r2F27HxNC6BzbVtF4Zko/ypT2YLTuSluqqeUKSLXLEaL0hdYpBZrSpa/bcDTNcm1cG7sbTO2m5Q8jY3MzcbXBmejs+HZ+CLm4dwGmU2MgWzBtmJbcjgaxZj7lb60lfOQl4mXipeLl0w4tpi8hPyhXkpeTmP9RlX1BUmPb3+17Y+kAAAAAElFTkSuQmCC"
        icon = System.Drawing.Bitmap(System.IO.MemoryStream(System.Convert.FromBase64String(icon_text)))
        return icon
    
    def get_canvas_toolbar(self):
        all_toolbars = Grasshopper.Instances.ActiveCanvas.Parent.Controls
        canvas_toolbar = all_toolbars.Item[all_toolbars.IndexOfKey("CanvasToolbar")]
        return canvas_toolbar

    def add_reload_button(self, args):
        icon = self.get_icon()
        canvas_toolbar = self.get_canvas_toolbar()

        for item in canvas_toolbar.Items:
            if item.Text == "Rehopper":
                return

        item = canvas_toolbar.Items.Add("Rehopper", icon, self.on_reload_button_clicked)
        item.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image
        item.ToolTipText = "Reload Grasshopper assemblies."

    def on_reload_button_clicked(self, sender, args):
        try:
            reload_grasshopper.ReloadGrasshopper()
        except Exception as ex:
            System.Windows.Forms.MessageBox.Show(str(ex), traceback.format_exc())

    def __init__(self):
        Grasshopper.Instances.CanvasCreated -= self.add_reload_button
        Grasshopper.Instances.CanvasCreated += self.add_reload_button
  
    def get_AssemblyName(self):
        return AssemblyInfo.Name

    def get_AssemblyDescription(self):
        return AssemblyInfo.Name

    def get_AssemblyVersion(self):
        return "0.0.2"

    def get_AuthorName(self):
        return "No Doubts GmbH"

    def get_Id(self):
        return System.Guid("cf4c90b3-6460-4c87-9100-3ce39d88a0c8")      
