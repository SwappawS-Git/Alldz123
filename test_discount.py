
import pytest

def discount(price, percent):
    if not 0 <= percent <= 100:
        raise ValueError(f"percent must be 0..100, got {percent}")
    return round(price * (1 - percent / 100), 2)

def test_Discount1():
    assert discount(100, 10) == 90

def test_Discount2():
    assert discount(100, 0) == 100

def test_Discount3():
    with pytest.raises(ValueError):
        discount(100, 150)

  
  
