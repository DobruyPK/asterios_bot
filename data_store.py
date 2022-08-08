import core


class dataSaver():
    _instances = {}
    _target_tag = str()
    _data = dict()
    _unic_bos = set()

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def update_tag(self, tag):
        self._target_tag = tag

    def get_target_tag(self):
        return self._target_tag

    def update_data(self, data_r):
        if 'Boss' in str(data_r):
            valid_data = core.validate_data(data_r)
            self._unic_bos.add(str(valid_data[1]))
            try:
                if self._data[valid_data[1]] < valid_data[0]:
                    self._data[valid_data[1]] = valid_data[0]
            except KeyError:
                self._data[valid_data[1]] = valid_data[0]

    def get_data(self):
        return self._data

    def get_unic_bos(self):
        return self._unic_bos
