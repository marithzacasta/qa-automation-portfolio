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


def test_employee_id(logged_in_page):
    employee_page = EmployeePage(logged_in_page)
    employee_page.search_employee("Orange")

    employee_id = employee_page.get_employee_id("Orange")

    print("RESULTADO FALLIDO", employee_id)

    expect(employee_id).to_have_text("0001")


def test_employee_last_name(logged_in_page):
    employee_page = EmployeePage(logged_in_page)
    employee_page.search_employee("Orange")

    last_name = employee_page.get_employee_last_name("Orange")

    expect(last_name).to_have_text("Test")


def test_search_employee_and_validate_information(logged_in_page):
    employee_page = EmployeePage(logged_in_page)

    # Buscar empleado
    employee_page.search_employee("Orange")

    # Validar que aparece el empleado
    employee = employee_page.get_employee_result("Orange")
    expect(employee).to_be_visible()

    # Validar ID
    employee_id = employee_page.get_employee_id("Orange")
    expect(employee_id).to_have_text("0001")

    # Validar apellido
    last_name = employee_page.get_employee_last_name("Orange")
    expect(last_name).to_have_text("Test")


