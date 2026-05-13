from django.db import models

# Create your models here.
class LogRegister_Details(models.Model):  
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Digital_Marketing_Head', 'Digital_Marketing_Head'),
        ('Team_Lead', 'Team_Lead'),
        ('Executive', 'Executive'),
        ('Data_Manager', 'Data_Manager'),
        ('Telecaller', 'Telecaller')
    ]
    
    log_username = models.CharField(max_length=255, blank=True, null=True, default='')
    log_password = models.CharField(max_length=255, blank=True, null=True, default='')
    log_date = models.DateField(auto_now_add=True)
    log_time = models.TimeField(auto_now_add=True)
    position = models.CharField(max_length=50, choices=ROLE_CHOICES, null=True, blank=True)
    is_staff = models.BooleanField(default=False)  
    active_status = models.BooleanField(default=True)  

    def __str__(self):
        return self.log_username or "Unnamed User"


class DistributorRegister_Details(models.Model):
    login = models.ForeignKey('LogRegister_Details', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True, default='')
    contact_no = models.CharField(max_length=255, blank=True, null=True, default='')
    email = models.EmailField(max_length=255, blank=True, null=True)
    agencies = models.CharField(max_length=255, blank=True, null=True, default='')
    profile = models.FileField(upload_to='profiles/', blank=True, null=True)
    file = models.FileField(upload_to='employee_files/', blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True, default='')
    address2 = models.CharField(max_length=255, blank=True, null=True, default='')
    address3 = models.CharField(max_length=255, blank=True, null=True, default='')
    pin = models.CharField(max_length=50, blank=True, null=True, default='')
    location = models.CharField(max_length=150, blank=True, null=True, default='')
    district = models.CharField(max_length=150, blank=True, null=True, default='')
    state = models.CharField(max_length=150, blank=True, null=True, default='')
    active_status = models.BooleanField(default=False)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name or "Unnamed Distributor"



class BusinessRegister_Details(models.Model):
    login = models.ForeignKey('LogRegister_Details', on_delete=models.CASCADE, null=True, blank=True)
    distributor = models.ForeignKey('DistributorRegister_Details', on_delete=models.CASCADE, null=True, blank=True)
    owner_fname = models.CharField(max_length=255, blank=True, null=True, default='')
    owner_lname = models.CharField(max_length=255, blank=True, null=True, default='')
    company_name = models.CharField(max_length=255, blank=True, null=True, default='')
    contact_number = models.CharField(max_length=255, blank=True, null=True, default='')
    email = models.EmailField(max_length=255, blank=True, null=True)
    logo = models.FileField(upload_to='profiles/', blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True, default='')
    address_line1 = models.CharField(max_length=255, blank=True, null=True, default='')
    address_line2 = models.CharField(max_length=255, blank=True, null=True, default='')
    address_line3 = models.CharField(max_length=255, blank=True, null=True, default='')
    pin = models.CharField(max_length=50, blank=True, null=True, default='')
    location = models.CharField(max_length=150, blank=True, null=True, default='')
    district = models.CharField(max_length=150, blank=True, null=True, default='')
    state = models.CharField(max_length=150, blank=True, null=True, default='')
    active_status = models.BooleanField(default=True)
    reg_date = models.DateField(auto_now_add=True)
    company_code = models.CharField(max_length=150, default='COMID001')

    def __str__(self):
        return self.company_name or "Unnamed Business"

