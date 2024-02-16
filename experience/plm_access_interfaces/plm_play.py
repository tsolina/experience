from experience.system import AnyObject

class PLMPlay(AnyObject):
    """
                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMPlay
    """

    def __init__(self, com):
        super().__init__(com)
        self.plm_play = com
    
    def play(self) -> 'PLMPlay':
        self.indexed_search.Play()
        return self       

    def stop(self) -> 'PLMPlay':
        self.indexed_search.Stop()
        return self 

    def __repr__(self):
        return f'PLMPlay(name="{self.name()}")'