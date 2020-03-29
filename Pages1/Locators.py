class Locator(object):
#home page locator
    logo = "//img[@alt='Mercury Tours']"
    sign_on = "//a[contains(text(),'SIGN-ON')]"
    register = "//a[contains(text(),'REGISTER')]"
    support = "//a[contains(text(),'SUPPORT')]"
    contact = "//a[contains(text(),'CONTACT')]"

#Registration page locator
    regis_txt = "//*[contains(text(),'basic information')]"
    firstName = "//input[@name='firstName']"
    lastName = "//input[@name='lastName']"
    phone = "//input[@name='phone']"
    email = "//input[@name='userName']"
    country = "//select[@name='country']"
    userName = "//input[@name='email']"
    password = "//input[@name='password']"
    confirmPassword = "//input[@name='confirmPassword']"
    submit = "//input[@name='submit']"

#Post Registration locator
    thank_you = "//*[contains(text(),'Thank you for registering')]"
    post_user = "//*[contains(text(),'Your user name is')]"

#sign on page locator
    signOn_userName = "//input[@name='userName']"
    signOn_password = "//input[@name='password']"
    signOn_login = "//input[@name='login']"
    signOn_txt = "//*[contains(text(),'Enter your user')]"
    signOn_registerLink = "//a[@href='mercuryregister.php']"
