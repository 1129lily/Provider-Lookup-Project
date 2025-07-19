
# Healthcare Provider Search Website

## 1. Background

The objective of this project is to create a web-based system that allows users to search for and locate healthcare providers.

**Data Sources:**
- **NPI Data:** [https://download.cms.gov/nppes/NPI_Files.html](https://download.cms.gov/nppes/NPI_Files.html)
- **Taxonomy Data:** [https://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40/csv-mainmenu-57](https://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40/csv-mainmenu-57)
- **Original Reference Site:** [https://npiregistry.cms.hhs.gov/search](https://npiregistry.cms.hhs.gov/search)

### Planned Enhancements Compared to Original Site

1. Simplify the search page by targeting only the most relevant fields for users.
2. Embed Google Maps directly on the site for address-based browsing.
3. Provide users with the ability to download full provider information.

## 2. AI Guidance for Website Creation

I asked Claude the following question:

I want to build a website using Django, with a presentation style similar to [download.cms.gov/nppes/NPI_Files.html](https://download.cms.gov/nppes/NPI_Files.html). In short, I have more or less finished organizing the database, and the website will generally consist of the following parts:

##### (1) Search Page

<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/fbe3de9b-f901-44c9-aa29-dc211c1501d6" />

- First name and last name do **not** require exact matching.

- The **State** dropdown supports:

  - A searchable input at the top.

  - A scrollable list of all 50 U.S. states.

- Only one input field needs to be filled to trigger a search.

### (2) Results

<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/c9954f8e-4501-4e8b-a569-0fe0957af3d0" />

- After clicking the **Search** button, the results appear in a list view.

- The **Address** field in each result should be a hyperlink to **Google Maps**.

- A **Full Information** link should lead to a detail page with all stored data about that provider.

Please help me to construct the website step by step.

## 3. Claude’s Suggested Steps

### Step 1: Initialize Project and Basic Setup

```bash
django-admin startproject npi_search
cd npi_search
python manage.py startapp providers
pip install django
pip install django-widget-tweaks  # For form styling
```

### Step 2: Create Data Models

- Edit `providers/models.py`

### Step 3: Create Search Form

- Create `providers/forms.py`

### Step 4: Create Views

- Edit `providers/views.py`

### Step 5: Configure URLs

- Create `providers/urls.py`
- Update `npi_search/urls.py`

### Step 6: Create Templates

- `templates/base.html`
- `templates/providers/search.html`
- `templates/providers/detail.html`

### Step 7: Configure Settings

- Modify `npi_search/settings.py`

### Step 8: Create Admin Interface

- Edit `providers/admin.py`

### Step 9: Database Migration and Initialization

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Step 10: (Optional) Data Import Script

- This step is still under development. Steps 1–9 have been completed.

## 4. Next Steps

- [ ] Connect the site to the backend database.
- [ ] Embed Google Maps in the results.
- [ ] Create an interface for users to download all provider information as a CSV.
- [ ] Establish a data sync mechanism to update the site database automatically when the source data is updated.

---
