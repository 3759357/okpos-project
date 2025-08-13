import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from shop.models import Tag

@pytest.mark.django_db
def test_create_product_with_tags_and_options():
    tag = Tag.objects.create(name="ExistTag")
    client = APIClient()

    payload = {
        "name": "TestProduct",
        "option_set": [
            {"name": "TestOption1", "price": 1000},
            {"name": "TestOption2", "price": 500},
            {"name": "TestOption3", "price": 0}
        ],
        "tag_set": [
            {"pk": tag.pk, "name": "ExistTag"},
            {"name": "NewTag"}
        ]
    }

    res = client.post(reverse('product-list'), payload, format='json')
    assert res.status_code == 201
    assert res.data["name"] == "TestProduct"
    assert len(res.data["option_set"]) == 3
    assert len(res.data["tag_set"]) == 2
