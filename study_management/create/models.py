from django.db import models


STUDY_PHASE_CHOICES = [
    ('Phase1', 'Phase 1'),
    ('Phase2', 'Phase 2'),
    ('Phase3', 'Phase 3'),
    ('Phase4', 'Phase 4'),
]

class createstudy(models.Model):
    Study_name = models.CharField(max_length=50) 
    Study_Phase = models.CharField(max_length=10, choices=STUDY_PHASE_CHOICES, default='Phase1')
    Sponsor_Name = models.CharField(max_length=50)
    Study_Description = models.TextField()
    
    
    def __str__(self):
        return self.Study_name
    
    