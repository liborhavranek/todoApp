from django.test import TestCase
from datetime import datetime, timezone
from .models import Task
# Create your tests here.


class HomeViewTestCase(TestCase):
    def test_home_view(self):
        # Send a GET request to the view
        response = self.client.get('/home')

        # Check that the response is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains the correct template
        self.assertTemplateUsed(response, 'home.html')



class TaskViewTestCase(TestCase):
    def setUp(self):
        # Create a test Task object
        Task.objects.create(
            title='Test Task',
            desc='This is a test task',
            due=datetime.now(timezone.utc)
        )

    def test_task_view(self):
        # Send a GET request to the view
        response = self.client.get('/task/1')

        # Check that the response is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains the correct template
        self.assertTemplateUsed(response, 'task.html')

        # Check that the rendered context contains the correct Task object
        self.assertEqual(response.context['task'].title, 'Test Task')
        self.assertEqual(response.context['task'].desc, 'This is a test task')