class DepartmentRegister_Details(models.Model):
    business = models.ForeignKey(BusinessRegister_Details, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, default='', null=True, blank=True)
    active_status = models.BooleanField(default=True)
    description = models.TextField(default='', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'department_register_details'

    def __str__(self):
        return self.name or "Unnamed Department"
    
class DesignationRegister_Details(models.Model):
    ROLE_CHOICES = [
        ('Digital_Marketing_Head', 'Digital_Marketing_Head'),
        ('Team_Lead', 'Team_Lead'),
        ('Executive', 'Executive'),
        ('Data_Manager', 'Data_Manager'),
        ('Telecaller', 'Telecaller')
    ]
    
    business = models.ForeignKey(BusinessRegister_Details, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(DepartmentRegister_Details, on_delete=models.CASCADE, null=True, blank=True)
    dashboard_id = models.CharField(max_length=50, choices=ROLE_CHOICES,null=True, blank=True) 
    name = models.CharField(max_length=255, default='', null=True, blank=True)
    description = models.TextField(default='', null=True, blank=True)
    active_status = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'designation_register_details'

    def __str__(self):
        return self.name or "Unnamed Designation"
    
class EmployeeRegister_Details(models.Model):
    login = models.ForeignKey(LogRegister_Details, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(BusinessRegister_Details, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(DepartmentRegister_Details, on_delete=models.CASCADE, null=True, blank=True)
    designation = models.ForeignKey(DesignationRegister_Details, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=255, default='', null=True, blank=True)
    employee_code = models.CharField(max_length=255, default='EMP001', null=True, blank=True)
    contact_number = models.CharField(max_length=255, default='', null=True, blank=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles', default='')
    documents = models.FileField(upload_to='employee_files', default='')

    address_line1 = models.CharField(max_length=255, default='', null=True, blank=True)
    address_line2 = models.CharField(max_length=255, default='', null=True, blank=True)
    address_line3 = models.CharField(max_length=255, default='', null=True, blank=True)
    pin = models.CharField(max_length=50, default='', null=True, blank=True)
    location = models.CharField(max_length=150, default='', null=True, blank=True)
    district = models.CharField(max_length=150, default='', null=True, blank=True)
    state = models.CharField(max_length=150, default='', null=True, blank=True)
    STATUS_CHOICES = (
        ('Approved','Approved'),
        ('Pending','Pending'),
    )
    active_status = models.CharField(max_length=50,choices=STATUS_CHOICES,null=True,default='Pending')
    verification_status = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True, null=True)

    class Meta:
        db_table = 'employee_register_details'

    def __str__(self):
        return self.name or "Unnamed Employee"
        
class Work_Task(models.Model):
    comp_taskid = models.ForeignKey(BusinessRegister_Details, on_delete=models.CASCADE, null=True, default="")
    task_name = models.CharField(max_length=255, default="", null=True, blank=True)
    task_description = models.TextField(default="", null=True, blank=True)
    task_add_time = models.TimeField(auto_now_add=True, null=True,blank=True)
    task_status = models.IntegerField(default=0)
    task_add_date = models.DateField(auto_now=True, null=True)
    
class ClientRegister(models.Model):
    compId = models.ForeignKey(BusinessRegister_Details, on_delete=models.CASCADE, null=True,default='')
    client_name = models.CharField(max_length=255,default='',null=True,blank=True)
    client_email_primary = models.EmailField(default='client@gmail.com',null=True,blank=True)
    client_email_alter = models.EmailField(default='client@gmail2.com',null=True,blank=True)
    client_phone = models.CharField(max_length=255,default='9000000009',null=True,blank=True)
    client_phone_alter = models.CharField(max_length=255,default='9000000009',null=True,blank=True)
    client_address1 = models.CharField(max_length=255,default='',null=True,blank=True)
    client_address2 = models.CharField(max_length=255,default='',null=True,blank=True)
    client_address3 = models.CharField(max_length=255,default='',null=True,blank=True)
    client_place = models.CharField(max_length=255,default='',null=True,blank=True)
    client_district = models.CharField(max_length=255,default='',null=True,blank=True)
    client_state = models.CharField(max_length=255,default='',null=True,blank=True)
    client_profile = models.ImageField(upload_to='client/profile',default='')

    #Bussiness Details ---

    client_bussiness_name = models.CharField(max_length=255,default='9000000009',null=True,blank=True)
    client_bussiness_email_primary = models.EmailField(default='client@gmail.com',null=True,blank=True)
    client_bussiness_email_alter = models.EmailField(default='client@gmail2.com',null=True,blank=True)
    client_bussiness_phone = models.CharField(max_length=255,default='9000000009',null=True,blank=True)
    client_bussiness_phone_alter = models.CharField(max_length=255,default='9000000009',null=True,blank=True)
    client_bussiness_website = models.CharField(max_length=255,default='',null=True,blank=True)
    client_bussiness_address1 = models.CharField(max_length=255,default='',null=True,blank=True)
    client_bussiness_address2 = models.CharField(max_length=255,default='',null=True,blank=True)
    client_bussiness_address3 = models.CharField(max_length=255,default='',null=True,blank=True)
    client_bussiness_place = models.CharField(max_length=255,default='',null=True,blank=True)
    client_bussiness_district = models.CharField(max_length=255,default='',null=True,blank=True)
    client_bussiness_state = models.CharField(max_length=255,default='',null=True,blank=True)
    client_bussiness_files = models.ImageField(upload_to='client/files',default='')
    bussiness_logo = models.ImageField(upload_to='client/logo',default='')
    more_description = models.TextField(default='',null=True,blank=True)
    client_add_time = models.TimeField(auto_now_add=True,null=True,blank=True)
    client_status = models.IntegerField(default=0)
    work_reg_status = models.IntegerField(default=0)
    client_reg_date = models.DateField(auto_now=True,null=True)

class WorkRegister(models.Model):
    wcompId = models.ForeignKey(BusinessRegister_Details, on_delete=models.CASCADE, null=True, default='')
    clientId = models.ForeignKey(ClientRegister, on_delete=models.CASCADE, null=True, default='')
    allocated_emp = models.ManyToManyField(EmployeeRegister_Details, related_name='works_allocated')
    work_description = models.TextField(default='', null=True, blank=True)
    work_create_time = models.TimeField(auto_now_add=True, null=True, blank=True)
    work_file = models.FileField(upload_to='work/files', default='')
    work_progress = models.IntegerField(default=0)
    work_allocate_status = models.IntegerField(default=0)
    work_status = models.IntegerField(default=0)
    work_create_date = models.DateField(auto_now=False, null=True)
    work_end_date = models.DateField(auto_now=False, null=True)

class ClientTask_Register(models.Model):
    cTcompId = models.ForeignKey(BusinessRegister_Details, on_delete=models.CASCADE, null=True,default='')
    client_Id = models.ForeignKey(ClientRegister, on_delete=models.CASCADE, null=True,default='')
    work_Id = models.ForeignKey(WorkRegister, on_delete=models.CASCADE, null=True,default='')
    task_name = models.CharField(max_length=255,default='',null=True,blank=True)
    task_description = models.TextField(default='',null=True,blank=True)
    task_file = models.FileField(upload_to=r'work/task/files',default='')
    task_allocate_status = models.IntegerField(default=0)
    task_total_progress = models.IntegerField(default=0)
    task_status = models.IntegerField(default=0)
    task_create_date = models.DateField(auto_now=False,null=True)
    
class Allocation_Details(models.Model):
    allocatEmp_id=models.ForeignKey(EmployeeRegister_Details,on_delete=models.CASCADE,null=True,default='')
    allocat_to=models.ForeignKey(EmployeeRegister_Details,on_delete=models.CASCADE,related_name="EmployeeRegister",null=True,default='')
    allocate_status=models.IntegerField(default=0)
    allocation_date=models.DateField(auto_now=False,null=True)
    
class EmployeeSchedule(models.Model):
    emp_id = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, null=True, default='')
    start_time = models.TimeField(auto_now=False, default='',null=True,blank=True)
    end_time = models.TimeField(auto_now=False, default='',null=True,blank=True)
    schedule_head = models.CharField(max_length=255, default='',null=True,blank=True)
    todo_content = models.TextField(default='',null=True,blank=True)
    log_time = models.TimeField(auto_now_add=True,null=True,blank=True)
    schedule_status = models.IntegerField(default=0)
    schedule_date = models.DateField(auto_now=False, null=True)

class EmployeeLeave(models.Model):
    emp_id = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, null=True, default='')
    start_date = models.DateField(auto_now=False, default='',null=True,blank=True)
    end_date = models.DateField(auto_now=False, default='',null=True,blank=True)
    leave_type = models.CharField(max_length=255, default='',null=True,blank=True)
    leave_reason = models.TextField(default='',null=True,blank=True)
    no_of_days = models.IntegerField(default=0)
    leave_status = models.IntegerField(default=0)
    leave_apply_date = models.DateField(auto_now=False, null=True)
    leave_statuChange_date = models.DateField(auto_now=False, null=True)
    leave_request_file = models.FileField(upload_to=r'leave\files', default='')
    
class ActionTaken(models.Model):
    act_emp_id = models.ForeignKey(EmployeeRegister_Details,on_delete=models.CASCADE,null=True,default='')
    act_from_id = models.IntegerField(default=0)
    act_from_name = models.CharField(max_length=255,default='',null=True,blank=True)
    act_reason = models.TextField(default='',null=True,blank=True)
    act_head = models.CharField(max_length=255,default='',null=True,blank=True)
    act_content = models.TextField(default='',null=True,blank=True)
    action_date = models.DateField(auto_now=False,null=True)
    status = models.IntegerField(default=0)

class Feedback(models.Model):
    feedback_emp_id = models.ForeignKey(EmployeeRegister_Details,on_delete=models.CASCADE,null=True,default='')
    from_id = models.IntegerField(default=0)
    from_name = models.CharField(max_length=255,default='',null=True,blank=True)
    feedback_content = models.TextField(default='',null=True,blank=True)
    feedback_date = models.DateField(auto_now=False,null=True)
    
class Complaints(models.Model):
    complaint_emp_id = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE, null=True, default='')
    compaint_head = models.CharField(max_length=255, default='', null=True, blank=True)
    compaint_content = models.TextField(default='', null=True, blank=True)
    complaint_date = models.DateField(auto_now=True, null=True)
    action = models.TextField(default='', null=True, blank=True)
    action_date = models.DateField(auto_now=False, null=True)
    status = models.IntegerField(default=0)
    
class LeadCollection(models.Model):
    work_Id = models.ForeignKey(WorkRegister, on_delete=models.CASCADE, null=True)
    collection_head = models.CharField(max_length=255, null=True, blank=True)
    collection_description = models.TextField(null=True, blank=True)
    target = models.IntegerField(default=0)
    file = models.FileField(upload_to='lead_collection/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class LeadAllocation(models.Model):

    team_lead = models.ForeignKey(EmployeeRegister_Details,on_delete=models.CASCADE)
    task = models.ForeignKey(ClientTask_Register,on_delete=models.CASCADE,null=True,blank=True)

    work = models.ForeignKey(WorkRegister,on_delete=models.CASCADE)
    description = models.TextField(null=True,blank=True)

    lead_collection = models.ForeignKey(LeadCollection,on_delete=models.SET_NULL,null=True,blank=True)

    display_name = models.CharField(max_length=255,
                                    null=True,
                                    blank=True)

    target = models.IntegerField(default=0)

    # ADD THESE
    instagram = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    facebook = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    work_type = models.CharField(max_length=20,
                                 default="single")

    start_date = models.DateField(null=True,blank=True)

    end_date = models.DateField(null=True,blank=True)

    allocated_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='lead_allocation/',null=True,blank=True)
    status = models.CharField(max_length=20, default='Pending')
    accepted_date = models.DateTimeField(null=True, blank=True)

    def save(self,*args,**kwargs):

        if self.lead_collection and not self.display_name:
            self.display_name = self.lead_collection.collection_head

        super().save(*args,**kwargs)
        
class LeadField(models.Model):
    lead = models.ForeignKey(LeadCollection, on_delete=models.CASCADE, related_name="fields")
    
    field_name = models.CharField(max_length=255)
    field_type = models.CharField(max_length=50, default="text")  
    field_description = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.field_name} ({self.lead.collection_head})"
    
