"""
유틸리티 함수 모듈

담당: 팀원 C (2인 팀의 경우 팀원 A가 함께 담당)
브랜치: feature/utils
"""

from typing import List, Any


def validate_numbers(data: List[Any]) -> bool:
    """리스트의 모든 요소가 숫자인지 검증합니다.

    Args:
        data: 검증할 리스트

    Returns:
        모든 요소가 숫자(int 또는 float)면 True, 아니면 False

    Examples:
        >>> validate_numbers([1, 2, 3])
        True
        >>> validate_numbers([1, 'a', 3])
        False
        >>> validate_numbers([])
        True
    """
    # TODO: 구현하세요
    # 힌트: isinstance(x, (int, float)) 사용
    # all() 안에 들어오는 모든 값 검사 -> 
    if data is None or not isinstance(data, list):
        return False

    if all(isinstance(x, (int, float)) for x in data):
        return True
    else:
        return False


def round_result(value: float, decimals: int = 2) -> float:
    """숫자를 지정한 소수점 자리수로 반올림합니다.

    Args:
        value: 반올림할 숫자
        decimals: 소수점 자리수 (기본값: 2)

    Returns:
        반올림된 숫자

    Examples:
        >>> round_result(3.14159)
        3.14
        >>> round_result(3.14159, 3)
        3.142
    """
    # TODO: 구현하세요
    # 힌트: round() 내장 함수 사용
    if type(value) is not float:
        return "소수가 아닙니다"
    return round(value, decimals)


def format_output(name: str, value: float, decimals: int = 2) -> str:
    """결과를 포맷팅된 문자열로 반환합니다.

    Args:
        name: 결과 이름 (예: "평균", "중앙값")
        value: 결과 값
        decimals: 소수점 자리수 (기본값: 2)

    Returns:
        "이름: 값" 형식의 문자열

    Examples:
        >>> format_output("평균", 3.14159)
        '평균: 3.14'
        >>> format_output("합계", 100.0, 0)
        '합계: 100'
    """
    # TODO: 구현하세요
    # 힌트: f-string 또는 format() 사용
    if name is None:
        return "결과 이름이 없습니다"

    if value is None:
        return "결과 값이 없습니다"

    if decimals == 0:
        return f"{name}: {round(value)}"        
    return f"{name}: {round(value, decimals)}"

    
