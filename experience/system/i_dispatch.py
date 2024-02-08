from experience.system.i_unknown import IUnknown

class IDispatch(IUnknown):
    """
                | System.IUnknown
                |     IDispatch
    """

    def __init__(self):
        super(self).__init__()

    def __repr__(self):
        return f'IDispatch()'
