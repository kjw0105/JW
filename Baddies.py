# Baddies.py
# 더 이상 직접 사용되지 않으나, 호환성을 위해 뼈대만 남김

class Baddie:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("Baddie는 Item 클래스로 대체되었습니다.")

class BaddieMgr:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("BaddieMgr는 ItemMgr로 대체되었습니다.")
