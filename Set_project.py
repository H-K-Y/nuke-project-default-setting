#!/usr/bin/env python
# -*- coding:utf-8 -*-

import nuke,os,ConfigParser

def Set_project():

    if os.path.exists(os.path.join(os.path.expanduser("~"),".nuke","Set_project.ini")):
        pass
    else:
        f = ConfigParser.ConfigParser()
        f.add_section("Set_project")
        f.set("Set_project", "width", "1920")
        f.set("Set_project", "height", "1080")
        f.set("Set_project", "pixel aspect", "1")
        f.set("Set_project", "fps", "24")
        f.set("Set_project", "Write channels", "rgb")
        f.set("Set_project", "Write node codec", "ap4h")
        f.set("Set_project", "Write mov write time code", "False")
        f.set("Set_project", "Viewer full_frame_processing", "False")
        f.set("Set_project", "Read raw data", "False")
        f.set("Set_project", "Write raw data", "False")
        f.set("Set_project", "Rendering automatically create a rendering path", "False")

        f.write(open(os.path.join(os.path.expanduser("~"),".nuke","Set_project.ini"),"w"))

    f = ConfigParser.ConfigParser()
    f.read(os.path.join(os.path.expanduser("~"),".nuke","Set_project.ini"))

    size = [f.get("Set_project", "width"),f.get("Set_project", "height"),"0","0",f.get("Set_project", "width"),f.get("Set_project", "height"),f.get("Set_project", "pixel aspect"),f.get("Set_project", "width")+"*"+f.get("Set_project", "height")]
    nuke.knobDefault("Root.format"," ".join(size))
    nuke.knobDefault("Root.fps",f.get("Set_project", "fps"))
    nuke.knobDefault("Write.channels",f.get("Set_project", "Write channels"))
    nuke.knobDefault("Write.mov.meta_codec",f.get("Set_project", "Write node codec"))
    nuke.knobDefault("Write.mov.mov64_write_timecode",f.get("Set_project", "Write mov write time code"))
    nuke.knobDefault("Viewer.full_frame_processing",f.get("Set_project", "Viewer full_frame_processing"))
    nuke.knobDefault("Read.raw",f.get("Set_project", "Read raw data"))
    nuke.knobDefault("Write.raw",f.get("Set_project", "Write raw data"))
    if f.get("Set_project", "Rendering automatically create a rendering path") == "False":
        pass
    else:
        nuke.addBeforeRender(chuangjian)


    menubar = nuke.menu("Nuke");
    m = menubar.addMenu("Set the project default")
    m.addCommand("Set the project default", Set_project_ui)





def Set_project_ui():

    f = ConfigParser.ConfigParser()
    f.read(os.path.join(os.path.expanduser("~"), ".nuke", "Set_project.ini"))


    Write_channels = ["all","rgb","rgba","alpha"]
    Write_channels.remove(f.get("Set_project", "Write channels"))
    Write_channels.insert(0,f.get("Set_project", "Write channels"))

    Write_codec = {"Apple_ProRes_4444": "ap4h",
                   "Apple_ProRes_4444_XQ": "ap4x",
                   "Apple_ProRes_422": "apcn",
                   "Apple_ProRes_422_HQ": "apch",
                   "Apple_ProRes_422_LT": "apcs",
                   "Apple_ProRes_422_Proxy": "apco",
                   "Component_Video": "yuv2",
                   "H.264": "avc1",
                   "MPEG-4_Video": "mp4v"
                   }


    p = nuke.Panel("Set the project default")
    p.addSingleLineInput("width",f.get("Set_project", "width"))
    p.addSingleLineInput("height", f.get("Set_project", "height"))
    p.addSingleLineInput("pixel aspect", f.get("Set_project", "pixel aspect"))
    p.addSingleLineInput("fps", f.get("Set_project", "fps"))
    p.addEnumerationPulldown("Write default channels"," ".join(Write_channels))
    p.addEnumerationPulldown("Write MOV default encoding"," ".join(Write_codec.keys()))
    p.addBooleanCheckBox('Write MOV automatically check "write time code"',panduan(f.get("Set_project", "Write mov write time code")))
    p.addBooleanCheckBox('Viewer automatically check "full_frame_processing"',panduan(f.get("Set_project", "Viewer full_frame_processing")))
    p.addBooleanCheckBox("Read raw data",panduan(f.get("Set_project", "Read raw data")))
    p.addBooleanCheckBox("Write raw data",panduan(f.get("Set_project", "Write raw data")))
    p.addBooleanCheckBox("Rendering automatically create a rendering path",panduan(f.get("Set_project", "Rendering automatically create a rendering path")))

    if p.show() :
        f = ConfigParser.ConfigParser()
        f.add_section("Set_project")
        f.set("Set_project", "width", p.value("width"))
        f.set("Set_project", "height", p.value("height"))
        f.set("Set_project", "pixel aspect", p.value("pixel aspect"))
        f.set("Set_project", "fps", p.value("fps"))
        f.set("Set_project", "Write channels", p.value("Write default channels"))
        f.set("Set_project", "Write node codec", Write_codec[p.value("Write MOV default encoding")])
        f.set("Set_project", "Write mov write time code", str(p.value('Write MOV automatically check "write time code"')))
        f.set("Set_project", "Viewer full_frame_processing", str(p.value('Viewer automatically check "full_frame_processing"')))
        f.set("Set_project", "Read raw data", str(p.value("Read raw data")))
        f.set("Set_project", "Write raw data", str(p.value("Write raw data")))
        f.set("Set_project", "Rendering automatically create a rendering path", str(p.value("Rendering automatically create a rendering path")))

        f.write(open(os.path.join(os.path.expanduser("~"), ".nuke", "Set_project.ini"), "w"))

    else:
        pass




def panduan(a):
    if a == "False":
        return False
    else:
        return True

def chuangjian():
    file = os.path.dirname(nuke.filename(nuke.thisNode()))
    if os.path.exists(file):
        pass
    else:
        os.makedirs(file)




