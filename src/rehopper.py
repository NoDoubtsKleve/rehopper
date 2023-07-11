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
        icon_text = "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAAXNSR0IArs4c6QAAAyxJREFUSEttVr1uk0EQnHNHgcBPgB1jSIRI3ECKBAl4B/sr/RJ2CVJaKuiQUsQubVfwBBahwRRUSWunS8lPEaoc2p3du/ssvkiOfb672Zmd3XUAAhAiEKHPPLbtQ+DC1iOrsjX4q37gijyDsK4dlNt1w+K2FYkR7DAQo4HbYbk0yvsIBP7Tl5PX17hc3mAW27ogCP2wUSAFmMfWVtTcxFdG6yseqR1WkJNX17hY3mB+27av5bqAQWMtcRAgUTZJ9FJloLR5UD6blqfnlcLK2oe3n3Cx/KsAZMb1SgCouT/U0kXsN9aWnqy8A/geOfHk5Z1CImNs8gbKU27n+yqsLWDmZDQ9QIwilP2FgHfDH8aHe2YmkbNXfZSBJs28EYGqsVEpJIjxWQ8PO48Sr/dvPutekU8uEmn4qNSWu6wJGTgdZj95aTTZR7ezq1E2j1bqtoF8n/JhFnWLKwOzrDktLGIrejIlor5EHwPGk6fo7uzpZc3jFdTDAfg+vWu+MjunvEc8G/7JYjtAyWAQrpI5P55Xuvn+8bckQarGZN+8sm0U1mFEWMS2FVi24+kXsaBcvkq2FFaSNJowOy1bkNas71EAqWDyVH0BiMflcspSapqNkLQoClHrRdtNK7WO5KJUUFsA6piUdgrhUZd2lLWB1k3ALD4wNjHbVADc+yKRaO+twtubNw+XKANxBwGAmTEQXWouqsKGZQ5gEVup2ZV9ycEK86i7NLhUD2SgnS4n2bqg2ZQA3g692VkJmMIMhnb1+hlNejgc/spnFSC134hBY8O8Alr6dIW07v+BsaKl8tkOgNHZAQ6Hv43NVg68LVMqOmgh1Wmdle2Ec8LngejOuwNG0310d3bRLPJX2NT8YYeVsk06IUE2ZlNvhmxBCjDWtrKnAbA4KV3KQX0E8py3ax85xX2prYs040kP3c5jBWq+kOKkpBKQKuxzWDEtH+53JvCKZa9jyb0CSDMUcGmIGvnRqjZKdeCUE40zlnNYmdv7n1+fFxEz6eUje++ZLKkMy5FpyYw+6sqxR7DMzPeQu1nL0Qqn1YZ+WaH+A6BkQFHFOfVfFWXjK+dwMYPxDzaM6LsoL59gAAAAAElFTkSuQmCC"
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
