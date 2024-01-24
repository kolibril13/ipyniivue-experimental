import importlib.metadata
import pathlib

import anywidget
import traitlets

try:
    __version__ = importlib.metadata.version("ipyniivue_experimental")
except importlib.metadata.PackageNotFoundError:
    __version__ = "unknown"

############ This code block will go to __init__.py 

import anywidget 
import pathlib

class AnyNiivue(anywidget.AnyWidget):
  path_root = pathlib.Path(__file__).parent.parent.parent
  _esm = path_root / "src" / "ipyniivue_experimental"/ "static" / "widget_send.js"

  def load_volumes(self, volume_list):
    self.send({ "type": "api", "func": "loadVolumes", "args": [volume_list] })

  def load_meshes(self, mesh_list):
    self.send({ "type": "api", "func": "loadMeshes", "args": [mesh_list] })
############
    

class AnyNiivueOpacity(anywidget.AnyWidget):
  path_root = pathlib.Path(__file__).parent.parent.parent
  _esm = path_root / "src" / "ipyniivue_experimental"/ "static" / "widget_traitlet.js"
  opacity = traitlets.Float(1.0).tag(sync=True)
