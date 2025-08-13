from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers
from .models import Product, ProductOption, Tag


class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOption
        fields = ['pk', 'name', 'price']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['pk', 'name']
        extra_kwargs = {
            'name': {'validators': []}
        }


class ProductSerializer(WritableNestedModelSerializer):
    option_set = ProductOptionSerializer(many=True)
    tag_set = TagSerializer(many=True)

    class Meta:
        model = Product
        fields = ['pk', 'name', 'option_set', 'tag_set']

    def create(self, validated_data):
        options_data = validated_data.pop('option_set', [])
        tags_data = validated_data.pop('tag_set', [])

        product = Product.objects.create(**validated_data)

        # 옵션 생성
        for opt_data in options_data:
            ProductOption.objects.create(product=product, **opt_data)

        # 태그 처리
        for tag_data in tags_data:
            if tag_data.get('pk'):
                tag = Tag.objects.get(pk=tag_data['pk'])
            else:
                tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
            product.tag_set.add(tag)

        return product
