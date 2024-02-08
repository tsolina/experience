import win32com.client
CATIA = win32com.client.dynamic.Dispatch("CATIA.Application")

class Reference():
    pass

def _get_safe_array(com_obj, method: str, tuple_length: int) -> tuple:
    vba_function_name = 'get_safe_array'
    vba_code = f"""
    Public Function {vba_function_name}({com_obj.__class__.__name__})
        Dim arr({tuple_length})
        {com_obj.__class__.__name__}.{method} arr
        {vba_function_name} = arr
    End Function
    """

    return CATIA.SystemService.Evaluate(vba_code, 1, vba_function_name, [com_obj])

def _get_reference(com_obj, method, i_pos: int):
    vba_function_name = 'get_ref'
    vba_code = f"""
    Public Function {vba_function_name}({com_obj.__class__.__name__} as HybridShapeCircle, i_pos as Integer) As Reference
        Dim p1 as Reference, obj as Object
        Set obj = {com_obj.__class__.__name__}
        MsgBox typename({com_obj.__class__.__name__}) & " " & typename(obj) 
        obj.{method} {i_pos}, p1
        Set {vba_function_name} = p1
    End Function
    """    
    print(vba_code)
    # print(dir(com_obj))
    return CATIA.SystemService.Evaluate(vba_code, 1, vba_function_name, [com_obj, i_pos])

def _get_section_from_loft(com_obj, method, i_pos: int) -> tuple:
    vba_function_name = 'get_section_from_loft'
    vba_code = f"""
    Public Function {vba_function_name}({com_obj.__class__.__name__} as HybridShapeLoft, i_pos as Integer) as Variant()
        Dim oCrv as Reference, oOri as Long, oPoint as Reference, obj as Object
        Set obj = {com_obj.__class__.__name__}
        'MsgBox typename({com_obj.__class__.__name__}) & " " & typename(obj) 
        obj.{method} i_pos, oCrv, oOri, oPoint
        {vba_function_name} = Array(oCrv, oOri, oPoint)
    End Function
    """    
    print(vba_code)
    # print(dir(com_obj))
    return CATIA.SystemService.Evaluate(vba_code, 3, vba_function_name, [com_obj, i_pos])

def _get_section_from_loft_ref(com_obj, method, i_pos: int) -> tuple:
    vba_function_name = 'get_section_from_loft'
    vba_code = f"""
    Public Function {vba_function_name}({com_obj.__class__.__name__} as HybridShapeLoft, i_pos as Integer) as Variant
        Dim oCrv as Reference, oOri as Long, oPoint as Reference', obj as Object
        'Set obj = {com_obj.__class__.__name__}
        'MsgBox typename({com_obj.__class__.__name__}) & " " & typename(obj) 
        'obj.{method} i_pos, oCrv, oOri, oPoint
        {com_obj.__class__.__name__}.{method} i_pos, oCrv, oOri, oPoint
        'dim rVal(2), rVal1
        'Set rVal(0) = oCrv
        'rVal(1) = oOri
        'Set rVal(2) = oPoint
        '{vba_function_name} = rVal

        'rVal1 = Array(oCrv, oOri, oPoint)
        '{vba_function_name} = rVal1
        {vba_function_name} = Array(oCrv, oOri, oPoint)
        'set {vba_function_name} = oCrv
        'rVal = Array(oCrv, oOri, oPoint
        
        'MsgBox Typename({vba_function_name})
    End Function
    """    
    print(vba_code)
    # print(dir(com_obj))
    return CATIA.SystemService.Evaluate(vba_code, 3, vba_function_name, [com_obj, i_pos])

def _get_section(com_obj, method: str, i_pos: int) -> tuple:
    vba_function_name = 'get_section'
    vba_code = f"""
    Public Function {vba_function_name}({com_obj.__class__.__name__} as HybridShapeLoft, i_pos as Integer) as Variant
        Dim oCrv as Reference, oOri as Long, oPoint as Reference
        {com_obj.__class__.__name__}.{method} i_pos, oCrv, oOri, oPoint
        {vba_function_name} = Array(oCrv, oOri, oPoint)
    End Function
    """
    return CATIA.SystemService.Evaluate(vba_code, 3, vba_function_name, [com_obj, i_pos])

def get_section_from_loft(self, i_rank: int) -> tuple[Reference, int, Reference]:   
    vba_function_name = 'get_section'
    vba_code = f"""
    Public Function {vba_function_name}(obj as HybridShapeLoft, i_pos as Integer) as Variant
        Dim oCrv as Reference, oOri as Long, oPoint as Reference
        obj.GetSectionFromLoft i_pos, oCrv, oOri, oPoint
        {vba_function_name} = Array(oCrv, oOri, oPoint)
    End Function
    """
    return self.application().system_service().evaluate(vba_code, 3, vba_function_name, [self._com, i_rank])



def get_multi(params, ins, outs) -> tuple:
    com_type = ins[0]
    method = ins[1]
    str_ins = ins[2:]
    dim_in = ", ".join([f"in{i} As {value}" for i, value in enumerate(str_ins)])
    if len(dim_in):
        dim_in = ", " + dim_in
    dim_out = ", ".join([f"out{i} As {value}" for i, value in enumerate(outs)])
    args_in = ", ".join([f"in{i}" for i, _ in enumerate(str_ins)])
    args_out = ", ".join([f"out{i}" for i, _ in enumerate(outs)])
    if len(dim_in):
        args = ", ".join((args_in, args_out))
    else:
        args = args_out
    vba_function_name = "func"
    vba_code = f""" 
        Public Function {vba_function_name}(obj as {com_type}{dim_in}) as Variant
            Dim {dim_out}
            obj.{method} {args}
            {vba_function_name} = Array({args_out})
        End Function
    """
    print(vba_code)
    return CATIA.SystemService.Evaluate(vba_code, 1, vba_function_name, params)

Part = CATIA.ActiveEditor.ActiveObject
HSF = Part.HybridShapeFactory
sel = CATIA.ActiveEditor.Selection
vp = sel.VisProperties

# sel.Clear()
# sel.Add(Part.HybridBodies.Item(1))
# print(vp.GetLayer(None, None))
v = ()

shape = Part.HybridBodies.Item(1).HybridShapes.Item(1)
#c1 = Part.HybridBodies.Item(1).HybridShapes.Item(2)
#c2 = Part.HybridBodies.Item(1).HybridShapes.Item(3)
try:
    arr = (100,100,100)
    #print(shape.Name, shape.GetSectionFromLoft(1))
    #print(shape.Name, _get_section(shape, "GetSectionFromLoft", 1)[0].displayName)
    #print("obj", _get_reference(circle, "GetAxis", 2).Name)
    # print(_get_safe_array(circle, "GetPlaneNormal", 2))
    #print("fun: ", get_multi((shape, 1),("HybridShapeLoft", "GetSectionFromLoft", "Integer"),("Reference", "Long", "Reference")))
    #print(shape.ModifySectionCurve(c1, c2))
    #print("fun: ", get_multi((shape, c1, c2),("HybridShapeLoft", "ModifySectionCurve", "Reference", "Reference"), ("Reference", "Reference", "Long")))
    #print("plane: ", shape.SetPosition(50, 30, 25))
    #print("fun: ", get_multi(([shape]), ("Plane", 'GetPosition'), ("Double", "Double", "Double")))
    #print("this:? ", _get_safe_array(shape, "GetPosition", 2))
    #Part.Update()
    print("aaa:", shape.GetAngleLawTypes())

except Exception as e:
    print("exception: ", e)
    
input("Wait for Enter...")