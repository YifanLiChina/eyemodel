#!/usr/bin/python
# coding=utf-8

import bpy
import sys
import os

#dir = os.path.dirname(bpy.data.filepath)
dir = "C:\\Users\\localadmin\\Documents\\GitHub\\eyemodel"
if not dir in sys.path:
    sys.path.append(dir)

import eyemodel

#   ^
#   |    .-.
#   |   |   | <- Head
#   |   `^u^'
# Y |      ¦V <- Camera    (As seen from above)
#   |      ¦
#   |      ¦
#   |      o <- Target
#
#     ----------> X
#
# +X = left
# +Y = back
# +Z = up

with eyemodel.Renderer() as r:
    r.eye_target = [0, -1000, 0]
    r.camera_position = [20, -50, -10]
    r.camera_target = [0, -r.eye_radius, 0]
    r.eye_closedness = 0.0
    r.iris = "light"
    
    # all the parameters can be found in init.py
    r.eye_radius = 24/2
    r.eye_position = [0,0,0]
    r.eye_up = [0,0,1]
    r.iris = "dark"
    r.cornea_refractive_index = 1.336
    r.pupil_radius = 4/2
    r.focus_distance = None
    r.fstop = 2.0
    r.render_samples = 20
    r.render_seed = None
    r.camera_noise_seed = None
    
    r.lights = [
        #eyemodel.Light(
        #    type="sun",
        #    location = [10, -10, 100],
        #    strength = 10,
        #    target = [0,0,0]),
        eyemodel.Light(
            strength = 1,
            location = [15, -50, -10],
            target = r.camera_target),
        eyemodel.Light(
            strength = 1,
            location = [25, -50, -10],
            target = r.camera_target)
    ]

    #r.render_samples = 50
    #r.render("example.png", "example.m")
    r.render("example1.png")
    # The file is saved under "C:\Program Files\Blender Foundation\Blender"
    # Remember to run as an administrater