# example to modify properties of product and access part
# product must be open and one part attached to it
from experience import *

# accessing application
app = experience_application()

root = app.active_editor().active_object(VPMRootOccurrence)

# accessing instance and setting the title
prod_instance = root.occurrences().item(1).instance_occurrence_of().title("Instance.1").as_pyclass(VPMInstance)

# setting the title to reference
prod_reference = prod_instance.reference_instance_of().title("Reference")

# to access part
part = prod_instance.reference_instance_of().rep_instances().item(1).reference_instance_of().part()
print(part.main_body().name())

input("Done")