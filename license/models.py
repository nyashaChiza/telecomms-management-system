from django.db import models
from django.contrib.auth.models import User


APPLICATION_STATUS_CHOICES = (
        ('Appoved', 'Approved'),
        ('Pending', 'Pending'),
        ('Denied', 'Denied'),
    )

class License(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Disabled', 'Disabled'),
    )
    
    
    LICENSE_TYPE_CHOICES = (
        ('perpetual', 'Perpetual'),
        ('subscription', 'Subscription'),
        ('Temporary', 'Temporary'),
    )
    
    APPLICATION_TYPE_CHOICES = (
        ('private_mobile_network', 'Private Mobile Network'),
        ('coverage_licensing', 'Coverage Licensing'),
        ('private_telecoms_network', 'Private Telecoms Network'),
        ('equipment_approval', 'Equipment Approval'),
        ('frequency_spectrum_allocation', 'Frequency Spectrum Allocation')
    )
    
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField( null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20)
    location = models.CharField(max_length=250, null=True, blank=True)
    tag = models.CharField(max_length=20, null=True, blank=True)  
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    terms = models.TextField()
    license_type = models.CharField(max_length=20, choices=LICENSE_TYPE_CHOICES)
    application_type = models.CharField(max_length=250, null=True, blank=True, choices=APPLICATION_TYPE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
class LicenseApplication(models.Model):
    license = models.ForeignKey(License, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications', blank=True, null=True)
    application_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    instruction = models.TextField(blank=True, null=True)
    preliminary = models.TextField(blank=True, null=True)
    applicant_name = models.CharField(max_length=255, blank=True, null=True)
    type_of_application = models.CharField(max_length=255, blank=True, null=True)
    applicant_address = models.TextField(blank=True, null=True)
    qualifications = models.TextField(blank=True, null=True)
    declaration = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    license_details = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=APPLICATION_STATUS_CHOICES, default='Pending')
    
    def __str__(self):
        return f'{self.license.title}'

class EquipmentApprovalApplication(LicenseApplication):
    application_no = models.CharField(max_length=255, blank=True, null=True)
    license_no = models.CharField(max_length=255, blank=True, null=True)
    physical_address = models.TextField(blank=True, null=True)
    postal_address = models.TextField(blank=True, null=True)
    nature_of_business = models.TextField(blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    technical_contact_name = models.CharField(max_length=255, blank=True, null=True)
    technical_contact_telephone = models.CharField(max_length=50, blank=True, null=True)
    technical_contact_mobile = models.CharField(max_length=50, blank=True, null=True)
    technical_contact_fax = models.CharField(max_length=50, blank=True, null=True)
    technical_contact_email = models.EmailField(blank=True, null=True)
    equipment_type = models.CharField(max_length=255, blank=True, null=True)
    equipment_details = models.TextField(blank=True, null=True)
    make = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    serial_no = models.CharField(max_length=255, blank=True, null=True)
    country_of_origin = models.CharField(max_length=255, blank=True, null=True)
    nomenclature = models.CharField(max_length=255, blank=True, null=True)
    manufacturer = models.CharField(max_length=255, blank=True, null=True)
    mounting = models.CharField(max_length=255, blank=True, null=True)
    supplier_name = models.CharField(max_length=255, blank=True, null=True)
    supplier_telephone = models.CharField(max_length=50, blank=True, null=True)
    supplier_fax = models.CharField(max_length=50, blank=True, null=True)
    accessories_list = models.TextField(blank=True, null=True)
    applicant_title = models.CharField(max_length=255, blank=True, null=True)
    approval_status = models.CharField(max_length=20, choices=[('Passed', 'Passed'), ('Failed', 'Failed')], blank=True, null=True)
    certificate_collection_date = models.DateField(blank=True, null=True)
    collected_by = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Equipment Approval for {self.applicant_name}'
    
class PrivateMobileNetworkLicenseApplication(LicenseApplication):
    application_no = models.CharField(max_length=255, blank=True, null=True)
    license_no = models.CharField(max_length=255, blank=True, null=True)
    postal_address = models.TextField(blank=True, null=True)
    physical_address = models.TextField(blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    private_telecommunication_service = models.CharField(max_length=50, choices=[('Local', 'Local'), ('National', 'National')], blank=True, null=True)
    company_profile = models.TextField(blank=True, null=True)
    shareholding = models.TextField(blank=True, null=True)
    ceo_details = models.TextField(blank=True, null=True)
    senior_managers_details = models.TextField(blank=True, null=True)
    auditors_lawyers_details = models.TextField(blank=True, null=True)
    project_proposal = models.TextField(blank=True, null=True)
    service_description = models.TextField(blank=True, null=True)
    area_of_operation = models.TextField(blank=True, null=True)
    premises_details = models.TextField(blank=True, null=True)
    technical_information = models.TextField(blank=True, null=True)
    equipment_details = models.TextField(blank=True, null=True)
    spectrum_usage = models.TextField(blank=True, null=True)
    past_disciplinary_actions = models.TextField(blank=True, null=True)
    litigation_history = models.TextField(blank=True, null=True)
    judgment_debt = models.TextField(blank=True, null=True)
    insolvency_details = models.TextField(blank=True, null=True)


    def __str__(self):
        return f'Private Mobile Network License for {self.applicant_name}'

class FrequencySpectrumAllocationLicenseApplication(LicenseApplication):
    temporary_specific_field = models.CharField(max_length=100, blank=True, null=True)
    application_no = models.CharField(max_length=255, blank=True, null=True)
    license_no = models.CharField(max_length=255, blank=True, null=True)
    postal_address = models.TextField(blank=True, null=True)
    physical_address = models.TextField(blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    frequency_band = models.CharField(max_length=255, blank=True, null=True)
    frequency_range = models.CharField(max_length=255, blank=True, null=True)
    frequency_bandwidth = models.CharField(max_length=255, blank=True, null=True)
    transmitter_location = models.TextField(blank=True, null=True)
    receiver_location = models.TextField(blank=True, null=True)
    transmitter_power = models.CharField(max_length=255, blank=True, null=True)
    receiver_sensitivity = models.CharField(max_length=255, blank=True, null=True)
    equipment_description = models.TextField(blank=True, null=True)
    purpose_of_use = models.TextField(blank=True, null=True)
    technical_specifications = models.TextField(blank=True, null=True)
  

    def __str__(self):
        return f'Frequency Spectrum Allocation License for {self.applicant_name}'
    
class CoverageLicenseApplication(LicenseApplication):
    temporary_specific_field = models.CharField(max_length=100, blank=True, null=True)
    application_no = models.CharField(max_length=255, blank=True, null=True)
    license_no = models.CharField(max_length=255, blank=True, null=True)
    postal_address = models.TextField(blank=True, null=True)
    physical_address = models.TextField(blank=True, null=True)
    telephone = models.CharField(max_length=50, blank=True, null=True)
    geographical_area = models.TextField(blank=True, null=True)
    coverage_plan = models.TextField(blank=True, null=True)
    population_coverage = models.CharField(max_length=255, blank=True, null=True)
    infrastructure_details = models.TextField(blank=True, null=True)
    service_description = models.TextField(blank=True, null=True)
    technical_specifications = models.TextField(blank=True, null=True)
    financial_information = models.TextField(blank=True, null=True)
    business_plan = models.TextField(blank=True, null=True)
    compliance_details = models.TextField(blank=True, null=True)
    past_experience = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Coverage License Application for {self.applicant_name}'
    
    