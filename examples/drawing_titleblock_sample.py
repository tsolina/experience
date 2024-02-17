import traceback

try:
    from experience import * # DrawingReady

    with DrawingReady() as cat:
        sel = cat.app.active_editor().selection()
        sheet = cat.drawing.active_sheet()
        view = sheet.views().item(2) # get background view
        texts = view.texts()
        text = {}
        fact = view.factory_2d()
        active_view = sheet.views().active_view()

        def cat_init() -> bool:
            sel.clear()
            cat.app.hso_synchronized(False).refresh_display(False)
            return True

        def get_macro_id() -> str:
            return "Drawing_Titleblock_Sample1"
        
        def cat_check_ref(mode: int) -> int:
            for i in range(1, texts.count()+1):
                text = texts.item(i)
                whole_name = text.name()
                left_name = whole_name[:10]
                if left_name == "Reference_":
                    refText = "Reference_" + get_macro_id()
                    if mode == 1:
                        return 1
                    elif text.name != refText:
                        return 1
                    else:
                        return 0

            if mode == 1:
                return 0
            else:
                return 1
        
        def get_width() -> float:
            return sheet.get_paper_width()
        
        def get_height() -> float:
            return sheet.get_paper_height()
        
        def get_offset() -> float:
            if sheet.paper_size() == 2 or sheet.paper_size() == 3 or sheet.paper_size() == 13 and (get_width() > 594 or get_height() > 594):
                return 20
            else:
                return 10
            
        def get_ov() -> float:
            return get_offset()
        
        def get_oh() -> float:
            return get_width() - get_offset()
            
        def get_ruler_length() -> float:
            return 200
        
        def col(idx: int) -> int:
            cols = [-190, -170, -145, -45, -25, -20]
            return cols[idx - 1]

        def row(idx: int) -> int:
            rows = [4, 17, 30, 45, 60]
            return rows[idx - 1]
        
        def get_nb_of_revisions() -> int:
            return 9
        
        def get_rev_letter(index: int) -> str:
            return chr(ord("A") + index - 1)
        
        def get_context() -> str:
            return "DRW"
        
        def get_date() -> str:
            from win32com.client import Dispatch
            shell = Dispatch('WScript.Shell')
            imposed_date = shell.ExpandEnvironmentStrings("%IMPOSED_DATE%")
            if imposed_date == "%IMPOSED_DATE%":
                from datetime import date
                imposed_date = date.today()

            return str(imposed_date)

        def cat_create_reference():
            text = texts.add("", get_width() - get_offset(), get_offset()).name("Reference_" + get_macro_id())

        def get_display_format() -> str:
            return ["Letter","Legal","A0","A1","A2","A3","A4","A","B","C","D","E","F","User"][sheet.paper_size()]

        def get_col_rev(idx: int) -> int:
            cols = [-190, -175, -140, -20]
            return cols[idx - 1]
        
        def get_rev_row_height() -> float:
            return 10

        def cat_frame_standard() -> tuple[int, int, int, float, float]:
            cst_1 = 74.2
            cst_2 = 52.5

            if sheet.orientation() ==  0 and ( sheet.paper_size() == 2 or sheet.paper_size() == 4 or sheet.paper_size() == 6) or sheet.orientation() == 1 and (
                    sheet.paper_size == 3 or  sheet.paper_size == 5):
                cst_1 = 52.5
                cst_2 = 74.2

            nb_cm_h = int(.5 * get_width() / cst_1)
            nb_cm_v = int(.5 * get_height() / cst_2)
            ruler = int((nb_cm_h - 1) * cst_1 / 50) * 100

            if get_ruler_length() < ruler:
                ruler = get_ruler_length()

            return (nb_cm_h, nb_cm_v, ruler, cst_1, cst_2)
        
        def cat_frame_border():
            fact.create_line(get_ov(), get_ov(), get_oh(), get_ov()).name("Frame_Border_Bottom")
            fact.create_line(get_oh(), get_ov(), get_oh(), get_height() - get_offset()).name("Frame_Border_Left")
            fact.create_line(get_oh(), get_height() - get_offset(), get_ov(), get_height() - get_offset()).name("Frame_Border_Top")
            fact.create_line(get_ov(), get_height() - get_offset(), get_ov(), get_ov()).name("Frame_Border_Right")
            print("frame added")

        def cat_frame_centring_mark(nb_cm_h: int, nb_cm_v: int, ruler: int, cst_1: float, cst_2: float):
            fact.create_line(.5 * get_width(), get_height() - get_offset(), .5 * get_width(), get_height()).name("Frame_CentringMark_Top")
            fact.create_line(.5 * get_width(), get_ov(), .5 * get_width(), 0).name("Frame_CentringMark_Bottom")
            fact.create_line(get_ov(), .5 * get_height(), 0, .5 * get_height()).name("Frame_CentringMark_Left")
            fact.create_line(get_width() - get_offset(), .5 * get_height(), get_width(), .5 * get_height()).name("Frame_CentringMark_Right")
            for i in range(nb_cm_h + 1, ruler // (2 * int(cst_1)), -1):
                if (i * cst_1 < .5 * get_width() - 1):
                    x = .5 * get_width() + i * cst_1
                    fact.create_line(x, get_ov(), x, .25 * get_offset()).name("Frame_CentringMark_Bottom_" + str(int(x)))
                    x = .5 * get_width() - i * cst_1
                    fact.create_line(x, get_ov(), x, .25 * get_offset()).name("Frame_CentringMark_Bottom_" + str(int(x)))
            for i in range(1, nb_cm_h - 1 + 1):
                if (i * cst_1 < .5 * get_width() - 1):
                    x = .5 * get_width() + i * cst_1
                    fact.create_line(x, get_height() - get_offset(), x, get_height() - .25 * get_offset()).name("Frame_CentringMark_Top_" + str(int(x)))
                    x = .5 * get_width() - i * cst_1
                    fact.create_line(x, get_height() - get_offset(), x, get_height() - .25 * get_offset()).name("Frame_CentringMark_Top_" + str(int(x)))
            for i in range(1, nb_cm_v - 1 + 1):
                if (i * cst_2 < .5 * get_height() - 1):
                    y = .5 * get_height() + i * cst_2
                    fact.create_line(get_ov(), y, .25 * get_offset(), y).name(("Frame_CentringMark_Left_" + str(int(y))))
                    fact.create_line(get_oh(), y, get_width() - .25 * get_offset(), y).name(("Frame_CentringMark_Right_" + str(int(y))))
                    y = .5 * get_height() - i * cst_2
                    fact.create_line(get_ov(), y, .25 * get_offset(), y).name(("Frame_CentringMark_Left_" + str(int(y))))
                    fact.create_line(get_oh(), y, get_width() - .25 * get_offset(), y).name(("Frame_CentringMark_Right_" + str(int(y))))
            print("centering marks added")

        def cat_frame_text(nb_cm_h: int, nb_cm_v: int, ruler: int, cst_1: float, cst_2: float):
            for i in range(nb_cm_h, ruler // (2 * int(cst_1)) + 1, -1):
                n = "Frame_Text_Bottom_1_" + chr(65 + nb_cm_h - i)
                texts.add(chr(65 + nb_cm_h - i), .5 * get_width() + (i - .5) * cst_1, .5 * get_offset()).anchor_position(5).name(n)
                n = "Frame_Text_Bottom_2_" + chr(64 + nb_cm_h + i)
                texts.add(chr(64 + nb_cm_h + i), .5 * get_width() - (i - .5) * cst_1, .5 * get_offset()).anchor_position(5).name(n)

            for i in range( 1, nb_cm_h + 1 ): # - 1
                t = chr(65 + nb_cm_h - i)
                texts.add(t, .5  * get_width() + (i - .5) * cst_1, get_height() - .5 * get_offset()).anchor_position(5).angle(-90).name("Frame_Text_Top_1_" + t)
                t = chr(64 + nb_cm_h + i)
                texts.add(t, .5  * get_width() - (i - .5) * cst_1, get_height() - .5 * get_offset()).anchor_position(5).angle(-90).name("Frame_Text_Top_2_" + t)

            for i in range(1, nb_cm_v + 1):
                t = str(nb_cm_v + i)
                texts.add(t, get_width() - .5 * get_offset(), .5 * get_height() + (i - .5) * cst_2).anchor_position(5).name("Frame_Text_Right_1_" + t)
                texts.add(t, .5 * get_offset(), .5 * get_height() + (i - .5) * cst_2).anchor_position(5).angle(-90).name("Frame_Text_Left_1_" + t)
                t = str(nb_cm_v - i + 1)
                texts.add(t, get_width() - .5 * get_offset(), .5 * get_height() - (i - .5) * cst_2).anchor_position(5).name("Frame_Text_Right_2_" + t)
                texts.add(t, .5 * get_offset(), .5 * get_height() - (i - .5) * cst_2).anchor_position(5).angle(-90).name("Frame_Text_Left_2_" + t)
            print("frame texts added")

        def cat_frame_ruler(ruler: int, cst_1: float):
            fact.create_line(.5 * get_width() - ruler / 2, .75 * get_offset(), .5 * get_width() + ruler / 2, .75 * get_offset()).name("Frame_Ruler_Guide")
            for i in range(1, ruler // 100 + 1):
                fact.create_line(.5 * get_width() - 50 * i, get_ov(), .5 * get_width() - 50 * i, .5 * get_offset()).name("Frame_Ruler_1_" + str(i))
                fact.create_line(.5 * get_width() + 50 * i, get_ov(), .5 * get_width() + 50 * i, .5 * get_offset()).name("Frame_Ruler_2_" + str(i))

                for j in range(1, 4 + 1):
                    fact.create_line(.5 * get_width() - 50 * i + 10 * j, get_ov(), .5 * get_width() - 50 * i + 10 * j, .75 * get_offset()).name( "Frame_Ruler_3" + str(i) + "_" + str(j) ) 
                    fact.create_line(.5 * get_width() + 50 * i - 10 * j, get_ov(), .5 * get_width() + 50 * i - 10 * j, .75 * get_offset()).name( "Frame_Ruler_4" + str(i) + "_" + str(j) ) 
            print("frame ruler added")

        def cat_frame():
            fs = cat_frame_standard()
            nb_cm_h = fs[0]
            nb_cm_v = fs[1]
            ruler = fs[2]
            cst_1 = fs[3]
            cst_2 = fs[4]

            cat_frame_border()
            cat_frame_centring_mark(nb_cm_h, nb_cm_v, ruler, cst_1, cst_2)
            cat_frame_text(nb_cm_h, nb_cm_v, ruler, cst_1, cst_2)
            cat_frame_ruler(ruler, cst_1)

        def cat_create_title_block_frame():
            fact.create_line(get_oh() + col(1), get_ov(), get_oh(), get_ov()).name("TitleBlock_Line_Bottom")
            fact.create_line(get_oh() + col(1), get_ov(), get_oh() + col(1), get_ov() + row(5)).name("TitleBlock_Line_Left")
            fact.create_line(get_oh() + col(1), get_ov()+ row(5), get_oh(), get_ov() + row(5)).name("TitleBlock_Line_Top")
            fact.create_line(get_oh(), get_ov() + row(5), get_oh(), get_ov()).name("TitleBlock_Line_Right")
            fact.create_line(get_oh() + col(1), get_ov() + row(1), get_oh() + col(5), get_ov() + row(1)).name("TitleBlock_Line_Row_1")
            fact.create_line(get_oh() + col(1), get_ov() + row(2), get_oh() + col(5), get_ov() + row(2)).name("TitleBlock_Line_Row_2")
            fact.create_line(get_oh() + col(1), get_ov() + row(3), get_oh() + col(5), get_ov() + row(3)).name("TitleBlock_Line_Row_3")
            fact.create_line(get_oh() + col(1), get_ov() + row(4), get_oh() + col(3), get_ov() + row(4)).name("TitleBlock_Line_Row_4")
            for i in range(1, get_nb_of_revisions()):
                fact.create_line(get_oh() + col(5), get_ov() + row(5) / get_nb_of_revisions() * i, get_oh(), get_ov() + row(5) / get_nb_of_revisions() * i).name("TitleBlock_Line_Row_5" + str(i))
            fact.create_line(get_oh() + col(2), get_ov() + row(1), get_oh() + col(2), get_ov() + row(3)).name("TitleBlock_Line_Column_1")
            fact.create_line(get_oh() + col(3), get_ov() + row(1), get_oh() + col(3), get_ov() + row(5)).name("TitleBlock_Line_Column_2")
            fact.create_line(get_oh() + col(4), get_ov() + row(1), get_oh() + col(4), get_ov() + row(2)).name("TitleBlock_Line_Column_3")
            fact.create_line(get_oh() + col(5), get_ov(), get_oh() + col(5), get_ov() + row(5)).name("TitleBlock_Line_Column_4")
            fact.create_line(get_oh() + col(6), get_ov(), get_oh() + col(6), get_ov() + row(5)).name("TitleBlock_Line_Column_5")
            print("title block frame added")

        def cat_create_title_block_standard():
            r1 = 2.0
            r2 = 4.0
            x = [0.0] * 6
            y = [0.0] * 8  

            x[1] = get_oh() + col(2) + 2.0
            x[2] = x[1] + 1.5
            x[3] = x[1] + 9.5
            x[4] = x[1] + 15.5
            x[5] = x[1] + 21.0
            y[1] = get_ov() + (row(2) + row(3)) / 2.0
            y[2] = y[1] + r1
            y[3] = y[1] + r2
            y[4] = y[1] + 5.5
            y[5] = y[1] - r1
            y[6] = y[1] - r2
            y[7] = 2 * y[1] - y[4]     

            if sheet.projection_method() != 0:
                x_tmp = x[1]
                x[1] = x[0] + x[4] - x[2]
                x[2] = x[0] + x[4] - x_tmp
                x[3] = x[0] + x[4] - x[3]

            fact.create_line(x[1], y[1], x[5], y[1]).name("TitleBlock_Standard_Line_Axis_1")
            fact.create_line(x[4], y[7], x[4], y[4]).name("TitleBlock_Standard_Line_Axis_2")
            fact.create_line(x[2], y[5], x[2], y[2]).name("TitleBlock_Standard_Line_1")
            fact.create_line(x[2], y[2], x[3], y[3]).name("TitleBlock_Standard_Line_2")
            fact.create_line(x[3], y[3], x[3], y[6]).name("TitleBlock_Standard_Line_3")
            fact.create_line(x[3], y[6], x[2], y[5]).name("TitleBlock_Standard_Line_4")

            fact.create_closed_circle(x[4], y[1], r1).name("TitleBlock_Standard_Circle_1")
            fact.create_closed_circle(x[4], y[1], r2).name("TitleBlock_Standard_Circle_2")
            print("title block standard added")

        def cat_links():
            vpm_ref = {}
            if sheet.views().count() >= 3:
                if sheet.views().item(3).is_generative():
                    vpm_ref = sheet.views().item(3).drawing_gen_view().get_associated_root_product(VPMReference)
                    if vpm_ref.has_attribute_value("Effectivity"):
                        texts.get_item("TitleBlock_Text_EnoviaV5_Effectivity").text(vpm_ref.get_attribute_value("Effectivity"))
                    else:
                        texts.get_item("TitleBlock_Text_EnoviaV5_Effectivity").text(vpm_ref.plm_id())
                    texts.get_item("TitleBlock_Text_Title_1").text("").insert_attribute_link(0, 0, vpm_ref, "Feature", "Name")   

            # - display sheet scale -
            param = cat.drawing.parameters().item("Drawing\\" + sheet.name() + "\\Scale")
            texts.get_item("TitleBlock_Text_Scale_1", DrawingText).text("").insert_variable(0, 0, param)

            # - display sheet format -
            disp_format = get_display_format()
            if len(disp_format) > 4:
                texts.get_item("TitleBlock_Text_Size_1").text(disp_format).set_font_size(0, 0, 3.5)
            else:
                texts.get_item("TitleBlock_Text_Size_1").text(disp_format).set_font_size(0, 0, 5)

            # - display sheet numbering
            nb_sheet = 0
            cur_sheet = 0
            if sheet.is_detail() == False:
                for it_sheet in cat.drawing.sheets():
                    if it_sheet.is_detail() == False:
                        nb_sheet += 1
                for it_sheet in cat.drawing.sheets():
                    if it_sheet.is_detail() == False:
                        cur_sheet += 1
                        it_sheet.views().item(2).texts().get_item("TitleBlock_Text_Sheet_1").text(str(cur_sheet) + "/" + str(nb_sheet))

        def cat_title_block_text():
            text_01 = "This drawing is our property; it can't be reproduced or communicated without our written agreement."
            text_02 = "SCALE"
            text_03 = "XXX"
            text_04 = "WEIGHT (kg)"
            text_05 = "XXX"
            text_06 = "DRAWING NUMBER"
            text_07 = "SHEET"
            text_08 = "SIZE"
            text_09 = "USER"
            text_10 = "XXX"                # Paper Format
            text_11 = "DASSAULT SYSTEMES"
            text_12 = "CHECKED BY:"
            text_13 = "DATE:"
            text_14 = "DESIGNED BY:"  
            text_15 = cat.app.system_service().environ("LOGNAME")
            text_15 = text_15 if not text_15 == "" else cat.app.system_service().environ("USERNAME")

            #texts.add("", 0, 0).anchor_position(1).set_font_size(0, 0, fs).name("")
            texts.add(text_01, get_oh() + col(1) + 1, get_ov() + .5 * row(1)).anchor_position(2).set_font_size(0, 0, 1.5).name("TitleBlock_Text_Rights")
            texts.add(text_02, get_oh() + col(1) + 1, get_ov() + row(2)).anchor_position(1).set_font_size(0, 0, 1.5).name("TitleBlock_Text_Scale")
            texts.add("", get_oh() + .5 * (col(1) + col(2)) - 4, get_ov() + row(1)).anchor_position(6).set_font_size(0, 0, 5).name("TitleBlock_Text_Scale_1")

            texts.add(text_04, get_oh() + col(2) + 1, get_ov() + row(2)).anchor_position(1).set_font_size(0, 0, 1.5).name("TitleBlock_Text_Weight")
            texts.add(text_05, get_oh() + .5 * (col(2) + col(3)), get_ov() + row(1)).anchor_position(6).set_font_size(0, 0, 5).name("TitleBlock_Text_Weight_1")
            texts.add(text_06, get_oh() + col(3) + 1, get_ov() + row(2)).anchor_position(1).set_font_size(0, 0, 1.5).name("TitleBlock_Text_Number")
            texts.add(text_05, get_oh() + .5 * (col(3) + col(4)), get_ov() + row(1)).anchor_position(6).set_font_size(0, 0, 4).name("TitleBlock_Text_EnoviaV5_Effectivity")
            texts.add(text_07, get_oh() + col(4) + 1, get_ov() + row(2)).anchor_position(1).set_font_size(0, 0, 1.5).name("TitleBlock_Text_Sheet")
            texts.add(text_05, get_oh() + .5 * (col(4) + col(5)), get_ov() + row(1)).anchor_position(6).set_font_size(0, 0, 5).name("TitleBlock_Text_Sheet_1")
            texts.add(text_08, get_oh() + col(1) + 1, get_ov() + row(3)).anchor_position(1).set_font_size(0, 0, 1.5).name("TitleBlock_Text_Size")

            if sheet.paper_size() == 13:
                texts.add(text_09, get_oh() + .5 * (col(1) + col(2)), get_ov() + row(2) + 2).anchor_position(6).set_font_size(0, 0, 5).name("TitleBlock_Text_Size_1")
            else:
                texts.add(text_10, get_oh() + .5 * (col(1) + col(2)), get_ov() + row(2) + 2).anchor_position(6).set_font_size(0, 0, 5).name("TitleBlock_Text_Size_1")

            texts.add(text_11, get_oh() + .5 * (col(3) + col(5)), get_ov() + .5 * (row(2) + row(3))).anchor_position(5).set_font_size(0, 0, 5).name("TitleBlock_Text_Company")
            texts.add(text_12, get_oh() + col(1) + 1, get_ov() + row(4)).anchor_position(1).set_font_size(0, 0, 1.5).name("TitleBlock_Text_Controller")
            texts.add(text_05, get_oh() + col(2) + 2.5, get_ov() + .5 * (row(3) + row(4))).anchor_position(6).set_font_size(0, 0, 3).name("TitleBlock_Text_Controller_1")
            texts.add(text_13, get_oh() + col(1) + 1, get_ov() + .5 * (row(3) + row(4))).anchor_position(1).set_font_size(0, 0, 1.5).name("TitleBlock_Text_CDate")
            texts.add(text_05, get_oh() + col(2) + 2.5, get_ov() + row(3)).anchor_position(6).set_font_size(0, 0, 3).name("TitleBlock_Text_Controller_1")
            texts.add(text_14, get_oh() + col(1) + 1, get_ov() + row(5)).anchor_position(1).set_font_size(0, 0, 1.5).name("TitleBlock_Text_Designer")
            texts.add(text_15, get_oh() + col(2) + 2.5, get_ov() + .5 * (row(4) + row(5))).anchor_position(6).set_font_size(0, 0, 3).name("TitleBlock_Text_Designer_1")
            texts.add(text_13, get_oh() + col(1) + 1, get_ov() + .5 * (row(4) + row(5))).anchor_position(1).set_font_size(0, 0, 1.5).name("TitleBlock_Text_DDate")
            texts.add(get_date(), get_oh() + col(2) + 2.5, get_ov() + row(4)).anchor_position(6).set_font_size(0, 0, 3).name("TitleBlock_Text_DDate_1")
            texts.add(text_05, get_oh() + .5 * (col(3) + col(5)), get_ov() + row(4)).anchor_position(5).set_font_size(0, 0, 7).name("TitleBlock_Text_Title_1")

            for ii in range(1, get_nb_of_revisions() + 1):
                i_y = get_ov() + (ii - .5) * row(5) / get_nb_of_revisions()
                texts.add(get_rev_letter(ii), get_oh() + .5 * (col(5) + col(6)), i_y).anchor_position(5).set_font_size(0, 0, 2.5).name("TitleBlock_Text_Modif_" + get_rev_letter(ii))
                texts.add("_", get_oh() + .5 * col(6), i_y).anchor_position(5).set_font_size(0, 0, 2).name("TitleBlock_Text_MDate_" + get_rev_letter(ii))

            print("title block texts added")
            cat_links()
        
        def cat_exit():
            sel.clear()
            active_view.activate()
            cat.app.hso_synchronized(True).refresh_display(True)

        def cat_drw_creation():
            if cat_check_ref(1):
                return
            cat_create_reference()
            cat_frame()
            cat_create_title_block_frame()
            cat_create_title_block_standard()
            cat_title_block_text()
            cat_exit()

        def compute_title_block_translation() -> tuple[float, float]:  
            translation_tab = [0.0] * 2
            try:
                text = texts.get_item("Reference_" + get_macro_id())
                translation_tab[0] = get_width() - get_offset() - text.x()
                translation_tab[1] = get_offset() - text.y()

                text.x(text.x() + translation_tab[0]).y(text.y() + translation_tab[1])
            except Exception as e:
                print("compute_title_block_translation", e)

            return translation_tab

        def compute_revision_block_translation() -> tuple:
            translation_tab = [0.0] * 2
            try:
                text = texts.get_item("RevisionBlock_Text_Init")
                translation_tab[0] = get_width() - get_offset() + get_col_rev(4) - text.x()
                translation_tab[1] = get_height() - get_offset() - .5 * get_rev_row_height() - text.y()
            except Exception as e:
                pass

            return translation_tab
        
        def delete_all(i_query: str):
            sel.clear().add(view).search(i_query + ",sel").delete()

        def select_all(i_query: str) -> 'Selection':
            sel.clear().add(view).search(i_query + ", sel")
            return sel

        def cat_delete_title_block_standard():
            delete_all("CATDrwSearch.2DGeometry.Name=TitleBlock_Standard*")

        def cat_delete_title_block_frame():
            delete_all("CATDrwSearch.2DGeometry.Name=TitleBlock_Line_*")

        def cat_move_title_block_text(translation: tuple):
            select_all("CATDrwSearch.DrwText.Name=TitleBlock_Text_*") 
            for i in range(1, sel.count() + 1):
                text = sel.item(i).value(DrawingText)
                text.x(text.x() + translation[0]).y(text.y() + translation[1])

        def cat_delete_revision_block_frame():
            delete_all("CATDrwSearch.2DGeometry.Name=RevisionBlock_Line_*")

        def cat_check_rev() -> int:
            return select_all("CATDrwSearch.DrwText.Name=RevisionBlock_Text_Rev_*").count()

        def cat_create_revision_block_frame():
            revision = cat_check_rev()
            if revision == 0:
                return
            
            for i in range(0, revision + 1):
                ix = get_oh()
                iy1 = get_height() - get_ov() - get_rev_row_height() * i
                iy2 = get_height() - get_ov() - get_rev_row_height() * (i + 1)

                fact.create_line(ix + get_col_rev(1), iy1, ix + get_col_rev(1), iy2).name("RevisionBlock_Line_Column_" + get_rev_letter(i) + "_1")
                fact.create_line(ix + get_col_rev(2), iy1, ix + get_col_rev(2), iy2).name("RevisionBlock_Line_Column_" + get_rev_letter(i) + "_2")
                fact.create_line(ix + get_col_rev(3), iy1, ix + get_col_rev(3), iy2).name("RevisionBlock_Line_Column_" + get_rev_letter(i) + "_3")
                fact.create_line(ix + get_col_rev(4), iy1, ix + get_col_rev(4), iy2).name("RevisionBlock_Line_Column_" + get_rev_letter(i) + "_4")
                fact.create_line(ix + get_col_rev(1), iy2, ix, iy2).name("RevisionBlock_Line_Row_") + get_rev_letter(i)

        def cat_move_revision_block_text(translation: tuple):
            count = select_all("CATDrwSearch.DrwText.Name=RevisionBlock_Text_*").count()
            for i in range(1, count + 1):
                text = sel.item(i).value(DrawingText)
                text.x(text.x() + translation[0]).y(text.y() + translation[1])

        def cat_move_views(translation: tuple):
            relation_activate_array = [False] * (sheet.views().count() - 3 + 1)
            #print(len(relation_activate_array), relation_activate_array, sheet.views().count() + 1)
            for i in range(3, sheet.views().count() + 1):
                relation_activate_array[i - 3] = sheet.views().item(i).un_aligned_with_reference_view().is_relation_activated()

            for i in range(3, sheet.views().count() + 1):
                cur_view = sheet.views().item(i)
                cur_view.x(cur_view.x() + translation[0]).y(cur_view.y() + translation[1])

                if relation_activate_array[i - 3] == True:
                    try:
                        ref_view = cur_view.reference_view()
                        if ref_view is not None:
                            cur_view.aligned_with_reference_view()
                    except Exception as e:
                        print("ref view cannot be accessed")

        def cat_drw_resizing():
            if cat_check_ref(0) == False:
                return
            tb_translation = compute_title_block_translation()
            rb_translation = compute_revision_block_translation()

            if tb_translation[0] != 0 or tb_translation[1] != 0:
                print("deleting frame")
                delete_all("CATDrwSearch.DrwText.Name=Frame_Text_*")
                delete_all("CATDrwSearch.2DGeometry.Name=Frame_*")
                cat_frame()

                cat_delete_title_block_standard()
                cat_create_title_block_standard()

                cat_delete_title_block_frame()
                cat_create_title_block_frame()
                cat_move_title_block_text(tb_translation)

                cat_delete_revision_block_frame()
                cat_create_revision_block_frame()
                cat_move_revision_block_text(rb_translation)

                cat_move_views(tb_translation)
                cat_links()

            cat_exit()

        def cat_drw_update():
            if cat_check_ref(0) == False:
                return
            
            cat_delete_title_block_standard()
            cat_create_title_block_standard()
            cat_links()
            cat_exit()

        def catmain():
            target_sheet = cat.drawing.sheets().active_sheet()
            target_sheet.views().item(2).activate()
            print("init")
            if cat_init() == False:
                return
            
            try:
                name =  texts.get_item("Reference_" + get_macro_id()).name()
            except Exception as e:
                name = "none"

            if name == "none":
                cat_drw_creation()
            else:
                cat_drw_resizing()
                cat_drw_update()

            cat_exit()


        catmain()

except Exception as e:
    traceback_str = traceback.format_exc()
    print("traceback", traceback_str)

input("Press enter to continue...")