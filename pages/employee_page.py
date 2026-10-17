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

    def reset_filter(self):
        self.button_reset.click()

    def get_employee_row(self, employee_name):
        return self.page.get_by_role("row").filter(has_text=employee_name)

    def get_employee_result(self, employee_name):
        return self.get_employee_row(employee_name)

    def get_employee_id(self, employee_name):
        row = self.get_employee_row(employee_name)

        return row.get_by_role("cell").nth(1)

    def get_employee_last_name(self, employee_name):
        row = self.get_employee_row(employee_name)

        return row.get_by_role("cell").nth(3)
    