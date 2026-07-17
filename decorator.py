def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()  
    return wrapper

class Report:
    def __init__(self, title):
        self.title = title

    @classmethod
    def from_template(cls, template_name):
        
        templates = {
            "annual": "Annual Financial Performance Report",
            "monthly": "Monthly Progress and Analytics Summary",
            "weekly": "Weekly Team Status Update"
        }
       
        title = templates.get(template_name.lower(), template_name)
        return cls(title)

    def __str__(self):
        return f"Report Title: {self.title}"

    @uppercase_decorator
    def generate(self):
        return f"This is the report: {self.title}"

report1 = Report("Quarterly Sales Review")
print("--- Standard Report ---")
print(report1)             # Triggers __str__
print(report1.generate())  # Triggers generate() with uppercase_decorator

print("\n--- Template Report ---")
# 2. Testing the @classmethod alternative constructor
report2 = Report.from_template("annual")
print(report2)
print(report2.generate())