# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2015, Ocado Innovation Limited
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ADDITIONAL TERMS – Section 7 GNU General Public Licence
#
# This licence does not grant any right, title or interest in any “Ocado” logos,
# trade names or the trademark “Ocado” or any other trademarks or domain names
# owned by Ocado Innovation Limited or the Ocado group of companies or any other
# distinctive brand features of “Ocado” as may be secured from time to time. You
# must not distribute any modification of this program using the trademark
# “Ocado” or claim any affiliation or association with Ocado or its employees.
#
# You are not authorised to use the name Ocado (or any of its trade names) or
# the names of any author or contributor in advertising or for publicity purposes
# pertaining to the distribution of this program, without the prior written
# authorisation of Ocado.
#
# Any propagation, distribution or conveyance of this program must include this
# copyright notice and these terms. You must not misrepresent the origins of this
# program; modified versions of the program must be marked as such and not
# identified as the original program.
from portal.tests.pageObjects.portal.base_page import BasePage

class TeacherPasswordResetFormPage(BasePage):
    def __init__(self, browser):
        super(TeacherPasswordResetFormPage, self).__init__(browser)

        self.wait_for_element_by_id('teacherPasswordResetForm_page')

        assert self.browser.find_element_by_id('id_email').get_attribute('placeholder') == 'my.email@address.com'

    def cancel(self):
        from portal.tests.pageObjects.portal.home_page import HomePage

        self.browser.find_element_by_id('cancel_button').click()
        return HomePage(self.browser)

    def reset_email_submit(self, email):
        self.browser.find_element_by_id('id_email').send_keys(email)

        self.wait_for_element_by_id('reset_button')

        self.browser.find_element_by_id('reset_button').click()
        return self
