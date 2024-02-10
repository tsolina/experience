# - this example shows the possibility to directly work in product context -
import traceback

try:
    from experience import ProductReady

    with ProductReady() as cat:
        # - perform the ckeck if part is ready and executes the code -
        print("product is ready")

        # - access Application object from wrapper -     
        app = cat.app

        # - if product contains subproducts: -
        if cat.root.occurrences().count():
            # - print instance title of first subproduct - 
            print(cat.root.occurrences().item(1).instance_occurrence_of().title())

        # - print 3DExperience name -
        print(app.name())
        
except Exception as e:
    # - throws the error in case that product was not active -
    traceback_str = traceback.format_exc()
    print("traceback", traceback_str)

input("Press enter to continue...")