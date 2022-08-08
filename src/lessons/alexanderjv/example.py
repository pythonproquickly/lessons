import hou
import viewerstate.utils as su

#from stateutils import ancestorObject
from stateutils import sopGeometryIntersection
from stateutils import cplaneIntersection


class State(object):
    MSG = "LMB to add points to the construction plane."

    def __init__(self, state_name, scene_viewer):                
        self.state_name = state_name
        
        self.scene_viewer = scene_viewer
       
        self.pressed = False

        self.collisiongeo = None

        self._cursor = hou.SimpleDrawable(
            scene_viewer, 
            hou.drawablePrimitive.Sphere, 
            state_name + "_cursor"
        )
        
        self._cursor.enable(True)
        
        self._cursor.show(False)
             
    def pointCount(self):
        """ This is how you get the number of instances 
            in a multiparm. 
        """
        try:
            multiparm = self.node.parm("points")
            return multiparm.evalAsInt()
        except:
            return 0

    def start(self):
        if not self.pressed:
            self.scene_viewer.beginStateUndo("Add point")
            self.index = self.pointCount()
            multiparm = self.node.parm("points")
            multiparm.insertMultiParmInstance(self.index)

        self.pressed = True

    def finish(self):
        if self.pressed:
            self.scene_viewer.endStateUndo()
            
        self.pressed = False


    def onEnter(self, kwargs):    
        self.node = kwargs["node"]
        
        inputs = self.node.inputs()
        
        if inputs and inputs[0]:
            self.collisiongeo = inputs[0].geometry()

        self.scene_viewer.setPromptMessage( State.MSG )

        
        
    def onInterrupt(self,kwargs):    
        self.finish()
        
        self._cursor.show(False)

        
    def onResume(self, kwargs):    
        self.scene_viewer.setPromptMessage( State.MSG )

        
    def onMouseEvent(self, kwargs):
        """ Find the position of the point to add by 
            intersecting the construction plane. 
        """
        node = kwargs["node"]
        ui_event = kwargs["ui_event"]
        device = ui_event.device()
        
        reason = ui_event.reason()
        
        ray_origin, ray_dir = ui_event.ray()
        
        
        if self.collisiongeo:
            hit, position, norm, uvw = su.sopGeometryIntersection(self.collisiongeo, ray_origin, ray_dir)
        
        # Intersect in local space!
        intersected = -1
        
        if node.inputs() and node.inputs()[0]:
            # Grab the incoming geometry
            geometry = node.inputs()[0].geometry()
            intersected, position, _, _ = su.sopGeometryIntersection(geometry, ray_origin, ray_dir)
            
        if intersected < 0:
            # Either there was no incoming geometry or the ray missed, so
            # try intersecting the construction plane
            position = su.cplaneIntersection(self.scene_viewer, ray_origin, ray_dir)

        # Find the container Geo... this is often just node.parent(), but we need to
        # handle the case where the node is inside one or more subnets
        parent = su.ancestorObject(kwargs["node"])
        
        # Use the container's transform to display the cursor in world space
        parent_xform = parent.worldTransform()
        world_pos = position * parent_xform
        
        # Build a Matrix4 from the world space translate
        m = hou.hmath.buildTranslate(world_pos)
        self._cursor.setTransform(m)
        self._cursor.show(True)

        # Create/move point if LMB is down
        if device.isLeftButton():
            self.start()
            # set the point position
            self.node.parm("usept%d" % self.index).set(1)
            self.node.parmTuple("pt%d" % self.index).set(position)
            
        else:
            self.finish()
            
        return True


def createViewerStateTemplate(kwargs):
    """ Mandatory entry point to create and return the viewer state 
        template to register. """

    state_typename = kwargs["type"].definition().sections()["DefaultState"].contents()
    state_label = "Cable demo"
    state_cat = hou.sopNodeTypeCategory()

    template = hou.ViewerStateTemplate(state_typename, state_label, state_cat)
    template.bindFactory(State)
    template.bindIcon(kwargs["type"].icon())

    return template