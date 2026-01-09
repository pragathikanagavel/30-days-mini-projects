print("SMART EMAIL SUBJECT LINE GENERATOR")
print("----------------------------------")

print("Choose email purpose:")
print("1. Job Application")
print("2. Leave Request")
print("3. Meeting Request")
print("4. Follow-up Email")
print("5. Complaint")

choice = input("Enter your choice (1-5): ")

if choice == "1":
    print("\nSuggested Subject Lines:")
    print("- Application for Job Opportunity")
    print("- Resume Submission for Your Review")
    print("- Applying for Open Position")

elif choice == "2":
    print("\nSuggested Subject Lines:")
    print("- Request for Leave on [Date]")
    print("- Leave Application")
    print("- Seeking Approval for Leave")

elif choice == "3":
    print("\nSuggested Subject Lines:")
    print("- Request to Schedule a Meeting")
    print("- Meeting Discussion Proposal")
    print("- Availability for Meeting")

elif choice == "4":
    print("\nSuggested Subject Lines:")
    print("- Following Up on Previous Email")
    print("- Gentle Reminder")
    print("- Checking In")

elif choice == "5":
    print("\nSuggested Subject Lines:")
    print("- Issue Regarding Service")
    print("- Formal Complaint Submission")
    print("- Concern Requiring Immediate Attention")

else:
    print("\nInvalid choice. Please enter a number between 1 and 5.")

