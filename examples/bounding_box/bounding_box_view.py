import tkinter as tk

from examples.bounding_box.bounding_box_view_model import BoundingBoxViewModel

class BoundingBoxView:
    def __init__(self, root, view_model: 'BoundingBoxViewModel'):
        self.view_model = view_model

        self.add_user_input(root)
        self.add_options(root)
        self.execute_frame_definition(root)

    def add_user_input(self, root):
        self.frame = tk.Frame(root, padx=0, pady=0, relief=tk.SOLID, highlightbackground="darkblue", highlightcolor="red", highlightthickness=1)
        self.frame.pack(padx=20, pady=20, fill=tk.X)

        title_bar = tk.Frame(self.frame, bg='darkblue', bd=1)
        title_bar.pack(fill=tk.X)

        title_label = tk.Label(title_bar, text="Input:", bg='darkblue', fg='white', font=("Helvetica", 12, "bold"))
        title_label.pack(side = tk.LEFT, padx=10)

        input_frame = tk.Frame(self.frame, padx=10, pady=10)
        input_frame.pack(fill=tk.X)

        # Create the label
        label_a = tk.Label(input_frame, text="Shape:")
        label_a.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

        # Create the text field (entry)
        entry_a = tk.Entry(input_frame, textvariable=self.view_model.shape_name_var)
        entry_a.grid(row=0, column=1, padx=5, pady=5)

        # Create the button
        button_a = tk.Button(input_frame, text="Select", command=self.view_model.select_shape)
        button_a.grid(row=0, column=2, padx=5, pady=5)

        # Create the label
        label_b = tk.Label(input_frame, text="Axis System:")
        label_b.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)

        # Create the text field (entry)
        entry_b = tk.Entry(input_frame, textvariable=self.view_model.axis_name_var)
        entry_b.grid(row=1, column=1, padx=5, pady=5)

        # Create the button
        button_b = tk.Button(input_frame, text="Select", command=self.view_model.select_axis)
        button_b.grid(row=1, column=2, padx=5, pady=5)


    def add_options(self, root):
        self.options_frame = tk.Frame(root, padx=0, pady=0, relief=tk.SOLID, highlightbackground="darkblue", highlightcolor="red", highlightthickness=1)
        self.options_frame.pack(padx=20, pady=20, fill=tk.X)

        title_bar = tk.Frame(self.options_frame, bg='darkblue', bd=1)
        title_bar.pack(fill=tk.X)

        title_label = tk.Label(title_bar, text="Options:", bg='darkblue', fg='white', font=("Helvetica", 12, "bold"))
        title_label.pack(side = tk.LEFT, padx=10)

        options_frame = tk.Frame(self.options_frame, padx=10, pady=10)
        options_frame.pack(fill=tk.X)

        vcmd = (options_frame.register(self.view_model.validate_input), '%P')

        label_axis = tk.Label(options_frame, text='Axis:')
        label_axis.grid(row=0, column=0, padx=5, pady=5)

        label_px = tk.Label(options_frame, text="X")
        label_px.grid(row=1, column=0, padx=5, pady=5)

        self.input_px = tk.Entry(options_frame, width=5, validate='key', validatecommand=vcmd, textvariable=self.view_model.px_var)
        self.input_px.grid(row=1, column=1, padx=5, pady=5)

        label_py = tk.Label(options_frame, text="Y")
        label_py.grid(row=2, column=0, padx=5, pady=5)

        self.input_py = tk.Entry(options_frame, width=5, validate='key', validatecommand=vcmd, textvariable=self.view_model.py_var)
        self.input_py.grid(row=2, column=1, padx=5, pady=5)

        label_pz = tk.Label(options_frame, text="Z")
        label_pz.grid(row=3, column=0, padx=5, pady=5)

        self.input_pz = tk.Entry(options_frame, width=5, validate='key', validatecommand=vcmd, textvariable=self.view_model.pz_var)
        self.input_pz.grid(row=3, column=1, padx=5, pady=5)


        label_nx = tk.Label(options_frame, text="-X")
        label_nx.grid(row=1, column=2, padx=5, pady=5)

        self.input_nx = tk.Entry(options_frame, width=5, validate='key', validatecommand=vcmd, textvariable=self.view_model.nx_var)
        self.input_nx.grid(row=1, column=3, padx=5, pady=5)

        label_ny = tk.Label(options_frame, text="-Y")
        label_ny.grid(row=2, column=2, padx=5, pady=5)

        self.input_ny = tk.Entry(options_frame, width=5, validate='key', validatecommand=vcmd, textvariable=self.view_model.ny_var)
        self.input_ny.grid(row=2, column=3, padx=5, pady=5)

        label_nz = tk.Label(options_frame, text="-Z")
        label_nz.grid(row=3, column=2, padx=5, pady=5)

        self.input_nz = tk.Entry(options_frame, width=5, validate='key', validatecommand=vcmd, textvariable=self.view_model.nz_var)
        self.input_nz.grid(row=3, column=3, padx=5, pady=5)


        self.cb_x = tk.Checkbutton(options_frame, variable=self.view_model.cb_x_var, command=lambda: self.view_model.same_value(self.view_model.cb_x_var, self.input_px, self.input_nx))
        self.cb_x.grid(row=1, column=4, padx=5, pady=5)

        self.cb_y = tk.Checkbutton(options_frame, variable=self.view_model.cb_y_var, command=lambda: self.view_model.same_value(self.view_model.cb_y_var, self.input_py, self.input_ny))
        self.cb_y.grid(row=2, column=4, padx=5, pady=5)

        self.cb_z = tk.Checkbutton(options_frame, variable=self.view_model.cb_z_var, command=lambda: self.view_model.same_value(self.view_model.cb_z_var, self.input_pz, self.input_nz))
        self.cb_z.grid(row=3, column=4, padx=5, pady=5)

        self.cb_all = tk.Checkbutton(options_frame, text="Same offset", variable=self.view_model.cb_all_var, command=self.update_select_all)
        self.cb_all.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

    def execute_frame_definition(self, root):
        self.execute_frame = tk.Frame(root, padx=0, pady=0, relief=tk.SOLID, highlightbackground="darkblue", highlightcolor="red", highlightthickness=1,
                                      bg='darkblue', bd=1)
        self.execute_frame.pack(padx=20, pady=20, fill=tk.X)

        # Button to submit the name
        self.submit_button = tk.Button(self.execute_frame, text="Execute", command=self.view_model.execute)
        self.submit_button.pack()

    def update_select_all(self):
        self.input_nx.config(state=self.view_model.get_entry_state_option_nx())
        self.input_ny.config(state=self.view_model.get_entry_state_option_nx())
        self.input_nz.config(state=self.view_model.get_entry_state_option_nx())
        self.input_py.config(state=self.view_model.get_entry_state_option_nx())
        self.input_pz.config(state=self.view_model.get_entry_state_option_nx())
        self.view_model.set_select_all_state()