#
#   Copyright (c) 2001-2019, The Foundry Group LLC
#   All Rights Reserved. Patents granted and pending.
#

"""MODO TD API - A more 'pythonic' wrapper around the core MODO Python API intended to make performing common
coding tasks easier for TDs.

.. moduleauthor:: Gwynne Reddick <gwynne.reddick@thefoundry.co.uk>

"""

__version__ = "0.0.1"

import lx
import dialogs
import util

import scene
from scene import Scene, sceneList, current

from item import *

from channel import Channel, ChannelRead, ChannelWrite, ChannelTriple, Envelope, Keyframes

from mathutils import Vector3, Matrix3, Matrix4, Quaternion

from meshgeometry import MeshComponentContainer, MeshEdge, MeshEdges, MeshGeometry, MeshMaps, MeshPolygon
from meshgeometry import MeshPolygons, MeshVertex, MeshVertices, MorphMap, RGBAMap, RGBMap, UVMap, VertexMap
from meshgeometry import WeightMap, VertexNormalMap
