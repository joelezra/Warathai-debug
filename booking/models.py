from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.
class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()


class Date(models.Model):
    date = models.DateField()


class Table(models.Model):
    capacity = models.IntegerField()


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    num_people = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Ensure the table has sufficient capacity for the booking
        if num_people > self.table.capacity:
            raise ValidationError("The table's capacity is insufficient for this booking.")

        # Ensure the selected time slot and date are valid
        existing_bookings = Booking.objects.filter(date=self.date, time_slot=self.time_slot)
        total_people = sum(booking.num_people for booking in existing_bookings)
        if total_people + self.num_people > self.table.capacity:
            raise ValidationError("The selected time slot is unavailable.")

    def save(self, *args, **kwargs):
        self.full_clean() # Perform full validation before saving
        super().save(*args, **kwargs)