class LeadRow(models.Model):

    lead_collection = models.ForeignKey(
        LeadCollection,
        on_delete=models.CASCADE,
        related_name="rows"
    )

    full_name = models.CharField(max_length=255,null=True,blank=True)

    email = models.CharField(max_length=255,null=True,blank=True)

    contact = models.CharField(max_length=255,null=True,blank=True)

    source = models.CharField(max_length=255,null=True,blank=True)

    collected_by = models.ForeignKey(
        EmployeeRegister_Details,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ("Unverified","Unverified"),
        ("Verified","Verified"),
        ("Incomplete","Incomplete"),
        ("Waste","Waste"),
    ]

    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default="Unverified"
    )

    is_waste = models.BooleanField(default=False)

    waste_reason = models.TextField(null=True, blank=True)
    waste_marked_date = models.DateTimeField(null=True, blank=True)
    
    waste_status = models.BooleanField(default=False)  
    is_recall= models.BooleanField(default=False)
    is_repeated = models.BooleanField(default=False)
    


    is_transferred = models.BooleanField(default=False)

    transferred_to = models.ForeignKey(
        EmployeeRegister_Details,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="transferred_leads"
    )
    transfer_date = models.DateTimeField(null=True,blank=True)

class LeadRowValue(models.Model):

    lead_row = models.ForeignKey(
        LeadRow,
        on_delete=models.CASCADE,
        related_name="values"
    )

    field = models.ForeignKey(
        LeadField,
        on_delete=models.CASCADE
    )

    value = models.TextField(null=True, blank=True)
    
