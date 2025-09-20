# This program organizes and displays a student's academic, financial, and personal portfolio using Python data types and calculations.

#personal information storage

full_name = "Chloe Barnes"
student_email = "cebarnes3@ncat.edu"
hometown = "Hampton, VA"
graduation_semester = "Spring 2029"
major = "Computer Science"

#Academic data organization (list)

course = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
completed = ["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]
credit_hours = [3, 3, 3, 3]
gpa = [3.2, 3.6, 3.4, 3.7]

#Contact information storage (tuple)

contact = ("Mom", "Hannah Smith", "704-555-0199")
address = ("456 Oak Street", "Charlotte", "NC", 28202)
instagram = ("Instagram", "@jordan_codes", 312)
twitter = ("Twitter", " @jordandev", 127)
birthday = ("Birthday", 5, 22, 2006)

#Intrest tracking (exact values)

current_skills = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
skills_learn = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
career_intrest = {"Software development", "Web development", "Data science", "Game development"}
hobbies = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment = {"One Piece", "Barry", "Life", "Incantation", "Memento"}

#organization mapping (dictionary values)

credit_dictionary = {course[0]: credit_hours[0], course[1]: credit_hours[1], course[2]: credit_hours[2], course[3]: credit_hours[3]}
professors_directory = {course[0]: "Prof. Rhodes", course[1]: "Dr. Lee", course[2]: "Dr. Martinez", course[3]: "Dr. Brown"}
room_directory = {course[0]: "M-Eric 300", course[1]: "Marteena 201", course[2]: "Crosby 121", course[3]: "Crosby 210"}
budget_directory = {"Food": 450, "Entertainment": 200, "Books": 125, "Transportation": 100}
study_hours = {"Programming": 10, "Math": 8, "English": 4, "History": 3}
contact_directory = {contact[0]: contact[2], "Roommate": "336-555-7821", "Academic Advisor": "336-334-5000"}

#Required calculations

total_credits = sum(credit_hours)
cumulative_gpa = ((gpa[0] * credit_hours[0] + gpa[1] * credit_hours[1] + gpa[2] * credit_hours[2] + gpa[3] * credit_hours[3])/total_credits)
count_complete = len(completed)
total_study = sum(study_hours.values())
academic_load = total_credits + total_study
monthly_budget = sum(budget_directory.values())
daily_food = (budget_directory["Food"]/ 30)
annual_budget = (monthly_budget * 12)
study_cost = (budget_directory["Books"]/total_study)

#Analytics Calculations

total_followers = instagram[2] + twitter[2]
platforms = 2
current_skills_count = len(current_skills)
skills_to_learn_count = len(skills_learn)
contact_count = len(contact_directory)
entertainment_count = len(entertainment)
academic_workload = academic_load


#Print all code
print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")
print("Student:", full_name, "|", "Email:", student_email)
print("From:", hometown, "|", "Graduating:", graduation_semester)
print("Major:", major)
print("")
print("=== ACADEMIC PROFILE ===")
print("Current Semester:", total_credits, "credits across", len(course), "courses")
print(f"Cumulative GPA: {cumulative_gpa:.2f}")
print("Weekly Study Time:", total_study, "hours")
print("Academic Investment: $", study_cost, "per study hour")
print("")
print("Current Courses:")
print(f"{course[0]} - {credit_dictionary[course[0]]} credits - {professors_directory[course[0]]} - {room_directory[course[0]]}")
print(f"{course[1]} - {credit_dictionary[course[1]]} credits - {professors_directory[course[1]]} - {room_directory[course[1]]}")
print(f"{course[2]} - {credit_dictionary[course[2]]} credits - {professors_directory[course[2]]} - {room_directory[course[2]]}")
print(f"{course[3]} - {credit_dictionary[course[3]]} credits - {professors_directory[course[3]]} - {room_directory[course[3]]}")
print("")
print("=== PERSONAL DEVELOPMENT ===")
print("Current Skills:", current_skills)
print("Learning Goals:", skills_learn)
print("Career Interests:", career_intrest)
print("Skills Currently Have:", len(current_skills))
print("Skills Want to Learn:", len(skills_learn))
print("")
print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthly_budget}")
print(f"Food: ${budget_directory["Food"]} (${daily_food:.1f}/day)")
print(f"Entertainment: ${budget_directory["Entertainment"]}")
print(f"Books: ${budget_directory["Books"]}")
print(f"Transportation: ${budget_directory["Transportation"]}")
print(f"Annual Projection: ${annual_budget}")
print("")
print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {contact[1]} ({contact[0]}) - {contact[2]}")
print(f"Home Address: {address[0]}, {address[1]}, {address[2]} {address[3]}")
print(f"Social Media Presence: {total_followers} followers across {platforms} platforms")
print(f"Key Contacts: {len(contact_directory)} people in directory")
print("")
print("=== LIFE STATISTICS ===")
print("Total Courses Completed:", len(completed))
print("Current Academic Load:", academic_load, "weekly commitments")
print("Entertainment Backlog:", len(entertainment), "items")
print("Current Hobbies:", len(hobbies), "activities")

print("================================================================")
