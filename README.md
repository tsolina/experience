# experience is 3DExperience wrapper for Catvba/CATScript API

# beta software:
currently part infrastructure, assembly structrue, drawing, measure are fully supported 

# requirements:
3DExperience installed and running on the system
pywin32 module is used to access raw COM object

# references:
complete documentation is stored in installation folder
"C:\Program Files\Dassault Systemes\"release"\win_b64\code\bin\DSYAutomation.chm"

# motivation:
## to return immutable output arguments in swift fashion:

    obj.get_coordinates() -> tuple(float, float, float)
    
    instead 
    
    Sub GetCoordinates(CATSafeArrayVariant oPoint)
      dim coords(2)
      obj.GetCoordinates coords
    End Sub
      
    obj.get_element(i_position) -> tuple(HybShpPolylineElement, HybShpPolylineRadius)
    
    instead 
    
    Sub GetElement(long iPosition,Reference oElement,Length oRadius) 
       Dim HybShpPolylineElement As Reference
       Dim HybShpPolylineRadius As Reference
       HybShpPolyline.GetElement 1, HybShpPolylineElement,HybShpPolylineRadius
    End Sub

# specialities:
## all properties are replaced with functions:
    sel = app.active_editor().selection()

## type conversions are included:
    p = app.active_editor().active_object(Part)

## setters and getters are now one function:
    print(p.main_body().name("test").name())

## all objects are chainable:
    sel.clear().add(p.hybrid_bodies().item(1)).copy().clear().add(p.hybrid_bodies()).paste().clear()

# examples:
examples will be stored as separate structure
