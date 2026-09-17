class LoginPage: # COMO INTERACTUO CON LOGIN
    def __init__(self,page): #¿Dónde está el elemento?
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.boton_login = page.get_by_role("button", name = "Login")
        self.mensaje_error = page.get_by_role("alert")
        self.username_required = page.locator(".oxd-input-group").filter(has_text="Username").get_by_text("Required")
        self.password_required = page.locator(".oxd-input-group").filter(has_text="Password").get_by_text("Required")

    def login(self, username, password): # ¿Qué hacemos con ese elemento?
        self.username.fill(username)
        self.password.fill(password)
        self.boton_login.click()

  