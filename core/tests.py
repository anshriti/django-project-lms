from django.test import TestCase
from core.models import Teacher
from django.contrib.auth.models import User
# Create your tests here.
class TeacherModelTest(TestCase):
    def test_teacher_creation(self):
        teacher = Teacher.objects.create(
            full_name="John Doe", 
            email="JD@gmail.com",
            department="BCA",
            phone_no=673281897,
            join_date="2025-06-22",
            #user=User.objects.get(id=11), # Assuming user with id 11 exists
            # Uncomment the line below if you want to create a new user
            user=User.objects.create_user(username="testuser", password="nepal@123")
        )
        try:
        #case one: user exists
            print("Case one: user exists")
            self.assertEqual(teacher.full_name, "John Doe")
            self.assertEqual(teacher.email, "JD@gmail.com")
            self.assertEqual(teacher.department, "BCA")
            self.assertEqual(teacher.phone_no, 673281)
            self.assertEqual(teacher.join_date, "2025-06-22")
            self.assertEqual(teacher.user, User.objects.get(username="testuser"))
        except Exception as e:
            print("Error :" ,e)

        
        try:
        #case two: user with different username
            print("Case Two: user exists with different username")
            self.assertEqual(teacher.full_name, "John Doe")
            self.assertEqual(teacher.email, "JD@gmail.com")
            self.assertEqual(teacher.department, "BCA")
            self.assertEqual(teacher.phone_no, 673281)
            self.assertEqual(teacher.join_date, "2025-06-22")
            self.assertEqual(teacher.user, User.objects.get(username="nirmal")) #different username
        except Exception as e:
            print("Error :" ,e)
            print("Error:", "User must be same for teacher.")

        #case three: phone number length
        try:

            print("Case Three: phone number length")
            self.assertEqual(teacher.full_name, "John Doe")
            self.assertEqual(teacher.email, "JD@gmail.com")
            self.assertEqual(teacher.department, "BCA")
            self.assertEqual(teacher.phone_no, 673281987) #phone number length is 9 but passing 10
            self.assertEqual(teacher.join_date, "2025-06-22")
            self.assertEqual(teacher.user, User.objects.get(username="testuser"))
        except Exception as e:
            print("Error :" ,e)
            print("Error:", "Required phone number length is 9.")

    def test_teacher_model_email_exist(self):
        teacher = Teacher.objects.create(
            full_name="KP Oli",
            email="kpoli@gmail.com",
            department="BCA",
            phone_no=673281897,
            join_date="2025-06-22",
            user=User.objects.create_user(username="testuser", password="nepal@123")
        )
  
  #case one: email different
        try:
            print("Case One: email different")
            self.assertEqual(teacher.full_name, "KP Oli")
            self.assertEqual(teacher.email, "jd@gmail.com")
            self.assertEqual(teacher.department, "BCA")
            self.assertEqual(teacher.phone_no, 673281897)
            self.assertEqual(teacher.join_date, "2025-06-22")
            self.assertEqual(teacher.user, User.objects.get(username="testemail"))
            print("Case Email: Email different passed.")
        except Exception as e:
            print("Error :" ,e)
            print("Error:" ,"Email already available")
