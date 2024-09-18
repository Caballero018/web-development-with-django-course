from django.test import TestCase
from registration.models import Profile
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user("test", "tra@test.com", "test1234")
        
    def test_profile_exists(self):
        exits = Profile.objects.filter(user__username = "test").exists()
        self.assertEqual(exits, True)
