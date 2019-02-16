import csv

with open('calls.csv', mode='r') as all_reports_file:
	reader = csv.reader(all_reports_file)
	with open('vehicles.csv', mode='w') as vehicle_report_outfile:
		writer = csv.writer(vehicle_report_outfile)
		writer.writerow(["Incident Datetime", "Incident Date", "Incident Time", "Incident Year", "Incident Day of Week", "Report Datetime", "Row ID", "Incident ID", "Incident Number", "CAD Number", "Report Type Code", "Report Type Description", "Filed Online", "Incident Code", "Incident Category", "Incident Subcategory", "Incident Description", "Resolution", "Intersection", "CNN", "Police District", "Analysis Neighborhood", "Supervisor District", "Latitude", "Longitude", "point"])
		for row in reader:
			if "vehicle" in row[14].lower():
				writer.writerow(row)



