from django.db import models

# 美国州的选择
US_STATES = [
    ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'),
    ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'),
    ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'),
    ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'),
    ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
    ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'),
    ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'),
    ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'),
    ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'),
    ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
    ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'),
    ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('DC', 'District of Columbia'),
]

class Provider(models.Model):
    # NPI number
    npi = models.CharField(max_length=10, unique=True, db_index=True)
    
    # name
    first_name = models.CharField(max_length=100, blank=True, db_index=True)
    last_name = models.CharField(max_length=100, blank=True, db_index=True)
    middle_name = models.CharField(max_length=100, blank=True)
    
    # address
    address_line_1 = models.CharField(max_length=200, blank=True)
    address_line_2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True, db_index=True)
    state = models.CharField(max_length=2, choices=US_STATES, blank=True, db_index=True)
    postal_code = models.CharField(max_length=20, blank=True, db_index=True)
    
    # taxonomy
    primary_taxonomy = models.CharField(max_length=200, blank=True)
    credential = models.CharField(max_length=20, blank=True)
    
    # other information
    organization_name = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    fax = models.CharField(max_length=20, blank=True)
    
    # timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'providers'
        indexes = [
            models.Index(fields=['first_name', 'last_name']),
            models.Index(fields=['city', 'state']),
        ]
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.npi}"
    
    @property
    def full_name(self):
        name_parts = [self.first_name, self.middle_name, self.last_name]
        return ' '.join([part for part in name_parts if part])
    
    @property
    def full_address(self):
        address_parts = []
        if self.address_line_1:
            address_parts.append(self.address_line_1)
        if self.address_line_2:
            address_parts.append(self.address_line_2)
        if self.city:
            address_parts.append(self.city)
        if self.state:
            address_parts.append(self.get_state_display())
        if self.postal_code:
            address_parts.append(self.postal_code)
        return ', '.join(address_parts)
    
    @property
    def google_maps_url(self):
        """generate a Google Maps URL for the provider's address"""
        if self.full_address:
            import urllib.parse
            return f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote(self.full_address)}"
        return None