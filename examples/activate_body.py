from experience import PartReady

with PartReady() as cat:
    test = cat.part.bodies().add().name("test")
    other = cat.part.bodies().add().name("other")
    in_work =  cat.part.in_work_object(test)

    cat.part.shape_factory().add_new_pad()