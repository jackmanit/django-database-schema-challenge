# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

MALE  = 'Male'
FEMALE = 'Female'
OTHER = 'Other'
GENDER_CHOICES = [(MALE,'Male'),
                    (FEMALE,'Female'),
                    (OTHER,'Other')]
NAME_LENGTH = 30
CITY_LENGTH = 20
GENDER_LENGTH = 6

class Hospital(models.Model):
    """ Hospital model.
        name(str): name of hospital
        city(str): city (location) of hospital
    """

    name = models.CharField(max_length=NAME_LENGTH, null=False, blank=False,
                            db_index= True)
    city = models.CharField(max_length=CITY_LENGTH, null=False, blank=False)

    def __str__(self):
        """Return name of hospital"""
        return self.name


class Department(models.Model):
    """ Department of a hospital model.
        name(str): name of department
        hospital(Hospital): related hospital object
    """
    
    name = models.CharField(max_length=NAME_LENGTH, null=False, blank=False, 
                            db_index=True)
    hospital = models.ForeignKey(Hospital, related_name='departments')

    def __str__(self):
        return self.name


class Person(models.Model):
    """ Person in hospital
        name(str): name of worker
        age(int): age of worker
        gender(str): gender of worker
    """
    DOCTOR = 'D'
    NURSE = 'N'
    POSITION = [(NURSE, 'Nurse'), 
                  (DOCTOR, 'Doctor')]
    POSITION_LENGTH = 6
    name = models.CharField(max_length=NAME_LENGTH, null=False, blank=False,
                            db_index=True)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, default=OTHER,
                              max_length=GENDER_LENGTH, null=False, blank=False)

    def __str__(self):
        return self.name


class Worker(models.Model):
    """ Worker of hospital model
        person(Person): related person object of worker
        position(str): role of worker in hospital
        department(Department): related department(s) in hospital
    """
    DOCTOR = 'Doctor'
    NURSE = 'Nurse'
    POSITION = [(NURSE, 'Nurse'), 
                  (DOCTOR, 'Doctor')]
    POSITION_LENGTH = 6
    person = models.ForeignKey(Person, related_name='jobs')
    position = models.CharField(choices=POSITION, max_length=6,
                                null=False, blank=False)
    department = models.ForeignKey(Department, related_name='workers')
  

class Patient(models.Model):
    """ Patient of hospital model
        person(Person): related person object of worker
        department(Department): related department in hospital
    """
    person = models.ForeignKey(Person, related_name='patient_data')
    department = models.ForeignKey(Department, related_name='patients')



class ExaminationResult(models.Model):
    """ Examine result model
        examine_time(datetime): examine time
        result(str): result of examination
        worker(Worker): related worker that examine patient
        patient(Patient): related patient that was examined
    """
    HEALTHY = 'Healthy'
    CORONA = 'Corona'
    BOTISM = 'Botism'
    DEAD = 'Dead'
    RESULTS = [(HEALTHY, 'Healthy'),
               (CORONA, 'Corona'),
               (BOTISM, 'Botism'),
               (DEAD, 'Dead')]
    RESULT_LENGTH = 7
    examination_time = models.DateTimeField(auto_now_add=True)
    result = models.CharField(choices=RESULTS, default=BOTISM, max_length=7,
                              null=False, blank=False)
    worker = models.ForeignKey(Worker, related_name='examinations')
    patient = models.ForeignKey(Patient, related_name='examinations')


    def __str__(self):
        return str(self.examine_time)