import csv

count = 0

with open('calls.csv', mode='r') as all_reports_file:
	reader = csv.reader(all_reports_file)
	with open('vehicles.csv', mode='w') as vehicle_report_outfile:
		writer = csv.writer(vehicle_report_outfile)
		writer.writerow(["Crime Id", "Original Crime Type Name", "Report Date", "Call Date", "Offense Date", "Call Time", "Call Date Time", "Disposition", "Address", "City", "State", "Agency Id", "Address Type", "Common Location"])
		for row in reader:
			if count < 80000 and "vehicle" in row[1].lower():
				writer.writerow(row)
				count += 1



