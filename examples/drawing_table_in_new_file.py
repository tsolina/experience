from experience import *



def create_new_drawing(catia: Application) -> DrawingRoot:
    drawing_doc =  catia.services().new_service().plm_create("Drawing")
    return drawing_doc.active_object(DrawingRoot)

def create_new_view(sheet: DrawingSheet) -> DrawingView:
    return sheet.views().add("First view").x(200).y(500).activate()

def create_new_table(view: DrawingView) -> DrawingTable:
    return view.tables().add(50, 50, 5, 5, 50, 50)

def apply_outer_edges(table: DrawingTable):
    # - set top left cell borders-
    table.set_cell_border(DrawingCellBorder(0, 1, 1).slash(True).bottom(True).right(True))

    # - set bottom right cell borders-
    table.set_cell_border(DrawingCellBorder(0, 5, 5).slash(True).top(True).left(True))

    # - set top right cell borders-
    table.set_cell_border(DrawingCellBorder(0, 1, 5).backslash(True).bottom(True).left(True))

    # - set bottom left cell borders-
    table.set_cell_border(DrawingCellBorder(0, 5, 1).backslash(True).top(True).right(True))

def apply_inner_edges(table: DrawingTable):
    # - set top left cell borders-
    table.set_cell_border(DrawingCellBorder().col(2).row(2).slash(True).top(True).left(True))

    # - set bottom right cell borders-
    table.set_cell_border(DrawingCellBorder(0, 4, 4).slash(True).bottom(True).right(True))

    # - set top right cell borders-
    table.set_cell_border(DrawingCellBorder(0, 2, 4).backslash(True).top(True).right(True))

    # - set bottom left cell borders-
    table.set_cell_border(DrawingCellBorder(0, 4, 2).backslash(True).bottom(True).left(True))

def apply_text(table: DrawingTable):
    table.parent(DrawingTables).parent(DrawingView).texts().add("drawing table:", 50, 75).set_font_size(0, 0, 10).anchor_position(
        CatTextAnchorPosition.catBaseLeft).frame_type(CatTextFrameType.catRectangle)

    table.set_cell_string(3, 3, "Generated by python").set_cell_alignment(3, 3, CatTablePosition.CatTableMiddleCenter)
    table.get_cell_object(3, 3).set_font_size(0, 0, 7)

app = experience_application()
drawing = create_new_drawing(app)
view = create_new_view(drawing.active_sheet())
table = create_new_table(view)
apply_outer_edges(table)
apply_inner_edges(table)
apply_text(table)

print("done")