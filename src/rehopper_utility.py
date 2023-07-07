#!/usr/bin/env ipy
# -*- coding: utf-8 -*-

__all__ = ['ReloadGrasshopper']

# - - - - BUILT-IN IMPORTS
import Rhino, System
import clr, sys, traceback

# - - - - GLOBALS
IGNORE_LIST =   [   
                    "Rehopper",
                    "rhinoscript.datetime", 
                    "Eto", 
                    "rhinoscript.System", 
                    "__main__", 
                    "rhinoscript.Rhino", 
                    "copy_reg", 
                    "rhinoscript.curve", 
                    "rhinoscript", 
                    "System", 
                    "rhinoscript.numbers", 
                    "rhinoscriptsyntax", 
                    "rhinoscript.linetype", 
                    "zipimport", 
                    "rhinoscript.geometry", 
                    "rhinoscript.string", 
                    "re", 
                    "rhinoscript.plane", 
                    "rhinoscript.selection", 
                    "scriptcontext", 
                    "Rhino", 
                    "string", 
                    "rhinoscript.mesh", 
                    "rhinoscript.toolbar", 
                    "rhinoscript.transformation", 
                    "time", 
                    "rhinoscript.layer", 
                    "rhinoscript.light", 
                    "rhinoscript.userdata", 
                    "rhinoscript.application", 
                    "rhinoscript.group", 
                    "__builtin__", 
                    "rhinoscript.hatch", 
                    "sys", 
                    "__future__", 
                    "numbers", 
                    "RhinoPython", 
                    "rhinoscript.math", 
                    "rhinoscript.RhinoPython", 
                    "rhinoscript.userinterface", 
                    "rhinoscript.line", 
                    "rhinoscript.pointvector", 
                    "types", 
                    "rhinoscript.grips", 
                    "rhinoscript.view", 
                    "rhinoscript.document", 
                    "rhinoscript.Eto", 
                    "_weakrefset", 
                    "rhinoscript.dimension", 
                    "_weakref", 
                    "rhinoscript.time", 
                    "datetime", 
                    "rhinoscript.surface", 
                    "rhinoscript.block", 
                    "rhinoscript.scriptcontext", 
                    "rhinoscript.object", 
                    "rhinoscript.utility", 
                    "math", 
                    "rhinoscript.material", 
                    "abc",
                ]

# - - - - LIBRARY METHODS
def load_grasshopper(files = []):
    grasshopper = Rhino.RhinoApp.GetPlugInObject( 'Grasshopper' )
    import Grasshopper
    Grasshopper.Instances.AutoShowBanner = False
    grasshopper.LoadEditor()
    
    if len(files) > 0:
        files.reverse()
        for file in files:
            Grasshopper.Instances.DocumentServer.AddDocument(file, True)
    
    grasshopper.ShowEditor()

def files_are_closed():
    """
    Check for open Grasshopper document. 
    Aks to reload if open.
    Return True or False. 
    """
    clr.AddReference("Grasshopper")
    import Grasshopper
    doc_open = Grasshopper.Instances.DocumentServer.DocumentCount
    if doc_open > 0:
        message = ["You have some documents open in Grasshopper.",
                  "You will loose all not saved progress.",
                  "Do you want to continue?"]
        rc = System.Windows.Forms.MessageBox.Show(
                "\n".join(message),
                "Warning",
                System.Windows.Forms.MessageBoxButtons.OKCancel,
                System.Windows.Forms.MessageBoxIcon.Warning)
        
        return int(rc) == 6 or str(rc).lower() == "ok"
    else:
        return True

def close_gh_docs(gh_files):
    """
    Recursive: close documents ans save to paths to list.
    """
    clr.AddReference("Grasshopper")
    import Grasshopper
    if Grasshopper.Instances.DocumentServer.DocumentCount != 0:
        doc = Grasshopper.Instances.DocumentServer[0]
        
        close = Grasshopper.Instances.DocumentServer.SafeRemoveDocument(doc)
        if not close:
            #Stop the process if canseled
            return False
        
        if doc.FilePath:
            gh_files.append(doc.FilePath)
        
        return close_gh_docs(gh_files)
    else:
        return True

def reload_grasshopper():

    if files_are_closed():
        gh_files = []
        close_gh_docs(gh_files)
        
        clr.AddReference("Grasshopper")
        import Grasshopper
        Grasshopper.Instances.ComponentServer.Clear()
        Grasshopper.Instances.UnloadAllObjects()

        modules = sys.modules.copy()

        for module in modules:
            if not module in IGNORE_LIST:
                sys.modules.pop(module)

        load_grasshopper(gh_files)
        return

    else:
        return

def ReloadGrasshopper():

    try:
        if "Grasshopper" in sys.modules.keys():
            reload_grasshopper()
        else:
            clr.AddReference("Grasshopper")
            load_grasshopper()
    except:
        System.Windows.Forms.MessageBox.Show(traceback.format_exc(), 'Failed to reload Grasshopper!')

# - - - - RUNSCRIPT
if __name__ == "__main__":
    ReloadGrasshopper()
