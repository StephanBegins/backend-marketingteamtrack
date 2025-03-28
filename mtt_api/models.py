from django.db import models

# Main Task Header (mthdr)
class TaskHeader(models.Model):
    user_id = models.CharField(max_length=255)  # User ID
    date = models.DateField()  # Task date
    time = models.CharField(max_length=20)  # Time in "HH:MM AM/PM" format
    customer_type = models.CharField(max_length=50, choices=[('Existing Customer', 'Existing Customer'), ('New Customer', 'New Customer')])
    task_type = models.CharField(max_length=50, choices=[('New Order', 'New Order'), ('Payment', 'Payment'), ('Meeting Customer', 'Meeting Customer')])
    no_of_customers = models.PositiveIntegerField()  # Number of customers
    remarks = models.TextField(blank=True, null=True)  # Remarks

    def __str__(self):
        return f"{self.user_id} - {self.date} - {self.task_type}"

# Task Details (mtdtl) linked to TaskHeader
class TaskDetail(models.Model):
    task_header = models.ForeignKey(TaskHeader, related_name="details", on_delete=models.CASCADE)  # Relationship with TaskHeader
    project = models.CharField(max_length=255)  # Project name
    contact_person = models.CharField(max_length=255)  # Contact person
    designation = models.CharField(max_length=255, blank=True, null=True)  # Designation
    contact_no = models.CharField(max_length=20)  # Contact number
    purpose_details = models.TextField(blank=True, null=True)  # Purpose details
    payment = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Payment amount (optional)

    def __str__(self):
        return f"{self.project} - {self.contact_person}"
