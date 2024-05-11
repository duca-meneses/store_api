from typing import List
from fastapi import status
import pytest

from tests.factories import product_data


async def test_controller_create_should_return_success(client, products_url):
    response = await client.post(products_url, json=product_data())

    content = response.json()

    del content["created_at"]
    del content["updated_at"]
    del content["id"]

    assert response.status_code == status.HTTP_201_CREATED
    assert content == {
        "name": "Iphone 14 pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }


async def test_controller_create_should_return_unprocessable_entity(
    client, products_url
):
    response = await client.post(products_url, json={})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
                "type": "missing",
                "loc": ["body", "name"],
                "msg": "Field required",
                "input": {},
            },
            {
                "type": "missing",
                "loc": ["body", "quantity"],
                "msg": "Field required",
                "input": {},
            },
            {
                "type": "missing",
                "loc": ["body", "price"],
                "msg": "Field required",
                "input": {},
            },
            {
                "type": "missing",
                "loc": ["body", "status"],
                "msg": "Field required",
                "input": {},
            },
        ]
    }


async def test_controller_get_should_return_success(
    client, products_url, product_inserted
):
    response = await client.get(f"{products_url}{product_inserted.id}")
    content = response.json()

    del content["created_at"]
    del content["updated_at"]

    assert response.status_code == status.HTTP_200_OK
    assert content == {
        "id": str(product_inserted.id),
        "name": "Iphone 14 pro Max",
        "quantity": 10,
        "price": "8.500",
        "status": True,
    }


async def test_controller_get_should_return_not_found(client, products_url):
    response = await client.get(f"{products_url}687d5cac-db1a-4660-8fa5-7c03fa677364")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert (
        response.json()["detail"]
        == "Product not found with filter: ID=687d5cac-db1a-4660-8fa5-7c03fa677364"
    )


@pytest.mark.usefixtures("products_inserted")
async def test_controller_get_all_should_return_success(client, products_url):
    response = await client.get(f"{products_url}")

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), List)
    assert len(response.json()) > 1


async def test_controller_update_should_return_success(
    client, products_url, product_inserted
):
    response = await client.patch(
        f"{products_url}{product_inserted.id}", json={"quantity": 30}
    )

    content = response.json()
    created_at = content["created_at"]
    updated_at = content["updated_at"]

    assert response.status_code == status.HTTP_200_OK
    assert content == {
        "id": str(product_inserted.id),
        "created_at": created_at,
        "updated_at": updated_at,
        "name": "Iphone 14 pro Max",
        "quantity": 30,
        "price": "8.500",
        "status": True,
    }


async def test_controller_delete_should_return_success(
    client, products_url, product_inserted
):
    response = await client.delete(f"{products_url}{product_inserted.id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT


async def test_controller_delete_should_return_not_found(client, products_url):
    response = await client.delete(
        f"{products_url}687d5cac-db1a-4660-8fa5-7c03fa677364"
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert (
        response.json()["detail"]
        == "Product not found with filter: ID=687d5cac-db1a-4660-8fa5-7c03fa677364"
    )
