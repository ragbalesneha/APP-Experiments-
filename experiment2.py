from datetime import datetime

# --- Custom Decorator ---
def log_report_generation(func):
    """A decorator that logs when a report is generated and adds a timestamp header."""
    def wrapper(self, *args, **kwargs):
        print(f"[LOG] Generating report: '{self.title}' at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        result = func(self, *args, **kwargs)
        print(f"[LOG] Report generation complete.\n")
        return result
    return wrapper


class Report:
    # Class attribute to track the total number of reports generated across all instances
    total_reports_created = 0

    def __init__(self, title, author, content_sections=None):
        self.title = title
        self.author = author
        self.content_sections = content_sections if content_sections else []
        
        # Increment class-level counter upon instance creation
        Report.total_reports_created += 1

    @classmethod
    def get_total_reports(cls):
        """Class method to retrieve the total number of reports created."""
        return cls.total_reports_created

    @classmethod
    def create_template(cls, template_type, author):
        """Class method acting as a factory constructor for preset templates."""
        if template_type == "academic":
            return cls(
                title="Academic Progress & Performance Report",
                author=author,
                content_sections=["Introduction", "Coursework & CGPA", "Extracurriculars", "Conclusion"]
            )
        elif template_type == "technical":
            return cls(
                title="Technical Project Architecture Report",
                author=author,
                content_sections=["Abstract", "System Design", "Implementation", "Results & Testing"]
            )
        else:
            return cls(title="General Report", author=author, content_sections=["Overview", "Details"])

    def add_section(self, section_text):
        """Instance method to dynamically add content sections to the report."""
        self.content_sections.append(section_text)

    @log_report_generation
    def generate_report(self):
        """Generates and formats the final report using the decorator."""
        separator = "=" * 50
        output = []
        output.append(separator)
        output.append(f"TITLE: {self.title}")
        output.append(f"AUTHOR: {self.author}")
        output.append(f"DATE: {datetime.now().strftime('%B %d, %Y')}")
        output.append(separator)
        output.append("SECTIONS:")
        for idx, section in enumerate(self.content_sections, 1):
            output.append(f"  {idx}. {section}")
        output.append(separator)
        
        formatted_report = "\n".join(output)
        print(formatted_report)
        return formatted_report

    # --- Magic Methods ---
    def __str__(self):
        """Magic method for a clean string representation of the report object."""
        return f"Report(Title: '{self.title}', Author: '{self.author}', Sections: {len(self.content_sections)})"

    def __len__(self):
        """Magic method returning the number of sections in the report using len()."""
        return len(self.content_sections)

    def __call__(self, new_title):
        """Magic method allowing the report instance to be called like a function to update its title."""
        self.title = new_title
        print(f"[UPDATE] Report title successfully updated to: '{self.title}'")


# ==================== Demonstration / Test Run ====================
if __name__ == "__main__":
    print("--- 1. Using Class Methods to Create Reports ---")
    # Creating a technical report template using the class method
    report1 = Report.create_template("technical", author="Sneha")
    
    # Creating an academic report template
    report2 = Report.create_template("academic", author="Sneha")

    print(f"Total reports initialized so far: {Report.get_total_reports()}\n")

    print("--- 2. Using Magic Methods (__str__ and __len__) ---")
    print(report1)
    print(f"Number of sections in report1 (via __len__): {len(report1)}\n")

    print("--- 3. Using Instance Methods & Decorator ---")
    report1.add_section("Future Scope & Enhancements")
    report1.generate_report()

    print("--- 4. Using Callable Magic Method (__call__) ---")
    # Calling the object directly to rename it
    report1("Advanced AI System Architecture Report")
    
    # Generate the report again to see the updated title
    report1.generate_report()