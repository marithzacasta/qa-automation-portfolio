class EmployeePage:
    def __init__(self,page):
        self.page = page
        self.employee_name = page.locator(".oxd-input-group").filter(has_text="Employee Name").locator("input")
        self.employee_id = page.locator(".oxd-input-group").filter(has_text="Employee Id").locator("input")
        self.button_search = page.get_by_role("button", name = "Search")
        self.button_reset = page.get_by_role("button", name = "Reset")
        self.no_records = page.locator(".orangehrm-horizontal-padding").get_by_text("No Records Found")


    def search_employee(self, employee_name):
        self.employee_name.fill(employee_name)
        self.button_search.click()

    def get_employee_result(self, employee_name):
        return self.page.get_by_role("row").filter(
            has_text=employee_name
        )

    def reset_filter(self):
        self.button_reset.click()
