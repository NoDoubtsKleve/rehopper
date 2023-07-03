# -*- coding: utf-8 -*-

import Rhino, System, traceback, sys, clr, Grasshopper

TO_IGNORE = [   "rhinoscript.datetime", 
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

def CheckIfAnythingOpen():
    """
    Check for open Grasshopper document. 
    Aks to reload if open.
    Return True or False. 
    """
    doc_open = Grasshopper.Instances.DocumentServer.DocumentCount
    if doc_open > 0:
        message = ["You have some documents open in Grasshopper.",
                  "You will loose all not saved progress.",
                  "Do you want to continue?"]
        rc = System.Windows.Forms.MessageBox.Show(
                "\n".join(message),
                "Category manager",
                System.Windows.Forms.MessageBoxButtons.OKCancel,
                System.Windows.Forms.MessageBoxIcon.Warning)
        return rc
    else:
        return True

def CloseTheGhDocs(gh_files):
    """
    Recursive: close documents ans save to paths to list.
    """
    if Grasshopper.Instances.DocumentServer.DocumentCount != 0:
        doc = Grasshopper.Instances.DocumentServer[0]
        
        close = Grasshopper.Instances.DocumentServer.SafeRemoveDocument(doc)
        if not close:
            #Stop the process if canseled
            return False
        
        if doc.FilePath:
            gh_files.append(doc.FilePath)
        
        return CloseTheGhDocs(gh_files)
    else:
        return True

def LoadGrasshopepr(files = None):
    #Load Grasshopepr
    Gh = Rhino.RhinoApp.GetPlugInObject( 'Grasshopper' )
    Grasshopper.Instances.AutoShowBanner = False
    Gh.LoadEditor()
    
    #Load open files
    if files:
        files.reverse()
        for f in files:
            Grasshopper.Instances.DocumentServer.AddDocument(f, True)
    
    #Load GH UI
    Gh.ShowEditor()

def ReloadGrasshopper(): 
    """
    Reloading of Grasshopper plugins
    """
    
    #Conferm the reloading
    if not CheckIfAnythingOpen():
        return 

    #Save paths of open files to reload them back
    gh_files = []
    if not CloseTheGhDocs(gh_files):
        return
    
    #Unload Grasshopper 
    Grasshopper.Instances.ComponentServer.Clear()
    Grasshopper.Instances.UnloadAllObjects()
    
    #Clean imported lybraries
    modules = sys.modules.copy()
    
    for k in modules:
        if k not in TO_IGNORE:
            sys.modules.pop(k)
    
    #Load back
    LoadGrasshopepr(gh_files)
    

def Reload():
    try:
        if "Grasshopper" not in sys.modules.keys():
            clr.AddReference('Grasshopper, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803')
            #import Grasshopper
            LoadGrasshopepr()
        else:
            #import Grasshopper
            #import franky
            ReloadGrasshopper()
    except:
        System.Windows.Forms.MessageBox.Show(traceback.format_exc(), 'Failed to reload Grasshopper!')

if __name__ == "__main__":
    try:
        if "Grasshopper" not in sys.modules.keys():
            clr.AddReference('Grasshopper, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803')
            #import Grasshopper
            LoadGrasshopepr()
        else:
            #import Grasshopper
            #import franky
            ReloadGrasshopper()
    except:
        System.Windows.Forms.MessageBox.Show(traceback.format_exc(), 'Failed to reload Grasshopper!')