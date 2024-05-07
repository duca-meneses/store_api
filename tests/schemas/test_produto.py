import pytest
from uuid import UUID
from pydantic import ValidationError

from store.schemas.product import ProductIn
from tests.factories import product_data


def test_schema_return_success():
    data = product_data()
    product = ProductIn.model_validate(data)

    assert product.name == "Iphone 14 pro Max"
    assert isinstance(product.id, UUID)


def test_schema_return_raise():
    data = {"name": "Iphone 14 pro Max", "quantity": 10, "price": 8.500}
    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Iphone 14 pro Max", "quantity": 10, "price": 8.5},
        "url": "https://errors.pydantic.dev/2.7/v/missing",
    }