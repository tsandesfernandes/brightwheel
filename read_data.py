import csv
from datetime import datetime

def read_csv(csv_file):
    with open(csv_file, 'r', encoding='cp1252') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data

def std_nevada(data):
    std_data = []
    for row in data:
        # print(row)
        ages_served = []
        if row.get('Infant') == 'Y': 
            ages_served.append('Infant')
        if row.get('Toddler') == 'Y': 
            ages_served.append('Toddler')
        if row.get('Preschool') == 'Y': 
            ages_served.append('Preschool')
        if row.get('School') == 'Y': 
            ages_served.append('School')
        std_row = {
            'accepts_financial_aid': 'N/A', # couldnt make a relation to any value
            'ages_served': ','.join(ages_served),
            'capacity': row.get('Capacity') if row.get('Capacity') else 0,
            'certificate_expiration_date': None, # couldnt make a relation to any value
            'city': row.get('City') if row.get('City') else 'N/A',
            'address1': row.get('Address') if row.get('Address') else 'N/A',
            'address2': 'N/A',
            'company': row.get('Operation/Caregiver Name') if row.get('Operation/Caregiver Name') else 'N/A',
            'phone': row.get('Phone') if row.get('Phone') else 'N/A',
            'phone2': 'N/A',
            'county': row.get('County') if row.get('County') else 'N/A',
            'curriculum_type': 'N/A',
            'email':  'N/A',
            'first_name': 'N/A',
            'language': 'N/A',
            'last_name': 'N/A',
            'license_status': row.get('Status') if row.get('Status') else 'N/A',
            'license_issued': datetime.strptime(row.get('Issue Date'), '%m/%d/%Y') if row.get('Issue Date') else None,
            'license_number':  row.get('Operation #') if row.get('Operation #') else 0,
            'license_renewed': None,
            'license_type': row.get('Type') if row.get('Type') else 'N/A',
            'licensee_name': 'N/A',
            'max_age': 0,
            'min_age': 0,
            'operator': 'N/A',
            'provider_id': row.get('Agency Number'),
            'schedule': 'N/A',
            'state': row.get('State'),
            'title': 'N/A',
            'website_address': 'N/A',
            'zip': row.get('Zip'),
            'facility_type': 'N/A',
            'source': 'Nevada'

        }
        std_data.append(std_row)
    return std_data

def std_oklahoma(data):
    std_data = []
    
    for row in data:
        schedule = []
        ages_served = []
        if row.get("Mon"):
            schedule.append(f"Monday - {row.get('Mon')}")
        if row.get("Tues"):
            schedule.append(f"Tuesday - {row.get('Tues')}")
        if row.get("Wed"):
            schedule.append(f"Wednesday - {row.get('Wed')}")
        if row.get("Thurs"):
            schedule.append(f"Thursday - {row.get('Thurs')}")
        if row.get("Friday"):
            schedule.append(f"Friday - {row.get('Friday')}")
        if row.get("Saturday"):
            schedule.append(f"Saturday - {row.get('Saturday')}")
        if row.get("Sunday"):
            schedule.append(f"Sunday - {row.get('Sunday')}")
        
        if row.get("Ages Accepted 1"):
            ages_served.append(row.get("Ages Accepted 1"))
        if row.get("AA2"):
            ages_served.append(row.get("AA2"))
        if row.get("AA3"):
            ages_served.append(row.get("AA3"))
        if row.get("AA4"):
            ages_served.append(row.get("AA4"))

        std_row = {            
            'accepts_financial_aid': row.get('Accepts Subsidy'),
            'ages_served': ','.join(ages_served),
            'capacity': row.get('Total Cap') if row.get('Total Cap') else 0,
            'certificate_expiration_date': None, # couldnt make a relation to any value
            'city': row.get('City') if row.get('City') else 'N/A',
            'address1': row.get('Address1') if row.get('Address1') else 'N/A',
            'address2': row.get('Address2'),
            'company': row.get('Company') if row.get('Company') else 'N/A',
            'phone': row.get('Phone') if row.get('Phone') else 'N/A',
            'phone2': 'N/A',
            'county': row.get('County') if row.get('County') else 'N/A',
            'curriculum_type': 'N/A',
            'email': row.get('Email') if row.get('Email') else 'N/A',
            'first_name': 'N/A',
            'language': 'N/A',
            'last_name': 'N/A',
            'license_status': row.get('Status') if row.get('Status') else 'N/A',
            'license_issued': datetime.strptime(row.get('License Monitoring Since').split(" ")[-1], '%Y-%m-%d') if row.get('License Monitoring Since') else None,
            'license_number': row.get('Subsidy Contract Number').split(" ")[-1] if row.get('Subsidy Contract Number') and type(row.get('Subsidy Contract Number').split(" ")[-1]) == int else 0,
            'license_renewed': None,
            'license_type': row.get('Type License') if row.get('Type License') else 'N/A',
            'licensee_name': 'N/A',
            'max_age': 0,
            'min_age': 0,
            'operator': 'N/A',
            'provider_id': row.get('Subsidy Contract Number'),
            'schedule': ','.join(schedule),
            'state': row.get('State'),
            'title': 'N/A',
            'website_address': 'N/A',
            'zip': row.get('Zip'),
            'facility_type': 'N/A',
            'source': 'Oklahoma'
        }
        std_data.append(std_row)
    return std_data


