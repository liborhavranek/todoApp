from django.urls import reverse

from django.test import TestCase, Client
from datetime import datetime, timezone
from .models import Task, User
# Create your tests here.


class HomeViewTestCase(TestCase):
    def test_home_view(self):
        # Send a GET request to the view
        response = self.client.get('/home')

        # Check that the response is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains the correct template
        self.assertTemplateUsed(response, 'home.html')





































class LoginViewTestCase(TestCase):
    def test_login_view(self):
        # Set up test user
        test_user = User.objects.create_user(username='testuser', password='password')
        
        # Send a POST request to the login view with valid credentials
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'password'})
        
        # Check that the user was logged in and redirected to the index page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        self.assertIn('_auth_user_id', self.client.session)
        
    def test_login_view_invalid_credentials(self):
        # Set up test user
        test_user = User.objects.create_user(username='testuser', password='password')
        
        # Send a POST request to the login view with invalid credentials
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'wrongpassword'})
        
        # Check that the user was not logged in and an error message was displayed
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertNotIn('_auth_user_id', self.client.session)
        self.assertContains(response, 'Invalid username or password')












# Log out function test working good 

class LogoutViewTestCase(TestCase):
    def test_logout_view(self):
        # Set up test user and log them in
        test_user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        
        # Send a GET request to the logout view
        response = self.client.get(reverse('logout'))
        
        # Check that the user was logged out and redirected to the login page
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertNotIn('_auth_user_id', self.client.session)
        
        
        
        
        
        
        
        
        
        
        
        
        
        

class RegisterViewTestCase(TestCase):
    def test_register(self):
        # Send a POST request to the view with the form data
        response = self.client.post(reverse('register'), {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'password123',
            'confirm_password': 'password123',
        })

        # Check that the user's email, username, and password are correct
        user = User.objects.first()
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('password123'))
        
        
        
        
        
    