class teamleadallocation(models.Model):
    team_lead = models.ForeignKey(EmployeeRegister_Details,on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(   
        EmployeeRegister_Details,
        on_delete=models.CASCADE,
        related_name='assigned_tasks',
        null=True,
        blank=True
    )
    task = models.ForeignKey(ClientTask_Register,on_delete=models.CASCADE,null=True,blank=True)
    work = models.ForeignKey(WorkRegister,on_delete=models.CASCADE)
    description = models.TextField(null=True,blank=True)
    lead_collection = models.ForeignKey(LeadCollection,on_delete=models.SET_NULL,null=True,blank=True)
    display_name = models.CharField(max_length=255,null=True,blank=True)
    target = models.IntegerField(default=0)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    allocated_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='lead_allocation/',null=True,blank=True)
    status = models.CharField(max_length=20, default='Pending')
    accepted_date = models.DateTimeField(null=True, blank=True)

class DailyWork(models.Model):
    employee = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE)
    task = models.ForeignKey(ClientTask_Register, on_delete=models.CASCADE)
    allocation = models.ForeignKey(teamleadallocation, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField()

    target = models.IntegerField(default=0)
    work_date = models.DateField()

    file = models.FileField(upload_to='daily_work/', null=True, blank=True)
    verified_target =models.IntegerField(default=0)
    verification= models.CharField(max_length=50, default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)
    
class DailyWork2(models.Model):
    employee = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE)
    task = models.ForeignKey(ClientTask_Register, on_delete=models.CASCADE)
    
    singleallocation = models.ForeignKey(
    LeadAllocation,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)

    title = models.CharField(max_length=255)
    description = models.TextField()

    target = models.IntegerField(default=0)
    work_date = models.DateField()

    file = models.FileField(upload_to='daily_work/', null=True, blank=True)
    verified_target =models.IntegerField(default=0)
    verification= models.CharField(max_length=50, default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)