def std_texas(data):
    std_data = []
    
    for row in data:
        schedule = []
        ages_served = []
        if row.get("Mon"):
            schedule.append(f"Monday - {row.get('Mon')}")
        if row.get("Tues"):
            schedule.append(f"Tuesday - {row.get('Tues')}")
        if row.get("Wed"):
            schedule.append(f"Wednesday - {row.get('Wed')}")
        if row.get("Thurs"):
            schedule.append(f"Thursday - {row.get('Thurs')}")
        if row.get("Friday"):
            schedule.append(f"Friday - {row.get('Friday')}")
        if row.get("Saturday"):
            schedule.append(f"Saturday - {row.get('Saturday')}")
        if row.get("Sunday"):
            schedule.append(f"Sunday - {row.get('Sunday')}")
        
        if row.get("Ages Accepted 1"):
            ages_served.append(row.get("Ages Accepted 1"))
        if row.get("AA2"):
            ages_served.append(row.get("AA2"))
        if row.get("AA3"):
            ages_served.append(row.get("AA3"))
        if row.get("AA4"):
            ages_served.append(row.get("AA4"))

        std_row = {            
            'accepts_financial_aid': row.get('Accepts Subsidy'),
            'ages_served': ','.join(ages_served),
            'capacity': row.get('Capacity') if row.get('Capacity') else 0,
            'certificate_expiration_date': None, # couldnt make a relation to any value
            'city': row.get('City') if row.get('City') else 'N/A',
            'address1': row.get('Address1') if row.get('Address1') else 'N/A',
            'address2': row.get('Address2'),
            'company': row.get('Company') if row.get('Company') else 'N/A',
            'phone': row.get('Phone') if row.get('Phone') else 'N/A',
            'phone2': 'N/A',
            'county': row.get('County') if row.get('County') else 'N/A',
            'curriculum_type': 'N/A',
            'email': row.get('Email') if row.get('Email') else 'N/A',
            'first_name': 'N/A',
            'language': 'N/A',
            'last_name': 'N/A',
            'license_status': row.get('Status') if row.get('Status') else 'N/A',
            'license_issued': datetime.strptime(row.get('License Monitoring Since').split(" ")[-1], '%Y-%m-%d') if row.get('License Monitoring Since') else None,
            'license_number': row.get('Operation #') if row.get('Operation #') else 0,
            'license_renewed': None,
            'license_type': row.get('Type License') if row.get('Type License') else 'N/A',
            'licensee_name': 'N/A',
            'max_age': 0,
            'min_age': 0,
            'operator': 'N/A',
            'provider_id': row.get('Subsidy Contract Number'),
            'schedule': ','.join(schedule),
            'state': row.get('State'),
            'title': 'N/A',
            'website_address': 'N/A',
            'zip': row.get('Zip'),
            'facility_type': 'N/A',
            'source': 'Texas'
        }
        std_data.append(std_row)
    return std_data


def return_std_data():


    nevada_data = read_csv('07-07-2023 Nevada Dept of Public _ Behavioral Health.csv')
    oklahoma_data = read_csv('07-07-2023 Oklahoma Human Services.csv')
    texas_data = read_csv('07-07-2023 Texas DHHS.csv')

    nevada_std = std_nevada(nevada_data)
    oklahoma_std = std_oklahoma(oklahoma_data)
    # still need to parse texas data
    texas_std = []

    return [nevada_std, oklahoma_std, texas_std]

