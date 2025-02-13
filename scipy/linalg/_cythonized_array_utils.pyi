from numpy.typing import NDArray
from typing import Any, Tuple

def get_array_bandwidth(a: NDArray[Any]) -> Tuple[int, int]: ...

def issymmetric(
    a: NDArray[Any],
    atol: None | float = ...,
    rtol: None | float = ...,
) -> bool: ...

def ishermitian(
    a: NDArray[Any],
    atol: None | float = ...,
    rtol: None | float = ...,
) -> bool: ...