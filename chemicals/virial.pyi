# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from typing import List
from typing import Union


def BVirial_Pitzer_Curl(T: float, Tc: float, Pc: float, omega: float, order: int = ...) -> float: ...


def BVirial_Tsonopoulos(T: float, Tc: float, Pc: float, omega: float, order: int = ...) -> float: ...


def BVirial_Tsonopoulos_extended(
    T: float,
    Tc: float,
    Pc: float,
    omega: float,
    a: int = ...,
    b: int = ...,
    species_type: str = ...,
    dipole: float = ...,
    order: int = ...
) -> float: ...

__all__: List[str]