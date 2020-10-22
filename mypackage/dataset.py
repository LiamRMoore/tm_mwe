import timbermafia as tm

class BaseDataset:
    pass

class Dataset(BaseDataset, tm.Logged):
    def debug_msg(self):
        self.log.debug("i am debug")
    def warn_msg(self):
        self.log.warning("i am warning")
