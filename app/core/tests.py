from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    
        
    def test_create_user_with_email_suceesful(self):
        #Test creating a new user with an email is succesful
        email = 'alhiladam@gmail.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        
    def test_new_user_email_normalize(self):
        #Test the email for a new user is normalized
        email = 'alhilaladam@gmail.com'
        user = get_user_model().objects.create_user(email, 'Test123')
        self.assertEqual(user.email.lower(), user.email)
    
    def test_new_user_invalid_email(self):
        #Test cresting user with no email raises error
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test123')
        
   
    def test_create_new_superuser(self):
        #Test creating a new superuser
        user = get_user_model().objects.create_superuser(
            email = 'alhilaladam@gmail.com',
            password = 'Test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        
    