class progressreport(models.Model):
    REPORT_TYPE_CHOICES = [
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]
    employee = models.ForeignKey(EmployeeRegister_Details, on_delete=models.CASCADE)
    allocation = models.ForeignKey(teamleadallocation, on_delete=models.CASCADE)

    from_date = models.DateField()
    to_date = models.DateField()

    progress = models.IntegerField()
    description = models.TextField()

    file = models.FileField(upload_to='weekly_reports/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=50, default='Pending')
    report_type = models.CharField(
        max_length=10,
        choices=REPORT_TYPE_CHOICES,
        default='weekly'   
    )

class FollowUpStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class followUpUpdates(models.Model):
    response=models.ForeignKey(FollowUpStatus,on_delete=models.SET_NULL,null=True,blank=True)
    next_update_date=models.DateField(null=True,blank=True)
    reason=models.TextField(null=True,blank=True)
    call_record=models.FileField(upload_to='followup_calls/',null=True,blank=True)
    lead=models.ForeignKey(LeadRow,on_delete=models.CASCADE,null=True,blank=True)
    updated=models.DateTimeField(auto_now_add=True)

    user=models.ForeignKey(EmployeeRegister_Details,on_delete=models.SET_NULL,null=True,blank=True)
    notes=models.TextField(null=True,blank=True)
    is_close=models.BooleanField(default=False)
    close_date=models.DateTimeField(null=True,blank=True)
    
class Platform(models.Model):
    company = models.ForeignKey(BusinessRegister_Details, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name