from examples.bounding_box.bounding_box_model import BoundingBoxModel
from examples.bounding_box.bounding_box_view import BoundingBoxView
from examples.bounding_box.bounding_box_view_model import BoundingBoxViewModel
import tkinter as tk


def start(catia_com = None):
    root = tk.Tk()
    root.title("Bounding Box Example")

    # Initialize the Model
    model = BoundingBoxModel(catia_com)

    # Initialize the ViewModel with the Model
    view_model = BoundingBoxViewModel(model)

    # Initialize the View with the ViewModel
    view = BoundingBoxView(root, view_model)

    root.mainloop()

if __name__ == "__main__":
    start()