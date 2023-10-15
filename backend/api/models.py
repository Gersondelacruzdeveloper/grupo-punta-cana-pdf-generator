from django.db import models
from django.contrib.auth.models import User


class Template(models.Model):
    TEMPLATE_TYPE = [
        ('BoardingPass', 'BoardingPass'),
        ('Invoice', 'Invoice'),
        ('Advertisement', 'Advertisement'),
    ]
    name = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    type = models.CharField(max_length=50, choices=TEMPLATE_TYPE)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
 
# BoardingPass model
class GeneratedBoardingPass(models.Model):
    name = models.CharField(max_length=100, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.ForeignKey(
        Template,
        on_delete=models.CASCADE,
        related_name='generated_boarding_passes',
        default=None,
        blank =True,
        null = True,
    )
    pdf_data = models.BinaryField()
    generated_at = models.DateTimeField(auto_now_add=True)
    passenger_name = models.CharField(max_length=255)
    seat_number = models.CharField(max_length=10)
    departure_date = models.DateTimeField()
    boarding_gate = models.CharField(max_length=10)

    def __str__(self):
        return f"Generated Boarding Pass for {self.passenger_name} at {self.generated_at}"
    
GeneratedBoardingPass.default_template = Template.objects.filter(
        type='BoardingPass', active=True).first()

# invoice model
class Invoice(models.Model):
    name = models.CharField(max_length=100, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invoices_created')
    template = models.ForeignKey(Template,
                                 on_delete=models.CASCADE,
                                 related_name='invoices_received',
                                 default=None,
                                 null = True,
                                 blank=True
                                 )
    invoice_number = models.CharField(
        max_length=20, unique=True, blank=True)  # Make it blank
    issue_date = models.DateField()
    due_date = models.DateField()
    # You can choose a different model for customers
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products_or_services = models.TextField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice {self.invoice_number} for {self.customer}"

    def save(self, *args, **kwargs):
        if not self.invoice_number:  # Generate invoice number only if it's not set
            last_invoice = Invoice.objects.all().order_by('invoice_number').last()
            if last_invoice:
                last_invoice_number = last_invoice.invoice_number
                new_invoice_number = int(last_invoice_number) + 1
            else:
                new_invoice_number = 1

            self.invoice_number = str(new_invoice_number).zfill(
                4)  # Adjust the format as needed

        super(Invoice, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Invoice"
        verbose_name_plural = "Invoices"

Invoice.default_template = Template.objects.filter(
        type='Invoice', active=True).first()

# Advertisement model
class Advertisement(models.Model):
    name = models.CharField(max_length=100, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.ForeignKey(Template,
                                 on_delete=models.CASCADE,
                                 related_name='Advertisement',
                                 default=None,
                                 blank=True,
                                 null=True,
                                 )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateTimeField()
    place = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
# Advertisement atribute to search for the right model
Advertisement.default_template = Template.objects.filter(
        type='Advertisement', active=True).first()