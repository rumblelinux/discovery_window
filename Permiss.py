import wmi

w = wmi.WMI()

# Get all users and groups
users = w.Win32_UserAccount()
groups = w.Win32_Group()

# Get the names of all administrators
admins = []
for group in groups:
    if group.Name == "Administrators":
        admins = [a.Name for a in group.associators(wmi_result_class="Win32_UserAccount")]

# Print user information
print("Users:")
for user in users:
    print(f"  Name: {user.Name}")
    print(f"  Administrator: {user.Name in admins}")
    print()

# Print group information
print("Groups:")
for group in groups:
    print(f"  Name: {group.Name}")
    print("  Members:")
    for member in group.associators(wmi_result_class="Win32_UserAccount"):
        print(f"    {member.Name}")
    print()
