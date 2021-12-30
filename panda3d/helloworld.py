from direct.showbase.ShowBase import ShowBase
from panda3d.core import AmbientLight
from direct.actor.Actor import Actor
from panda3d.core import Vec4
import simplepbr

class MyApp(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        simplepbr.init()
        self.camera.setPos(0, 0, 0)
        render.setShaderAuto()
        self.scene = self.loader.loadModel("models/environment") # Load the environment model.
        self.scene.reparentTo(self.render) # Reparent the model to render.
        self.scene.setScale(0.25, 0.25, 0.25) # Apply scale and position transforms on the model.
        self.scene.setPos(0, 120, 0) # was -8, 42, 0 # (left/right, distance, vertical)

        ambientLight = AmbientLight("ambient light")
        ambientLight.setColor(Vec4(1, 1, 1, 1))
        self.ambientLightNodePath = render.attachNewNode(ambientLight)
        render.setLight(self.ambientLightNodePath)
        

        self.linearPosition = 30
        self.verticalPosition = 3
        self.pandaActor = Actor("models/Face1.gltf") #Actor("models/face1.bam")
        self.pandaActor.setScale(3, 3, 3)
        self.pandaActor.setPos(0, self.linearPosition, self.verticalPosition)
        self.pandaActor.getChild(0).setHpr(0, 180, 360)
        self.pandaActor.reparentTo(self.render)

        

        self.accept('space', self.jumpEvent)
        self.accept('w', self.moveEvent)

    def jumpEvent(self):
        print("jumping")
        self.verticalPosition = self.verticalPosition + 1
        self.pandaActor.setPos(0, self.linearPosition, self.verticalPosition)
        print(self.verticalPosition)

    def moveEvent(self):
        print("moving")
        self.linearPosition = self.linearPosition - 1
        self.pandaActor.setPos(0, self.linearPosition, self.verticalPosition)
        print(self.linearPosition)

app = MyApp()
app.run()