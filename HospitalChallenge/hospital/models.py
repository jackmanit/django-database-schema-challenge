# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

MALE  = 'M'
FEMALE = 'F'
OTHER = 'O'
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

    name = models.CharField(max_length=NAME_LENGTH)
    city = models.CharField(max_length=CITY_LENGTH)

    def __str__(self):
        """Return name of hospital"""
        return self.name


class Department(models.Model):
    """ Department of a hospital model.
        name(str): name of department
        hospital(Hospital): related hospital object
    """
    
    name = models.CharField(max_length=NAME_LENGTH)
    hospital = models.ForeignKey(Hospital)

    def __str__(self):
        return self.name


class Worker(models.Model):
    """ Worker of hospital model
        name(str): name of worker
        age(int): age of worker
        gender(str): gender of worker
        position(str): role of worker in hospital
        department(Department): related department(s) in hospital
    """
    DOCTOR = 'D'
    NURSE = 'N'
    POSITION = [(NURSE, 'Nurse'), 
                  (DOCTOR, 'Doctor')]
    POSITION_LENGTH = 6
    name = models.CharField(max_length=NAME_LENGTH)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, default=OTHER,
                              max_length=GENDER_LENGTH)
    position = models.CharField(choices=POSITION, max_length=6)
    department = models.ManyToManyField(Department)

    def __str__(self):
        return self.name


class Patient(models.Model):
    """ Patient of hospital model
        name(str): name of patient
        age(int): age of patient
        gender(str): gender of patient
        department(Department): related department in hospital
    """
    name = models.CharField(max_length=NAME_LENGTH)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, default=OTHER,
                              max_length=GENDER_LENGTH)
    department = models.ForeignKey(Department)

    def __str__(self):
        return self.name


class ExamineResult(models.Model):
    """ Examine result model
        examine_time(datetime): examine time
        result(str): result of examination
        worker(Worker): related worker that examine patient
        patient(Patient): related patient that was examined
    """
    HEALTHY = 'H'
    CORONA = 'C'
    BOTISM = 'B'
    DEAD = 'D'
    RESULTS = [(HEALTHY, 'Healthy'),
               (CORONA, 'Corona'),
               (BOTISM, 'Botism'),
               (DEAD, 'Dead')]
    RESULT_LENGTH = 7
    examine_time = models.DateTimeField()
    result = models.CharField(choices=RESULTS, default=BOTISM, max_length=7)
    worker = models.ForeignKey(Worker)
    patient = models.ForeignKey(Patient)


    def __str__(self):
        return self.examine_time.__str__()