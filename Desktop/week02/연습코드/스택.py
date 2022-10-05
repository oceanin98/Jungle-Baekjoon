#고정길이 스택 클래스 fixedStack구현하기

from typing import Any


class FixedStack:
    """고정 길이 스택 클래스"""
    class Empty(Exception):
        """비어 있는 fixedstack에 팝 또는 피크할 떄 내보내는 예외처리"""
        pass
    class Full(Exception):
        """가득찬 FixedStack에 푸시할 떄 내보내는 예외처리"""

        pass

def __init__(self, capacity: int =256) -> None:
    """스택초기화"""
    self.stk = [None]* capacity #스택본체
    self.capacity = capacity #스택크기
    self.ptr=0 #스텍포인터

def __len__(self)-> int:
    """스택에 쌓여 있는 데이터 개수를 반환"""
    return self.ptr 

def is_empty(self) -> bool:
    """스택이 비어있는지 확인"""
    return self.ptr <= 0

def is_full(self) -> bool:
    """스택이 가득 차 있는지 판단"""

    return self.ptr >= self.capacity

def push(self, value:Any) -> None:
    if self.is_full():
        raise FixedStack.Full
    

