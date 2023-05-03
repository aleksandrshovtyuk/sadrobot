from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

User = get_user_model()


class SadsiteURLTests(TestCase):
    def test_post_namespaces_uses_correct_template(self):
        """Проверка шаблонов для namespaces приложения sadsite."""
        reverse_names_templates = (
            ('sadsite:index', 'sadrobot/index.html'),
        )
        for reverse_name, template in reverse_names_templates:
            with self.subTest(reverse_name=reverse_name):
                self.assertTemplateUsed(
                    self.client.get(reverse(reverse_name)), template)

    def test_posts_namespaces_matches_correct_urls(self):
        """Проверка namespaces совпадают с hardcod urls приложения sadsite."""
        reverse_names_urls = (
            ('sadsite:index', '/'),
        )
        for reverse_name, url in reverse_names_urls:
            with self.subTest(reverse_name=reverse_name):
                self.assertEqual(reverse(reverse_name), url)

    def test_404_page_available(self):
        """Проверка доступности страницы 404."""
        self.assertEqual(
            self.client.get('unexisting_page/').status_code,
            HTTPStatus.NOT_FOUND.value)
