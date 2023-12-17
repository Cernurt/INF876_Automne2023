# Generated by Django 3.1 on 2020-10-30 11:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0136_add_attribute_type_and_page_to_attribute_relation"),
        ("attribute", "0001_initial"),
    ]

    state_operations = [
        migrations.AlterUniqueTogether(
            name="assignedproductattribute",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="assignedproductattribute",
            name="assignment",
        ),
        migrations.RemoveField(
            model_name="assignedproductattribute",
            name="product",
        ),
        migrations.RemoveField(
            model_name="assignedproductattribute",
            name="values",
        ),
        migrations.AlterUniqueTogether(
            name="assignedvariantattribute",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="assignedvariantattribute",
            name="assignment",
        ),
        migrations.RemoveField(
            model_name="assignedvariantattribute",
            name="values",
        ),
        migrations.RemoveField(
            model_name="assignedvariantattribute",
            name="variant",
        ),
        migrations.RemoveField(
            model_name="attribute",
            name="page_types",
        ),
        migrations.RemoveField(
            model_name="attribute",
            name="product_types",
        ),
        migrations.RemoveField(
            model_name="attribute",
            name="product_variant_types",
        ),
        migrations.AlterUniqueTogether(
            name="attributepage",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="attributepage",
            name="assigned_pages",
        ),
        migrations.RemoveField(
            model_name="attributepage",
            name="attribute",
        ),
        migrations.RemoveField(
            model_name="attributepage",
            name="page_type",
        ),
        migrations.AlterUniqueTogether(
            name="attributeproduct",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="attributeproduct",
            name="assigned_products",
        ),
        migrations.RemoveField(
            model_name="attributeproduct",
            name="attribute",
        ),
        migrations.RemoveField(
            model_name="attributeproduct",
            name="product_type",
        ),
        migrations.AlterUniqueTogether(
            name="attributetranslation",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="attributetranslation",
            name="attribute",
        ),
        migrations.AlterUniqueTogether(
            name="attributevalue",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="attributevalue",
            name="attribute",
        ),
        migrations.AlterUniqueTogether(
            name="attributevaluetranslation",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="attributevaluetranslation",
            name="attribute_value",
        ),
        migrations.AlterUniqueTogether(
            name="attributevariant",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="attributevariant",
            name="assigned_variants",
        ),
        migrations.RemoveField(
            model_name="attributevariant",
            name="attribute",
        ),
        migrations.RemoveField(
            model_name="attributevariant",
            name="product_type",
        ),
        migrations.DeleteModel(
            name="AssignedPageAttribute",
        ),
        migrations.DeleteModel(
            name="AssignedProductAttribute",
        ),
        migrations.DeleteModel(
            name="AssignedVariantAttribute",
        ),
        migrations.DeleteModel(
            name="Attribute",
        ),
        migrations.DeleteModel(
            name="AttributePage",
        ),
        migrations.DeleteModel(
            name="AttributeProduct",
        ),
        migrations.DeleteModel(
            name="AttributeTranslation",
        ),
        migrations.DeleteModel(
            name="AttributeValue",
        ),
        migrations.DeleteModel(
            name="AttributeValueTranslation",
        ),
        migrations.DeleteModel(
            name="AttributeVariant",
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]
