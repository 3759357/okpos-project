import pytest
from shop.models import Tag, Product, ProductOption

@pytest.mark.django_db
def test_model_strs():
    tag = Tag.objects.create(name="Tag1")
    product = Product.objects.create(name="Prod1")
    option = ProductOption.objects.create(product=product, name="Opt1", price=100)

    assert str(tag) == "Tag1"
    assert str(product) == "Prod1"
    assert str(option) == "Opt1"