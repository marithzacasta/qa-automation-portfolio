from pages.employee_page import EmployeePage
# from pages.login_page import LoginPage
from playwright.sync_api import expect


# def test_validar_elementos(logged_in_page): #TEST DE ERRORES

#     employee_page = EmployeePage(logged_in_page)

#     print("URL actual:", logged_in_page.url)
#     print("Título:", logged_in_page.title())

#     print("Search:", employee_page.button_search.count())
#     print("Employee name:", employee_page.employee_name.count())

#     expect(employee_page.button_search).to_be_visible()
#     expect(employee_page.employee_name).to_be_visible()

    

def test_successful_search_employee(logged_in_page):

    employee_page = EmployeePage(logged_in_page)
    employee_page.search_employee("Orange")

    expect(employee_page.get_employee_result("Orange")).to_be_visible()


def test_invalid_search_employee(logged_in_page):

    employee_page = EmployeePage(logged_in_page)
    employee_page.search_employee("Invalido")

    expect(employee_page.no_records).to_contain_text("No Records Found")


def test_reset_search_employee(logged_in_page):

    employee_page = EmployeePage(logged_in_page)
    employee_page.search_employee("Orange")

    employee_page.reset_filter()

    expect(employee_page.employee_name).to_have_value("")

    