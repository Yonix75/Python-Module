required_packages = ["python3", "pip", "requests", "boto3", "pip"]
print(required_packages)
required_packages = set(required_packages)
print(required_packages)

print(f"Is requests {"requests" in required_packages}")
print(f"Is ansible {"ansible" in required_packages}")
required_packages.add("paramiko")
required_packages.discard("pip")
print(required_packages)
print("---------------------------------------------------------")
installed_packages = {"docker", "python3", "pip"}
missing_packages = required_packages - installed_packages
print(missing_packages)

extra_packages = installed_packages - required_packages
print(extra_packages)

common_packages = required_packages & installed_packages
print(common_packages)
