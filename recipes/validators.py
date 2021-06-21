from .forms import RecipesForm
from .views import get_ingredients


def validate_ingredients(request, form, ingredients):
    if ingredients is []:
        context = {
            "form": form,
            "error": "������� ��� ������� 1 ����������"
        }
        return context
    for item in ingredients:
        if not ingredients[item].exists():
            context = {
                "form": form,
                "error": "����� ���������� �� ����������"
            }
            return context
    for amount in ingredients.values():
        if int(amount) <= 0:
            context = {
                "form": form,
                "error":
                    "������� ��������� ����������� �� ���� ���� ��������������"
            }
            return context
