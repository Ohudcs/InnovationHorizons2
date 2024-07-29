from rest_framework import serializers
from .models import Lesson, Student, Teacher, Attendance, Assignment, Grade


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['course_id', 'title', 'content', 'date_added']


class StudentSerializer(serializers.ModelSerializer):
    classes = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'level', 'classes']


class TeacherSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'email', 'experience', 'student', 'classes']


class AttendanceSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    lesson_id = LessonSerializer(read_only=True)

    class Meta:
        model = Attendance
        fields = ['id', 'student', 'lesson_id', 'date', 'status']


class AssignmentSerializer(serializers.ModelSerializer):
    lesson_id = LessonSerializer(read_only=True)
    student_id = StudentSerializer(read_only=True)

    class Meta:
        model = Assignment
        fields = ['assignment_id', 'title', 'description', 'due_date', 'grade', 'lesson_id', 'student_id']


class GradeSerializer(serializers.ModelSerializer):
    assignment = AssignmentSerializer(read_only=True)
    student = StudentSerializer(read_only=True)

    class Meta:
        model = Grade
        fields = ['id', 'assignment', 'student', 'grade']


class ChangePasswordSerializer(serializers.Serializer):
       old_password = serializers.CharField(required=True)
       new_password = serializers.CharField(required=True)