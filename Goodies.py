# Goodies.py
# 더 이상 직접 사용되지 않으나, 호환성을 위해 뼈대만 남김

class Goodie:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("Goodie는 Item 클래스로 대체되었습니다.")

class GoodieMgr:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("GoodieMgr는 ItemMgr로 대체되었습니다.")
