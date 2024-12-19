from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


class LoginPage():
    def _init_(self, driver):
        self.driver = driver

    _email = "username"
    _password = "password"
    _login = "/html/body/main/section/div/div/div/form/div[2]/button"

    def Email(self):
        return self.driver.find_element(By.ID, self._email)

    def Password(self):
        return self.driver.find_element(By.ID, self._password)

    def Loginbutton(self):
        return self.driver.find_element(By.ID, self._login)

    def enterEmail(self, email):
        self.Email().send_keys(email)

    def enterPassword(self, password):
        self.Password().send_keys(password)

    def clicklogin(self):
        self.Loginbutton().click()

    def login(self, email, password):
        self.Email(email)
        self.Password(password)
        self.clicklogin()