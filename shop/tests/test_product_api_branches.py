import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from shop.models import Tag

@pytest.mark.django_db
def test_create_list_retrieve_with_existing_and_new_tags():
    exist = Tag.objects.create(name="ExistTag")
    client = APIClient()

    payload = {
        "name": "BranchProduct",
        "option_set": [
            {"name": "OptA", "price": 1},
            {"name": "OptB", "price": 2}
        ],
        "tag_set": [
            {"pk": exist.pk, "name": "ExistTag"},  # pk 경로 커버
            {"name": "NewTag"}                     # get_or_create 경로 커버
        ]
    }

    # create
    res = client.post(reverse("product-list"), payload, format="json")
    assert res.status_code == 201
    pid = res.data["pk"]
    assert {t["name"] for t in res.data["tag_set"]} == {"ExistTag", "NewTag"}

    # list
    res_list = client.get(reverse("product-list"))
    assert res_list.status_code == 200
    assert any(p["pk"] == pid for p in res_list.data)

    # retrieve
    res_get = client.get(reverse("product-detail", args=[pid]))
    assert res_get.status_code == 200
    assert res_get.data["name"] == "BranchProduct"