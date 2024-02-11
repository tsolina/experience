import traceback
# - example to search for an item in database using indexed and database search and open the item in editor -

from experience import experience_application, Part

# - accessing application -
app = experience_application()

# - accessing search service -
search = app.services().search_service()

# - indexed search -
i_search = search.indexed_search().types("VPMReference , 3DShape , Material Part").predicate("ds6w:label", "prd*").max_search_result_count(20).sort_by("ds6w:label", 1).search()
print(i_search.results().count(), "indexed results found")

# - some valid id -
item_id = "prd-*-00012131"

# - database search,  -
db_search = search.database_search().base_type("VPMReference").add_easy_criteria("PLM_ExternalID", item_id)
search.search()

plm_entities = db_search.results()
print(plm_entities.count(), "same as", db_search.search_count(), "results found")

if db_search.search_count():
    # - opening serched item in the editor -
    editor = app.services().open_service().plm_open(plm_entities.item(1))
    
    # - do some action with open element, part in this example -
    print(editor.active_object(Part).main_body().name())

input("Press enter to continue...")