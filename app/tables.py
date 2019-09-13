import django_tables2 as tables
from .models import Upfront


class UpfrontTable(tables.Table):
    selection = tables.CheckBoxColumn(
                accessor="pk",
                attrs={
                    "th__input": {
                        "onclick": "toggle(this)"
                    }
                },
                orderable=False)

    class Meta:
        model = Upfront
        template_name = "django_tables2/bootstrap.html"
        fields = ("recoupable", "organizer", "projection", "selection")
